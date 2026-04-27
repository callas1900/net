/**
 * no-excessive-list-usage
 *
 * 文書全体で箇条書きが過剰になっていないかを検出する。
 * AI生成文では「短い説明や情緒的な内容まで箇条書きにする」傾向がある。
 *
 * 2種類のチェックを行う:
 *   1. 文書全体の List 比率（List ノード数 / (List + Paragraph) ノード数）が高すぎる
 *   2. 各 List の項目が短すぎる（リスト化する必要がない内容を箇条書きにしている）
 *
 * options:
 *   maxListRatio:       List比率の上限（既定: 0.5 = 半分以上が箇条書きならNG）
 *   minDocumentNodes:   この数未満の小さな文書は比率チェックをスキップ（既定: 6）
 *   minItemLength:      リスト1項目の最小文字数（既定: 15）
 *   minItemsForCheck:   この項目数以上のリストだけ「短すぎる」をチェック（既定: 3）
 */

const reporter = (context, options = {}) => {
  const maxListRatio = options.maxListRatio ?? 0.5;
  const minDocumentNodes = options.minDocumentNodes ?? 6;
  const minItemLength = options.minItemLength ?? 15;
  const minItemsForCheck = options.minItemsForCheck ?? 3;

  const { Syntax, RuleError, report, getSource } = context;

  return {
    [Syntax.Document](node) {
      // ドキュメント直下の List / Paragraph の比率を見る
      const topLevel = node.children ?? [];
      const lists = topLevel.filter((n) => n.type === Syntax.List);
      const paragraphs = topLevel.filter((n) => n.type === Syntax.Paragraph);
      const total = lists.length + paragraphs.length;

      if (total >= minDocumentNodes && total > 0) {
        const ratio = lists.length / total;
        if (ratio >= maxListRatio) {
          report(
            node,
            new RuleError(
              `文書全体に占める箇条書きの比率が${(ratio * 100).toFixed(0)}%です（${lists.length}/${total}）。AI生成文の典型である「箇条書き乱用」の可能性があります。文章として書き直すことを検討してください。`
            )
          );
        }
      }
    },

    [Syntax.List](node) {
      const items = (node.children ?? []).filter(
        (c) => c.type === Syntax.ListItem
      );
      if (items.length < minItemsForCheck) return;

      const itemTexts = items.map((item) => {
        const t = getSource(item).replace(/^[-*+\s\d.]+/, "").trim();
        return t;
      });

      const shortItems = itemTexts.filter((t) => t.length < minItemLength);
      if (shortItems.length === items.length) {
        report(
          node,
          new RuleError(
            `この箇条書きは全${items.length}項目すべてが${minItemLength}文字未満です。短い項目だけのリストは情報密度が低く、AIっぽさが強く出ます。文章にまとめるか、項目を充実させてください。`
          )
        );
      }
    },
  };
};

export default {
  linter: reporter,
  fixer: reporter,
};
