/**
 * no-ai-emoji-markers
 *
 * ✅/❌ などの「判定マーカー絵文字」を検出する。
 * AI生成文は良い例/悪い例・正解/不正解の対比にこれらを多用する傾向がある。
 *
 * options:
 *   markers: 検出する絵文字の配列（既定値あり）
 */

const DEFAULT_MARKERS = ["✅", "❌", "⭕", "✗", "☑", "☒", "🔴", "🟢", "🟡"];

const reporter = (context, options = {}) => {
  const markers = options.markers ?? DEFAULT_MARKERS;
  const pattern = new RegExp(`[${markers.join("")}]`, "gu");

  const { Syntax, RuleError, report, getSource, locator } = context;

  return {
    [Syntax.Str](node) {
      const text = getSource(node);
      pattern.lastIndex = 0;
      let match;
      while ((match = pattern.exec(text)) !== null) {
        const padding = locator.range([match.index, match.index + match[0].length]);
        report(
          node,
          new RuleError(
            `マーカー絵文字「${match[0]}」を検出しました。良い例/悪い例の対比に絵文字を使うのはAI生成文の典型パターンです。テキストで明示するか、文体に合わせた表現に変えてください。`,
            { padding }
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
