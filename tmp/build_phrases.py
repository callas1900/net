#!/usr/bin/env python3
"""
raw_phrase_frequency.csv に日本語訳・品詞・カテゴリを付与して phrases.csv を生成する。
列構造は vocabulary.csv と同一:
  英語名, 日本語訳, 品詞, 対象分類, 関連語, 独自辞書, 場所, 出現数
"""
import csv

# lemma → (日本語訳, 品詞, 対象分類, 関連語, 独自辞書フラグ)
TRANSLATIONS: dict[str, tuple[str, str, str, str, str]] = {
    # ---- 会議・プロセス ----
    "learning review meeting":       ("学習レビュー会議 / ポストインシデント振り返り会議",  "名詞句", "会議",      "post-incident review / calibration document / facilitator", "○"),
    "post-incident review":          ("ポストインシデント・レビュー / 事後レビュー",          "名詞句", "会議",      "learning review meeting / post-mortem / debrief",            "○"),
    "post-incident meeting":         ("ポストインシデント・ミーティング",                     "名詞句", "会議",      "learning review meeting / facilitator",                      "×"),
    "post-incident process":         ("ポストインシデント・プロセス / 事後プロセス",          "名詞句", "プロセス",  "investigation / post-incident review",                       "×"),
    "post-incident report":          ("ポストインシデント・レポート / 事後報告書",            "名詞句", "ドキュメント", "distribute / finding",                                    "○"),
    "post-incident investigation":   ("ポストインシデント調査",                               "名詞句", "プロセス",  "investigation / investigator",                               "×"),
    "incident analysis":             ("インシデント分析",                                     "名詞句", "プロセス",  "analysis / finding / timeline",                              "×"),
    "incident response":             ("インシデント対応",                                     "名詞句", "プロセス",  "on-call / action item / escalation",                         "×"),
    "incident investigation":        ("インシデント調査",                                     "名詞句", "プロセス",  "investigator / finding / timeline",                          "○"),
    "incident report":               ("インシデントレポート / 事後報告書",                   "名詞句", "ドキュメント", "post-incident report / distribute",                       "×"),

    # ---- ドキュメント ----
    "calibration document":          ("キャリブレーション・ドキュメント / 認識合わせ資料",   "名詞句", "ドキュメント", "calibration / learning review meeting / facilitator",     "○"),
    "calibration report":            ("キャリブレーション・レポート",                         "名詞句", "ドキュメント", "calibration document / finding",                         "×"),
    "how we got here":               ("「ここに至った経緯」文書 (HWGH)",                     "固定表現", "ドキュメント", "calibration document / narrative / timeline",            "○"),
    "incident document":             ("インシデント文書",                                     "名詞句", "ドキュメント", "post-incident report / finding",                         "×"),

    # ---- アクション ----
    "action item":                   ("アクションアイテム / 改善項目 / 対応事項",            "名詞句", "行動",      "finding / improvement / remediation",                        "○"),
    "improvement action":            ("改善アクション",                                       "名詞句", "行動",      "action item / finding / remediation",                        "×"),
    "follow-up action":              ("フォローアップ・アクション",                           "名詞句", "行動",      "action item / follow-up",                                    "×"),

    # ---- インシデント要因・事象 ----
    "root cause":                    ("根本原因",                                             "名詞句", "概念",      "contributing factor / causal factor / analysis",             "○"),
    "contributing factor":           ("寄与要因 / 関連要因",                                 "名詞句", "概念",      "root cause / causal factor / analysis",                      "×"),
    "causal factor":                 ("因果要因",                                             "名詞句", "概念",      "root cause / contributing factor",                           "×"),
    "near miss":                     ("ニアミス / 危うく事故になりかけた事象",               "名詞句", "イベント",  "incident / near-miss / high-severity",                       "○"),
    "high-severity incident":        ("重大インシデント / 高重要度インシデント",              "名詞句", "イベント",  "near miss / escalation / on-call",                           "×"),
    "service outage":                ("サービス停止 / サービスアウテージ",                   "名詞句", "イベント",  "incident / downtime / escalation",                           "×"),

    # ---- 分析・調査プロセス ----
    "timeline analysis":             ("タイムライン分析",                                     "名詞句", "プロセス",  "timeline / narrative / event sequence",                      "×"),
    "event sequence":                ("イベントシーケンス / 事象の時系列",                   "名詞句", "プロセス",  "timeline / narrative / contributing factor",                  "×"),
    "data analysis":                 ("データ分析",                                           "名詞句", "プロセス",  "analysis / data / finding",                                  "×"),
    "cognitive bias":                ("認知バイアス",                                         "名詞句", "概念",      "hindsight bias / narrative / human factor",                  "○"),
    "hindsight bias":                ("後知恵バイアス",                                       "名詞句", "概念",      "cognitive bias / narrative / in hindsight",                  "○"),
    "shared mental model":           ("共有メンタルモデル",                                   "名詞句", "概念",      "calibration / shared understanding / knowledge",             "○"),

    # ---- ファシリテーション・インタビュー ----
    "interview question":            ("インタビュー質問",                                     "名詞句", "会議",      "interview / facilitator / interviewee",                      "×"),
    "follow-up question":            ("フォローアップ質問 / 掘り下げ質問",                  "名詞句", "会議",      "interview question / clarification",                          "○"),
    "open question":                 ("オープンクエスチョン / 開かれた質問",                 "名詞句", "会議",      "interview / facilitation / clarification",                    "×"),
    "open-ended question":           ("オープンエンド質問",                                   "名詞句", "会議",      "interview / open question",                                   "×"),
    "knowledge elicitation":         ("知識引き出し / ナレッジ・エリシテーション",           "名詞句", "プロセス",  "interview / facilitator / tacit knowledge",                  "○"),
    "tacit knowledge":               ("暗黙知",                                               "名詞句", "概念",      "knowledge elicitation / expert / experience",                "○"),

    # ---- 人物・役割 ----
    "lead investigator":             ("主任調査者",                                           "名詞句", "人物",      "investigator / facilitator",                                 "×"),
    "incident commander":            ("インシデントコマンダー",                               "名詞句", "人物",      "on-call / escalation / response",                            "×"),

    # ---- 組織・文化 ----
    "blameless culture":             ("ブレームレス文化 / 非難しない文化",                   "名詞句", "文化",      "blame-free / blame-aware / psychological safety",            "○"),
    "safety culture":                ("安全文化",                                             "名詞句", "文化",      "blameless culture / learning culture / resilience",          "×"),
    "learning culture":              ("学習文化 / 継続的学習の文化",                         "名詞句", "文化",      "safety culture / blameless culture / continuous improvement","×"),
    "continuous improvement":        ("継続的改善",                                           "名詞句", "概念",      "learning culture / action item / improvement",               "○"),
    "psychological safety":          ("心理的安全性",                                         "名詞句", "概念",      "blameless culture / safety culture",                         "○"),
    "organizational learning":       ("組織学習",                                             "名詞句", "概念",      "learning culture / knowledge / improvement",                 "○"),

    # ---- 固定表現・慣用句 ----
    "lessons learned":               ("学んだ教訓 / レッスンズ・ラーンド",                  "固定表現", "概念",    "learning / insight / improvement",                           "○"),
    "learning from incident":        ("インシデントからの学習 / 障害から学ぶ",                "固定表現", "概念",    "learning / insight / post-incident review",                   "○"),
    "on call":                       ("オンコール / 待機当番中",                                 "固定表現", "概念",    "on-call / incident response / escalation",                   "○"),
    "on the same page":              ("認識が一致している / 共通理解を持つ",                 "固定表現", "概念",    "calibration / shared understanding",                          "×"),
    "up to speed":                   ("状況を把握している / 最新情報を得ている",             "固定表現", "概念",    "context / knowledge / onboarding",                           "×"),
    "in hindsight":                  ("後から振り返ると / 後知恵では",                       "固定表現", "概念",    "hindsight bias / narrative / review",                        "×"),
    "moving forward":                ("今後は / これからは",                                  "固定表現", "概念",    "action item / improvement",                                  "×"),
    "going forward":                 ("今後は / 将来的に",                                    "固定表現", "概念",    "action item / improvement",                                  "×"),
    "out of scope":                  ("スコープ外 / 対象外",                                  "固定表現", "概念",    "scope / boundary / investigation",                           "×"),
    "in scope":                      ("スコープ内 / 対象範囲内",                              "固定表現", "概念",    "scope / boundary / investigation",                           "×"),

    # ---- 頻出・重要熟語（追加） ----
    "review meeting":                ("レビューミーティング",                                 "名詞句", "会議",    "learning review meeting / incident review / calibration",    "×"),
    "incident review":               ("インシデントレビュー",                                 "名詞句", "会議",    "post-incident review / learning review meeting",             "×"),
    "initial analysis":              ("初期分析",                                             "名詞句", "プロセス","analysis / preliminary / finding",                           "×"),
    "incident data":                 ("インシデントデータ",                                   "名詞句", "データ",  "data / timeline / source",                                   "×"),
    "investigation process":         ("調査プロセス",                                         "名詞句", "プロセス","investigation / workflow / approach",                         "×"),
    "learning review":               ("学習レビュー",                                         "名詞句", "会議",    "learning review meeting / post-incident review",             "×"),
    "postmortem meeting":            ("ポストモーテム・ミーティング / 事後検討会",            "名詞句", "会議",    "post-mortem / learning review meeting / debrief",            "○"),
    "resilience engineering":        ("レジリエンスエンジニアリング",                         "名詞句", "概念",    "resilience / safety culture / human performance",            "○"),
    "performance improvement":       ("パフォーマンス改善",                                   "名詞句", "概念",    "improvement / action item / learning",                        "×"),
    "facilitated meeting":           ("ファシリテーションされた会議",                         "名詞句", "会議",    "facilitator / learning review meeting",                      "×"),
    "subject matter expert":         ("業務領域専門家 / SME",                                "名詞句", "人物",    "expert / knowledge / interview",                             "○"),
    "incident response":             ("インシデント対応",                                     "名詞句", "プロセス","on-call / escalation / action item",                          "×"),
    "corrective action":             ("是正措置 / 修正アクション",                           "名詞句", "行動",    "action item / improvement / remediation",                    "○"),
    "incident review meeting":       ("インシデントレビューミーティング",                     "名詞句", "会議",    "learning review meeting / post-incident review",             "×"),
    "analysis process":              ("分析プロセス",                                         "名詞句", "プロセス","analysis / workflow / investigation",                         "×"),
    "action item meeting":           ("アクションアイテムミーティング",                       "名詞句", "会議",    "action item / follow-up / meeting",                          "×"),
    "investigation program":         ("調査プログラム",                                       "名詞句", "プロセス","investigation / process / program",                          "×"),
    "human performance":             ("人間パフォーマンス / ヒューマンパフォーマンス",       "名詞句", "概念",    "human factor / resilience / performance",                    "○"),
    "root-cause analysis":           ("根本原因分析 / RCA",                                  "名詞句", "プロセス","root cause / causal factor / analysis",                      "○"),
    "mental model":                  ("メンタルモデル / 思考モデル",                         "名詞句", "概念",    "shared mental model / cognitive / understanding",            "○"),
    "continuous learning":           ("継続的学習",                                           "名詞句", "概念",    "learning culture / organizational learning / improvement",   "○"),
    "accident investigation":        ("事故調査",                                             "名詞句", "プロセス","incident investigation / safety / analysis",                  "○"),
    "point of view":                 ("視点 / 観点 / 見方",                                  "固定表現", "概念",   "perspective / viewpoint / narrative",                        "×"),
    "key moment":                    ("重要な瞬間 / キーモーメント",                         "名詞句", "概念",    "timeline / event / analysis",                                "×"),
    "initial review":                ("初期レビュー",                                         "名詞句", "プロセス","review / calibration / analysis",                             "×"),
    "direct message":                ("ダイレクトメッセージ / DM",                           "名詞句", "データ",  "chat transcript / data source / Slack",                      "×"),
    "specific question":             ("具体的な質問",                                         "名詞句", "会議",    "interview question / facilitation / probe",                  "×"),
    "multiple perspective":          ("多様な視点 / 複数の観点",                             "名詞句", "概念",    "perspective / viewpoint / diversity",                        "×"),
    "interview note":                ("インタビューメモ / 聴取記録",                         "名詞句", "ドキュメント","interview / document / transcript",                        "×"),
    "final report":                  ("最終レポート / 最終報告書",                           "名詞句", "ドキュメント","report / distribute / finding",                            "×"),
    "incident report":               ("インシデントレポート / 事後報告書",                   "名詞句", "ドキュメント","post-incident report / distribute / finding",              "×"),
    "incident investigation":        ("インシデント調査",                                     "名詞句", "プロセス","investigator / investigation / analysis",                     "○"),
    "incident phase":                ("インシデントのフェーズ / 障害の段階",                 "名詞句", "概念",    "timeline / event / sequence",                                "×"),
    "insight generation":            ("インサイト生成 / 洞察の導出",                        "名詞句", "プロセス","insight / analysis / learning",                               "○"),
    "incident metric":               ("インシデント指標 / 障害メトリクス",                  "名詞句", "データ",  "metric / data / improvement",                                "×"),
    "dev team":                      ("開発チーム",                                           "名詞句", "組織",    "team / organization / participant",                          "×"),
    "incident analysis program":     ("インシデント分析プログラム",                           "名詞句", "プロセス","investigation program / process / learning",                  "○"),
    "new information":               ("新たな情報 / 追加情報",                               "名詞句", "データ",  "information / data / finding",                               "×"),
    "chat transcript":               ("チャットトランスクリプト / チャット履歴",             "名詞句", "データ",  "data source / document / timeline",                          "○"),
    "data source":                   ("データソース / 情報源",                               "名詞句", "データ",  "data / information / evidence",                              "×"),
    "contextual information":        ("文脈情報 / コンテキスト情報",                        "名詞句", "データ",  "context / information / background",                          "×"),
    "organizational change":         ("組織変更 / 組織的変化",                              "名詞句", "概念",    "organization / management / improvement",                     "×"),
    "visual representation":         ("視覚的な表現 / ビジュアル表示",                      "名詞句", "概念",    "timeline / data / diagram",                                   "×"),
    "opening remark":                ("開会の挨拶 / 冒頭発言",                              "名詞句", "会議",    "facilitator / meeting / introduction",                        "×"),
    "parking lot":                   ("パーキングロット（議題保留リスト）",                 "固定表現", "会議",   "action item / meeting / follow-up",                           "○"),
    "continued learning":            ("継続的学習",                                           "名詞句", "概念",    "learning / improvement / knowledge",                          "×"),
    "everyday work":                 ("日常業務 / 日々の仕事",                              "名詞句", "概念",    "work / normal operation / safety",                            "×"),
    "error reduction":               ("エラー削減 / ミス低減",                              "名詞句", "概念",    "improvement / prevention / quality",                          "×"),
    "valuable insight":              ("価値ある洞察",                                         "名詞句", "概念",    "insight / finding / learning",                               "×"),
    "deeper insight":                ("より深い洞察",                                         "名詞句", "概念",    "insight / analysis / investigation",                          "×"),
    "deeper analysis":               ("より深い分析",                                         "名詞句", "プロセス","analysis / investigation / narrative",                         "×"),
    "raw data":                      ("生データ / ローデータ",                              "名詞句", "データ",  "data / source / evidence",                                    "×"),
    "key theme":                     ("主要テーマ / キーテーマ",                            "名詞句", "概念",    "theme / finding / analysis",                                  "×"),
    "response effort":               ("対応作業 / レスポンス作業",                          "名詞句", "プロセス","incident response / escalation / action",                      "×"),
    "work ticket":                   ("作業チケット / ワークチケット",                       "名詞句", "データ",  "ticket / action item / tracking",                             "×"),
    "question survey":               ("質問サーベイ / アンケート",                          "名詞句", "会議",    "survey / question / data collection",                         "×"),
    "investigation technique":       ("調査テクニック / 調査手法",                          "名詞句", "プロセス","investigation / method / approach",                            "×"),
    "investigation report":          ("調査レポート / 調査報告書",                          "名詞句", "ドキュメント","report / post-incident report / finding",                  "×"),
    "future reader":                 ("将来の読者",                                           "名詞句", "人物",    "report / document / audience",                               "×"),
    "new approach":                  ("新しいアプローチ / 新たな手法",                        "名詞句", "概念",    "approach / method / process",                                 "×"),
    "mean time":                     ("平均時間 (障害対応指標: MTTR 等の文脈で使用)",        "名詞句", "データ",  "metric / incident metric / availability",                     "×"),
    "foundational level":            ("基礎レベル / 基本的なレベル",                          "名詞句", "概念",    "level / knowledge / skill",                                   "×"),
    "level of knowledge":            ("知識レベル",                                            "名詞句", "概念",    "knowledge / expertise / skill",                               "×"),
    "individual interview":          ("個別インタビュー",                                       "名詞句", "会議",    "interview / interviewee / one-on-one",                        "×"),
    "key participant":               ("主要参加者 / キーパーソン",                             "名詞句", "人物",    "participant / investigator / subject matter expert",          "×"),
    "incident participant":          ("インシデント参加者",                                     "名詞句", "人物",    "participant / responder / on-call",                           "×"),
    "distribution of finding":       ("発見事項の共有 / 調査結果の配布",                      "名詞句", "プロセス","finding / distribute / report",                                "×"),
    "initial finding":               ("初期の発見 / 初期所見",                                 "名詞句", "概念",    "finding / analysis / preliminary",                            "×"),
    "consolidation of data":         ("データの統合 / データ集約",                            "名詞句", "プロセス","data / analysis / synthesis",                                  "×"),
    "prescriptive formula":          ("規定的な方法論 / 処方箋的なアプローチ",                "名詞句", "概念",    "approach / process / methodology",                            "○"),
    "relevant new information":      ("関連する新情報",                                         "名詞句", "データ",  "information / finding / context",                             "×"),
    "new investigation process":     ("新しい調査プロセス",                                    "名詞句", "プロセス","investigation process / approach / workflow",                  "×"),
    "strong incident analysis":      ("徹底的なインシデント分析",                              "名詞句", "プロセス","incident analysis / deep dive / thorough",                     "×"),
    "level of analysis":             ("分析のレベル / 分析の深度",                            "名詞句", "概念",    "analysis / depth / investigation",                            "×"),
    "potential action item":         ("潜在的なアクションアイテム",                          "名詞句", "行動",    "action item / finding / improvement",                         "×"),
}


