/**
 * no-uniform-paragraph-length
 *
 * 段落の長さが過度に均一な場合に警告する。
 * AI生成文は段落の文字数が揃いやすく、「金太郎飴」感の原因になる。
 *
 * 標準偏差 / 平均（変動係数）を見て、ばらつきが小さすぎる場合に警告。
 *
 * options:
 *   minParagraphs: 検査対象とする最小段落数（既定: 5）
 *   minLength:     この文字数未満の段落は対象外（既定: 30）
 *   maxCV:         変動係数の下限（これ未満で警告。既定: 0.25）
 */

const reporter = (context, options = {}) => {
  const minParagraphs = options.minParagraphs ?? 5;
  const minLength = options.minLength ?? 30;
  const maxCV = options.maxCV ?? 0.25;

  const { Syntax, RuleError, report, getSource } = context;

  return {
    [Syntax.Document](node) {
      const paragraphs = (node.children ?? [])
        .filter((n) => n.type === Syntax.Paragraph)
        .map((n) => ({ node: n, length: getSource(n).length }))
        .filter((p) => p.length >= minLength);

      if (paragraphs.length < minParagraphs) return;

      const lengths = paragraphs.map((p) => p.length);
      const mean = lengths.reduce((a, b) => a + b, 0) / lengths.length;
      const variance =
        lengths.reduce((acc, n) => acc + (n - mean) ** 2, 0) / lengths.length;
      const stdDev = Math.sqrt(variance);
      const cv = mean > 0 ? stdDev / mean : 0;

      if (cv < maxCV) {
        report(
          node,
          new RuleError(
            `段落の長さが均一すぎます（変動係数 ${cv.toFixed(2)} < ${maxCV}、平均 ${mean.toFixed(0)}文字）。AI生成文は段落の長さが揃う傾向があります。短い段落と長い段落を意図的に混ぜてリズムを作ってください。`
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
