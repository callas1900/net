/**
 * no-ai-structural-preamble
 *
 * 文書冒頭・セクション冒頭に置かれる「構造宣言型の前置き」を検出する。
 * 例:
 *   - 「本記事では〜について解説します」
 *   - 「以下では〜を見ていきます」
 *   - 「結論から言うと、〜」
 *   - 「本記事の構成は以下の通り。」
 *
 * prh で個別フレーズを検出するのと違い、このルールは
 * 「冒頭位置にある場合のみ警告する」「前置きが連発されていないか見る」
 * というAST位置依存の判定を行う。
 *
 * options:
 *   patterns:       セクション先頭段落のみを対象とするパターン（正規表現の配列、既定値あり）
 *   globalPatterns: 位置に関わらず全段落を対象とするパターン（正規表現の配列、既定値あり）
 *   checkSectionHeads: セクション冒頭もチェックするか（既定: true）
 */

const DEFAULT_PATTERNS = [
  /^結論から(言|い)うと/,
  /^結論から(申|もう)し上げると/,
  /^本記事では/,
  /^本稿では/,
  /^この記事では/,
  /^以下(で|では)(は|、)?[^。]{0,40}(解説|説明|紹介|見て)/,
  /^これから[^。]{0,30}(解説|説明|紹介)/,
  /^まずは[^。]{0,30}(から|について)[^。]{0,30}(見て|解説|説明)/,
  /いかがでしたでしょうか/,
  /いかがでしたか[。\?？]/,
  /(について|を)(整理|概説|概観|解説|紹介|説明)する[。]?$/,
  /を(示す|まとめる|述べる)[。]/,
];

// 位置に関わらず全段落をチェックするパターン
// 記事の構成・目次を宣言する孤立短文など、本文中のどこに現れても問題となるもの
const DEFAULT_GLOBAL_PATTERNS = [
  /^(本記事|本稿|この記事|記事)(の構成|の流れ|の目次)は以下/,
  // 「〜は以下の通り。」形式（です/だ なしで箇条書きを誘導する孤立短文）
  /は以下の通り[。]$/,
];

const reporter = (context, options = {}) => {
  const patterns = options.patterns
    ? options.patterns.map((p) => (p instanceof RegExp ? p : new RegExp(p)))
    : DEFAULT_PATTERNS;
  const globalPatterns = options.globalPatterns
    ? options.globalPatterns.map((p) => (p instanceof RegExp ? p : new RegExp(p)))
    : DEFAULT_GLOBAL_PATTERNS;
  const checkSectionHeads = options.checkSectionHeads ?? true;

  const { Syntax, RuleError, report, getSource, locator } = context;

  // ドキュメント直下の段落のうち、「セクション先頭の段落」を判定する
  // = 直前が Header または存在しない場合
  function isSectionLeadingParagraph(paragraph, parent) {
    if (!parent || !parent.children) return false;
    const idx = parent.children.indexOf(paragraph);
    if (idx === -1) return false;
    if (idx === 0) return true;
    const prev = parent.children[idx - 1];
    return prev && prev.type === Syntax.Header;
  }

  function reportMatch(node, match, message) {
    const offset = match.index ?? 0;
    const padding = locator.range([offset, offset + match[0].length]);
    report(node, new RuleError(message, { padding }));
  }

  function checkParagraph(node, parent) {
    const text = getSource(node).trim();

    // 位置不問パターンを先にチェック
    for (const pattern of globalPatterns) {
      const match = text.match(pattern);
      if (match) {
        reportMatch(
          node,
          match,
          `構造宣言「${match[0]}」を検出しました。AI生成文の典型パターンです。直接本論から書き始めることを検討してください。`
        );
        return;
      }
    }

    // セクション先頭限定パターン
    if (!checkSectionHeads && parent) {
      const idx = parent.children.indexOf(node);
      if (idx !== 0) return;
    } else if (parent && !isSectionLeadingParagraph(node, parent)) {
      return;
    }

    for (const pattern of patterns) {
      const match = text.match(pattern);
      if (match) {
        reportMatch(
          node,
          match,
          `セクション冒頭の構造宣言「${match[0]}」を検出しました。AI生成文の典型パターンです。直接本論から書き始めることを検討してください。`
        );
        break; // 1段落につき1警告
      }
    }
  }

  return {
    [Syntax.Document](node) {
      const children = node.children ?? [];
      for (const child of children) {
        if (child.type === Syntax.Paragraph) {
          checkParagraph(child, node);
        }
      }
    },
  };
};

export default {
  linter: reporter,
  fixer: reporter,
};
