/**
 * no-monotonous-sentence-endings
 *
 * 同一の文末表現（です/ます/でしょう など）が一定数連続している段落を検出する。
 * AI生成文に頻出する「平坦なリズム」をあぶり出すためのルール。
 *
 * options:
 *   threshold: 何文連続したら警告するか（既定: 4）
 *   endings:   検査する文末パターン（既定: です/ます/でしょう/ません/でした/ました）
 */
import { split, SentenceSplitterSyntax } from "sentence-splitter";

const DEFAULT_ENDINGS = [
  { name: "です", regex: /です[。．\.！？!?」』）)\s]*$/ },
  { name: "ます", regex: /ます[。．\.！？!?」』）)\s]*$/ },
  { name: "でしょう", regex: /でしょう[。．\.！？!?」』）)\s]*$/ },
  { name: "ません", regex: /ません[。．\.！？!?」』）)\s]*$/ },
  { name: "でした", regex: /でした[。．\.！？!?」』）)\s]*$/ },
  { name: "ました", regex: /ました[。．\.！？!?」』）)\s]*$/ },
];

function classifyEnding(sentence, endings) {
  for (const p of endings) {
    if (p.regex.test(sentence)) return p.name;
  }
  return null;
}

const reporter = (context, options = {}) => {
  const threshold = options.threshold ?? 4;
  const endings = options.endings ?? DEFAULT_ENDINGS;
  const { Syntax, RuleError, report, getSource } = context;

  return {
    [Syntax.Paragraph](node) {
      const text = getSource(node);
      const sentences = split(text)
        .filter((n) => n.type === SentenceSplitterSyntax.Sentence)
        .map((n) => ({
          raw: n.raw,
          ending: classifyEnding(n.raw, endings),
        }));

      if (sentences.length < threshold) return;

      let run = 1;
      let warned = false;

      for (let i = 1; i < sentences.length; i++) {
        const prev = sentences[i - 1];
        const cur = sentences[i];
        if (cur.ending && cur.ending === prev.ending) {
          run++;
          if (run >= threshold && !warned) {
            warned = true;
            report(
              node,
              new RuleError(
                `文末「〜${cur.ending}」が${run}文連続しています。リズムが単調になり、AIっぽさの典型パターンです。短文・体言止め・常体などを混ぜてリズムを崩してください。`
              )
            );
          }
        } else {
          run = 1;
        }
      }
    },
  };
};

export default {
  linter: reporter,
  fixer: reporter,
};
