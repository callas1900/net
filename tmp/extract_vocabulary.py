#!/usr/bin/env python3
"""
merge.md から中・上級レベルの英単語を抽出し、raw_frequency.csv に出力する。
"""
import re
import csv
from collections import defaultdict, Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize

# ---- 章境界の定義 ----
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
MAX_LINE = 649  # L650 以降 (Authors/Acknowledgements/References) は除外

# Glossary に出てくる重要なハイフン語（トークナイザで分割されないよう保護）
COMPOUND_WORDS = [
    "blame-aware",
    "post-mortem",
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

# 追加の基礎語ブラックリスト（stopwords で取りきれないもの）
EXTRA_STOPWORDS = {
    # 基本動詞
    "have", "has", "had", "been", "being", "will", "would", "could",
    "should", "might", "shall", "must", "can", "may", "does", "done",
    "went", "come", "came", "get", "got", "gotten", "make", "made",
    "take", "took", "taken", "give", "gave", "given", "see", "seen",
    "know", "knew", "known", "think", "thought", "want", "need",
    "look", "find", "found", "go", "going", "gone", "let", "keep",
    "kept", "put", "set", "say", "said", "says", "tell", "told",
    "call", "show", "become", "became", "come", "feel", "felt",
    "try", "tried", "bring", "brought", "hold", "held", "turn",
    "run", "ran", "lead", "led", "build", "built", "begin", "began",
    "spend", "spent", "read", "send", "sent", "write", "wrote",
    "add", "play", "ask", "asked", "appear", "remain", "close",
    "open", "move", "moved", "change", "changed", "follow", "allow",
    "include", "identify", "develop", "understand", "provide",
    "consider", "ensure", "require", "create", "start", "focus",
    "happen", "help",
    # 基本形容詞・副詞
    "also", "even", "just", "like", "much", "many", "most", "some",
    "such", "well", "very", "here", "there", "then", "than", "back",
    "over", "around", "along", "ahead", "already", "often", "still",
    "next", "each", "same", "more", "less", "however", "whether",
    "further", "instead", "forward", "ever", "once", "within", "good",
    "best", "right", "left", "long", "short", "sure", "really",
    "particularly", "generally", "simply", "typically", "again",
    "always", "sometimes", "usually", "likely", "quickly", "several",
    "little", "quite", "enough", "hard", "difficult", "easy", "free",
    "high", "low", "deep", "large", "small", "early", "later",
    "greater", "lower", "higher", "similar", "different", "various",
    "especially", "although", "because", "either", "neither",
    "indeed", "though", "therefore", "moreover", "furthermore",
    "available", "additional", "potential", "possible", "necessary",
    "appropriate", "effective", "current", "overall", "related",
    "important", "specific", "clear", "certain", "multiple",
    "whole", "full", "real", "particular", "complete",
    # 基本名詞
    "way", "time", "day", "year", "week", "thing", "things",
    "someone", "anyone", "everyone", "something", "anything",
    "everything", "person", "people", "place", "point", "part",
    "order", "number", "level", "case", "kind", "word", "idea",
    "note", "story", "image", "header", "home",
    "work", "step", "item", "guide", "company", "team", "group",
    "area", "role", "first", "second", "third", "end", "line",
    "able", "list", "initial", "new", "given", "common",
    "name", "section", "content", "sense", "example", "look",
    # 基本形容詞・副詞（追加）
    "great", "simple", "clean", "beyond", "behind", "almost",
    "never", "truly", "probably", "regularly", "actually",
    "certainly", "clearly", "directly", "quickly", "easily",
    "happened", "happening", "understood", "involved", "continued",
    # 縮約形（追加）
    "can't", "cannot", "won't",
    # 数字語・ノイズ
    "nine", "ten", "appendix",
    # 固有名詞（著者・大学関連）
    "vaughan", "johan", "bergstrom", "lund", "university",
    # 代名詞・限定詞
    "your", "their", "them", "they", "what", "when", "where",
    "which", "while", "from", "into", "this", "that", "these",
    "those", "about", "upon", "during", "before", "after", "since",
    "without", "under", "above", "across", "between", "through",
    "except", "plus", "versus", "towards", "another", "other",
    # 縮約形
    "you'll", "we'll", "they'll", "it'll", "you've", "we've",
    "they've", "you're", "we're", "they're", "it's", "don't",
    "doesn't", "didn't", "won't", "wouldn't", "couldn't", "shouldn't",
    "isn't", "aren't", "wasn't", "weren't", "haven't", "hasn't",
    "hadn't", "that's", "there's", "here's", "what's", "who's",
    "let's", "i'm", "i've", "i'll", "i'd", "you'd", "we'd", "they'd",
    "he's", "she's", "he'd", "she'd", "he'll", "she'll",
    # その他ノイズ
    "pdonpd", "assets", "images", "headers", "howie", "jeli",
    "pagerduty", "png", "jpeg",
}


def get_chapter(line_num: int) -> str | None:
    for start, end, name in CHAPTER_BOUNDARIES:
        if start <= line_num <= end:
            return name
    return None


def normalize_unicode(text: str) -> str:
    """Unicode スマートクォート・ダッシュ等を ASCII に正規化"""
    replacements = {
        '‘': "'", '’': "'",  # 'LEFT/RIGHT SINGLE QUOTATION MARK
        '“': '"', '”': '"',  # "LEFT/RIGHT DOUBLE QUOTATION MARK
        '–': '-', '—': '-',  # EN/EM DASH
        '‑': '-',                  # NON-BREAKING HYPHEN
        '­': '',                   # SOFT HYPHEN
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def clean_markdown(text: str) -> str:
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    # 画像は alt テキストを保持（ただし典型的な "Header" 系は除去）
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
    # 引用符で始まる単語の引用符除去
    text = re.sub(r'["""''`]', ' ', text)
    return text


def protect_compounds(text: str) -> str:
    for cw in COMPOUND_WORDS:
        placeholder = cw.replace("-", "ZZHYPHENZZ")
        text = text.replace(cw, placeholder)
    return text


def restore_compounds(token: str) -> str:
    return token.replace("ZZHYPHENZZ", "-")


def strip_punctuation(token: str) -> str:
    """先頭・末尾の句読点を除去（ハイフン保護語以外）"""
    return re.sub(r'^[^\w]+|[^\w]+$', '', token)


WORDNET_POS = {
    "NN": "n", "NNS": "n", "NNP": "n", "NNPS": "n",
    "VB": "v", "VBD": "v", "VBG": "v", "VBN": "v", "VBP": "v", "VBZ": "v",
    "JJ": "a", "JJR": "a", "JJS": "a",
    "RB": "r", "RBR": "r", "RBS": "r",
}

NLTK_TO_JP_POS = {
    "NN": "名詞", "NNS": "名詞", "NNP": "固有名詞", "NNPS": "固有名詞",
    "VB": "動詞", "VBD": "動詞", "VBG": "動詞", "VBN": "動詞",
    "VBP": "動詞", "VBZ": "動詞",
    "JJ": "形容詞", "JJR": "形容詞", "JJS": "形容詞",
    "RB": "副詞", "RBR": "副詞", "RBS": "副詞",
    "IN": "前置詞", "CC": "接続詞",
    "DT": "冠詞", "PRP": "代名詞", "PRP$": "代名詞",
    "MD": "助動詞",
}

# 最小出現回数（これ未満の語は除外）
MIN_COUNT = 2

# Glossary の重要語は count=1 でも含める
ALWAYS_INCLUDE = {
    "blame-aware", "post-mortem", "post-incident", "on-call",
    "knowledge-elicitation", "calibration", "facilitator",
    "facilitated", "tacit", "elicitation", "blameless",
    "resilience", "countermeasure", "debrief",
}


def is_valid_token(token: str, stop_en: set) -> bool:
    if len(token) <= 3:
        return False
    if re.fullmatch(r'[\d\W_]+', token):
        return False
    if token in stop_en:
        return False
    if token in EXTRA_STOPWORDS:
        return False
    return True


def main():
    input_path = "merge.md"
    output_path = "raw_frequency.csv"

    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    stop_en = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    word_data: dict[str, dict] = defaultdict(lambda: {
        "pos_votes": Counter(),
        "chapters": {},
        "count": 0,
    })

    for line_idx, line in enumerate(lines):
        line_num = line_idx + 1
        if line_num > MAX_LINE:
            break
        chapter = get_chapter(line_num)
        if chapter is None:
            continue

        # Unicode 正規化 → ハイフン複合語保護 → Markdown クリーンアップ
        line_clean = normalize_unicode(line)
        line_clean = protect_compounds(line_clean)
        line_clean = clean_markdown(line_clean)

        try:
            tokens_raw = word_tokenize(line_clean)
        except Exception:
            tokens_raw = line_clean.split()

        if not tokens_raw:
            continue

        pos_tagged = pos_tag(tokens_raw)

        for token, pos in pos_tagged:
            # ハイフン複合語は復元してそのまま扱う
            if "ZZHYPHENZZ" in token:
                token = restore_compounds(token)
                # 末尾の句読点を除去し、複数形の -s も正規化して原形に統一
                token_lower = token.lower().rstrip('.,;:!?')
                token_lower = re.sub(r"'s$", '', token_lower)
                # 複数形 -ups → -up などは末尾 s を除去（複合語の場合）
                token_lower = re.sub(r'-(\w+)s$', lambda m: '-' + m.group(1), token_lower)
                if token_lower in EXTRA_STOPWORDS:
                    continue
                lemma = token_lower
                pos_jp = "複合語"
            else:
                # 先頭・末尾の句読点を除去
                token = strip_punctuation(token)
                if not token:
                    continue
                token_lower = token.lower()

                if not is_valid_token(token_lower, stop_en):
                    continue

                wn_pos = WORDNET_POS.get(pos, "n")
                lemma = lemmatizer.lemmatize(token_lower, pos=wn_pos)

                # 原形化後も有効か
                lemma = strip_punctuation(lemma)
                if not lemma or not is_valid_token(lemma, stop_en):
                    continue

                pos_jp = NLTK_TO_JP_POS.get(pos, "その他")

            data = word_data[lemma]
            data["count"] += 1
            data["pos_votes"][pos_jp] += 1
            if chapter not in data["chapters"]:
                data["chapters"][chapter] = line_num

    # 出力行の構築
    rows = []
    for lemma, data in word_data.items():
        count = data["count"]
        if count < MIN_COUNT and lemma not in ALWAYS_INCLUDE:
            continue
        top_pos = data["pos_votes"].most_common(1)[0][0]
        chapter_list = "; ".join(
            f"{ch}(L{ln})"
            for ch, ln in sorted(data["chapters"].items(), key=lambda x: x[1])
        )
        rows.append({
            "lemma": lemma,
            "pos_estimate": top_pos,
            "locations": chapter_list,
            "count": count,
        })

    rows.sort(key=lambda r: -r["count"])

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["lemma", "pos_estimate", "locations", "count"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"出力: {output_path}")
    print(f"語彙数: {len(rows)}")
    print("\n上位40語:")
    for r in rows[:40]:
        print(f"  {r['count']:>4}  {r['lemma']:<28}  {r['pos_estimate']:<10}  {r['locations'][:55]}")


if __name__ == "__main__":
    main()
