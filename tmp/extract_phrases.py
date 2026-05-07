#!/usr/bin/env python3
"""
merge.md から 2〜5 語の熟語を spaCy ルールベースで抽出し、raw_phrase_frequency.csv に出力する。
"""
import re
import csv
from collections import defaultdict

import spacy
from spacy.matcher import Matcher

# ---- 章境界（extract_vocabulary.py と同じ） ----
CHAPTER_BOUNDARIES = [
    (1,   61,  "Home"),
    (62,  106, "Assign"),
    (107, 191, "Analyze"),
    (192, 306, "Interview"),
    (307, 501, "Calibrate"),
    (502, 529, "Distribute"),
    (530, 537, "Closing Thoughts"),
    (538, 649, "Continued Learning"),
]
MAX_LINE = 649

# ハイフン複合語保護（extract_vocabulary.py に "postmortem" を追加）
COMPOUND_WORDS = [
    "blame-aware",
    "post-mortem",
    "postmortem",
    "post-incident",
    "on-call",
    "how-we-got-here",
    "near-miss",
    "third-party",
    "root-cause",
    "in-depth",
    "real-time",
    "well-rounded",
    "follow-up",
    "old-school",
    "blame-free",
    "one-on-one",
]

# 文字列一致で検出する慣用句・固定表現
# （POS パターンでは取れないもの、または確実に拾いたいもの）
IDIOMATIC_PHRASES = [
    "how we got here",
    "how-we-got-here",
    "lessons learned",
    "on the same page",
    "up to speed",
    "in hindsight",
    "out of scope",
    "in scope",
    "moving forward",
    "going forward",
    "real-time data",
    "on-call",
    # 出現が少なくても必ず含める重要ドメイン熟語
    "near miss",
    "near-miss",
    "root cause",
    "blameless culture",
    "hindsight bias",
    "shared mental model",
    "blame-free culture",
    "learning from incident",
    "in hindsight",
]

# 熟語レベルのノイズフィルタ（lemma/表層形で列挙）
PHRASE_STOPLIST = {
    "same time", "same way", "first time",
    "lot of", "number of", "kind of", "sort of",
    "piece of", "set of", "type of", "part of", "end of",
    "each other", "one another",
    "much more", "much less", "even more",
    "well as", "next step", "much time",
    # ジェネリック過ぎる形容詞+名詞
    "more detail", "more time", "more information", "more people",
    "different way", "different size", "different part",
    "different point", "different role", "different participant",
    "first step", "long time", "good candidate", "other time",
    "other event", "other engineer", "full scope", "few minute",
    "how many people", "many people",
    # 固有名詞ノイズ（製品名・著者名起因）
    "howie guide", "howie process", "howie methodology",
    "jeli process", "pagerduty process",
    "nora jones", "dr. johan", "dr. johan bergstrom",
    "lund university", "johan bergstrom", "toolbox image",
    # サブフレーズ（より長い熟語に含まれる）
    "matter expert", "item meeting", "subject matter",
    "analysis program", "potential action", "strong incident",
    "action items",  # "action item" の複数形（重複）
    # ノイズ・ジェネリック
    "number of term", "size company", "part process",
    "incident write", "value interview", "new way",
    "new investigation", "new process",
    "accident investigation podcast",  # 特定リソース名
    "availability of participant", "important aspect",
    "piece of software", "different timeline", "sufficient time",
    # PROPN 起因の誤抽出を直接ブロック
    "many organization", "many team", "many company",
    "key player",
}

MIN_COUNT = 2


def get_chapter(line_num: int):
    for start, end, name in CHAPTER_BOUNDARIES:
        if start <= line_num <= end:
            return name
    return None


