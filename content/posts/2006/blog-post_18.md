---
title: '現在、ソースコードの修正中。'
date: 2006-10-18T13:40:00.000+09:00
draft: false
tags : [WorkLog]
---

現在、ソースコードの修正中。

ソースを修正し、ローカルサーバーにデプロイするのだけど、

一回ちょこっと直してから再度テストするためには

約３分～５分の時間を要する。

その間できる事は少ない。

サーバーへのデプロイ作業でPCのメモリがほぼ食い尽くされるからだ。

JSPのコメントアウト作業ですら時間がかかる。

何故WASはwarファイルなんぞでJSPをまとめようとするのか････

で

**暇な時間が出来る。**

故に、

私は軽めのテキストエディタで適当な事を書き遊んでいるのです。

さて

**有限要素法的な思考方法**が必要な時がある。

大学で習ったのだが、この思考方法は非常に数学的だと私は思っている。

これは端的に言えば、一種の分析方法である。

何か一つの事象を分析したい場合。

行き詰る事がある。

そういう場合は大抵、その事象の振る舞いが複雑に見えるからである。

なので、分割してしまえという単純明快な方法。

今まさにその最中です。

バグるのはわかるがどう見てもどのロジックも問題なし。

当然バグってるのだから問題があるわけで・・・

そういう時はある程度悩んでわからなかったら、

**全部コメントアウチ！**

そして動いたら（動かなかったらソースレベルのバグじゃなく環境の問題）

**半分ぐらいのソースを**

**コメントアウト！**

あ、ちなみにこのソースはJSPなのでこういう思い切ったことができやすいのです。

じゃ、呼び出してるアクションだけ切ればいいんじゃ？って思うだろうが・・・

今回のソースは**JSPに直接ロジックが書いてある**んだよおおおおUZEEEEE

で、また動いたら半分の半分を・・・・って具合にコアな部分を見つけ出す戦法。

さて・・・そうやって出た今回の結論・・・

ソースでもない・・・フレームワークでもない・・・おまえか・・・**WAS**なのか・・・

IBMｺﾛｽｿﾞ