def main():
    input_path = "raw_phrase_frequency.csv"
    output_path = "phrases.csv"

    with open(input_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows_in = list(reader)

    output_rows = []
    missing: list[str] = []

    for row in rows_in:
        lemma = row["lemma"]
        locations = row["locations"]
        count = int(row["count"])

        if lemma in TRANSLATIONS:
            jp, pos, category, related, in_dict = TRANSLATIONS[lemma]
        else:
            jp = ""
            pos = row["pos_pattern"] or "名詞句"
            category = ""
            related = ""
            in_dict = "×"
            missing.append(lemma)

        output_rows.append({
            "英語名":   lemma,
            "日本語訳": jp,
            "品詞":     pos,
            "対象分類": category,
            "関連語":   related,
            "独自辞書": in_dict,
            "場所":     locations,
            "出現数":   count,
        })

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["英語名", "日本語訳", "品詞", "対象分類", "関連語", "独自辞書", "場所", "出現数"],
        )
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"出力: {output_path}")
    print(f"総熟語数: {len(output_rows)}")
    if missing:
        print(f"\n未翻訳熟語 ({len(missing)} 語) — build_phrases.py の TRANSLATIONS に追加してください:")
        for w in missing:
            print(f"  {w}")
    else:
        print("未翻訳熟語: なし")


if __name__ == "__main__":
    main()