def normalize_unicode(text: str) -> str:
    replacements = {
        '‘': "'", '’': "'",
        '“': '"', '”': '"',
        '–': '-', '—': '-',
        '‑': '-', '­': '',
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def clean_markdown(text: str) -> str:
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'!\[(?:.*?Header.*?|)\]\([^\)]*\)', ' ', text, flags=re.IGNORECASE)
    text = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)
    text = re.sub(r'\[[^\]]*\]', ' ', text)
    text = re.sub(r'\?\?\?\+?\s+\S+\s+"[^"]*"', ' ', text)
    text = re.sub(r'!!!\s+(?:tip|note|warning|question|info)\s+"[^"]*"', ' ', text)
    text = re.sub(r'!!!\s+(?:tip|note|warning|question|info)', ' ', text)
    text = re.sub(r'^#+\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r':-+:?|:[-]+', ' ', text)
    text = re.sub(r'\*+([^\*\n]+)\*+', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'https?://\S+', ' ', text)
    text = re.sub(r'\{[^}]+\}', ' ', text)
    text = re.sub(r'\[\d+\]', ' ', text)
    text = re.sub(r'\$\w+', ' ', text)
    text = re.sub(r'["“”‘’`]', ' ', text)
    return text


def protect_compounds(text: str) -> str:
    for cw in COMPOUND_WORDS:
        placeholder = cw.replace("-", "_HYPHEN_")
        # 大文字・小文字を問わず保護（"Post-Incident" も "post-incident" も対象）
        text = re.sub(re.escape(cw), placeholder, text, flags=re.IGNORECASE)
    return text


def restore_compound_in_token(s: str) -> str:
    # _HYPHEN_ は保護時に大文字で埋め込まれるが tok.text.lower() 後は小文字になる
    return s.replace("_HYPHEN_", "-").replace("_hyphen_", "-")


def get_phrase_lemma(span) -> str:
    """spaCy Span のトークン列を正規化して熟語キーを返す。

    規則:
    - 規則的複数形 (NNS/NNPS) のみ lemma に正規化（"items"→"item"）
    - 不規則複数・ラテン語複数 ("data", "criteria") は表層形を保持
    - それ以外（動名詞 "learning"、形容詞等）は表層形 (lowercase) を保持
    """
    tokens = []
    for tok in span:
        if tok.is_punct or tok.is_space:
            continue
        text = tok.text.lower()
        # 規則的複数形のみ lemma に変換
        if tok.tag_ in ("NNS", "NNPS"):
            lemma = tok.lemma_.lower()
            if (
                (text.endswith("s") and text[:-1] == lemma)
                or (text.endswith("es") and text[:-2] == lemma)
                or (text.endswith("ies") and text[:-3] + "y" == lemma)
                or (text.endswith("ves") and text[:-3] + "f" == lemma)
            ):
                word = lemma
            else:
                word = text  # 不規則複数 ("data"→"datum" を避ける) は表層形を保持
        else:
            word = text
        word = restore_compound_in_token(word)
        tokens.append(word)
    return " ".join(tokens)


def get_pos_pattern(span) -> str:
    return " ".join(
        tok.pos_
        for tok in span
        if not tok.is_punct and not tok.is_space
    )


def is_valid_phrase(lemma: str) -> bool:
    tokens = lemma.split()
    n = len(tokens)
    if n < 2 or n > 5:
        return False
    if lemma in PHRASE_STOPLIST:
        return False
    # 全トークンが 2 文字以下の機能語のみは除外
    if all(len(t) <= 2 for t in tokens):
        return False
    return True


def main():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("spaCy モデルが見つかりません。以下を実行してください:")
        print("  python -m spacy download en_core_web_sm")
        raise SystemExit(1)

    # Matcher: 複数の POS パターンを明示的に定義（greedy OP の問題を回避）
    matcher = Matcher(nlp.vocab)

    # ADJ/NOUN/PROPN の連続で NOUN/PROPN で終わるパターン（長さ 2〜5）
    np_patterns = []
    for total_len in range(2, 6):
        pattern = (
            [{"POS": {"IN": ["ADJ", "NOUN", "PROPN"]}} for _ in range(total_len - 1)]
            + [{"POS": {"IN": ["NOUN", "PROPN"]}}]
        )
        np_patterns.append(pattern)
    matcher.add("NOUN_PHRASE", np_patterns)

    # NOUN of NOUN[+] パターン（例: "chain of events", "course of action"）
    noun_of_patterns = []
    for tail_len in range(1, 4):  # 3〜5 トークン合計
        pattern = (
            [{"POS": {"IN": ["NOUN", "PROPN"]}}]
            + [{"LOWER": "of"}]
            + [{"POS": {"IN": ["NOUN", "PROPN"]}} for _ in range(tail_len)]
        )
        noun_of_patterns.append(pattern)
    matcher.add("NOUN_OF_NOUN", noun_of_patterns)

    phrase_data: dict[str, dict] = defaultdict(lambda: {
        "pos_pattern": "",
        "chapters": {},
        "count": 0,
        "is_idiomatic": False,
    })

    with open("merge.md", encoding="utf-8") as f:
        lines = f.readlines()

    for line_idx, line in enumerate(lines):
        line_num = line_idx + 1
        if line_num > MAX_LINE:
            break
        chapter = get_chapter(line_num)
        if chapter is None:
            continue

        line_norm = normalize_unicode(line)

        # 慣用句検索用: markdown クリーン後に lowercase（保護なし）
        line_for_idiom = clean_markdown(line_norm).lower()

        # spaCy 用: ハイフン複合語を保護してから markdown クリーン
        line_protected = protect_compounds(line_norm)
        line_for_spacy = clean_markdown(line_protected)

        # ---- (C) 慣用句辞書マッチ（文字列レベル） ----
        for idiom in IDIOMATIC_PHRASES:
            search_target = idiom.lower()
            if search_target in line_for_idiom:
                # 正規化: ハイフン形 → スペース形
                normalized = idiom.replace("-", " ").strip()
                data = phrase_data[normalized]
                data["count"] += 1
                data["pos_pattern"] = "固定表現"
                data["is_idiomatic"] = True
                if chapter not in data["chapters"]:
                    data["chapters"][chapter] = line_num

        # ---- spaCy パース ----
        doc = nlp(line_for_spacy)

        seen_spans: set[tuple[int, int]] = set()

        # ---- (A) 名詞句チャンク ----
        for chunk in doc.noun_chunks:
            # 先頭の DET/PRON/NUM を除去
            start = chunk.start
            while start < chunk.end and doc[start].pos_ in ("DET", "PRON", "NUM"):
                start += 1
            span_len = chunk.end - start
            if span_len < 2 or span_len > 5:
                continue
            span = doc[start:chunk.end]
            lemma = get_phrase_lemma(span)
            if not is_valid_phrase(lemma):
                continue
            key = (start, chunk.end)
            if key not in seen_spans:
                seen_spans.add(key)
                data = phrase_data[lemma]
                data["count"] += 1
                if not data["pos_pattern"]:
                    data["pos_pattern"] = get_pos_pattern(span)
                if chapter not in data["chapters"]:
                    data["chapters"][chapter] = line_num

        # ---- (B) Matcher パターン ----
        matches = matcher(doc)
        for _match_id, start, end in matches:
            span_len = end - start
            if span_len < 2 or span_len > 5:
                continue
            key = (start, end)
            if key in seen_spans:
                continue
            span = doc[start:end]
            lemma = get_phrase_lemma(span)
            if not is_valid_phrase(lemma):
                continue
            seen_spans.add(key)
            data = phrase_data[lemma]
            data["count"] += 1
            if not data["pos_pattern"]:
                data["pos_pattern"] = get_pos_pattern(span)
            if chapter not in data["chapters"]:
                data["chapters"][chapter] = line_num

    # フィルタリングと出力行の構築
    rows = []
    for lemma, data in phrase_data.items():
        count = data["count"]
        if count < MIN_COUNT and not data["is_idiomatic"]:
            continue
        chapter_list = "; ".join(
            f"{ch}(L{ln})"
            for ch, ln in sorted(data["chapters"].items(), key=lambda x: x[1])
        )
        rows.append({
            "lemma": lemma,
            "pos_pattern": data["pos_pattern"],
            "locations": chapter_list,
            "count": count,
        })

    rows.sort(key=lambda r: -r["count"])

    with open("raw_phrase_frequency.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["lemma", "pos_pattern", "locations", "count"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"出力: raw_phrase_frequency.csv")
    print(f"熟語数: {len(rows)}")
    print("\n上位40熟語:")
    for r in rows[:40]:
        print(f"  {r['count']:>4}  {r['lemma']:<40}  {r['pos_pattern']:<20}  {r['locations'][:45]}")


if __name__ == "__main__":
    main()
