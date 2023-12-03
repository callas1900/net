+++
title = "在宅向けにコンデンサーマイクを探してみた話"
date = "2020-07-25"
author = ""
cover = ""
tags = ["WFH", "microphone"]
keywords = ["", ""]
description = "マイクのことを何も知らないところから、オンライン会議向けに単一指向性コンデンサーマイクを勉強して検討する。"
showFullContent = false
draft = false
+++

在宅でオンラインの仕事が増えてから、色々と机周りの機材が増えている。
時折、ヘッドセットやラップトップの備え付けのマイクじゃないマイク単体を使っている人を見かけるが、あまりそこまで気にしていなかった。

ある日、オンラインの勉強会でコンデンサーマイクを使ったほうが良いんじゃないかという意見を聞いた。いやいや要らないでしょう。会ったほうがいいかもしれないけど、必須じゃないのでは？と言ったところ。マイクの単一指向性の話を聞いて興味が出てしまった。確かにオンラインでやっている時、他の家族が家にいて彼らもオンラインで何らかの活動をしたり話し声を出したりしている。その声が入るのは確かにあまり気持ちの良いものではない。単一指向性によってそれらの音を除外出来るのであるばそれは良いのかもしれない。

# 要件を考える

## 欲しい機能

* usb 接続&バスパワー起動
* 単一指向性
* 自立スタンド

## あると嬉しい機能

* 指向性切り替え。単一・双方向・無指向の切り替え
* 高音質
* ミュート機能

# マイクに関して勉強
## 単一指向性の種類

単一指向性にはさらにタイプが存在することがわかった。
それらの中で有名なものを列挙し比較する。

* Cardioid
* Super Cardioid
* Hyper Cardioid
* Unidirectional

| name | Diagram | Comment |
| -------- | -------- | ----- |
| Cardioid     | ![](https://blog.discmakers.com/wp-content/uploads/2012/07/03P_Cardioid.jpg)  | 普通 |
|Super-Cardioid|![](https://blog.discmakers.com/wp-content/uploads/2012/07/05P_SuperCardioid.jpg)| Cardioid より若干指向性が強まってるが、後方からの音も取ってしまう |
| Hyper Cardioid |![](https://blog.discmakers.com/wp-content/uploads/2012/07/04P_HyperCardioid.jpg)| Super より傾向が進んでいる |
|Unidirectional|![](https://blog.discmakers.com/wp-content/uploads/2012/07/06P_Unidirectional.jpg)| Hyperより指向性が高まっている。Ultra-Cardioidともいう |

see also : https://blog.discmakers.com/2012/07/microphone-pickup-or-polar-patterns/

目的が単一指向性による環境ノイズの除去なので、可能であれば指向性が高いほうが良いのでUnidirectionalが最強となるが、何個か手頃な価格の製品を見たところRazerがSuper-Cardioidを出しているぐらいで、ほとんどCardioidだったので、気にしないことにする。

## 周波数特性

マイクの性能を見比べているとこの周波数特性が表示さているが。これは何か？
数字が大きいと良いのか？
[SHURE ブログ::マイクロホン 周波数特性表の見方](https://www.shure.com/ja-JP/performance-production/louder/how-to-read-a-microphone-frequency-response-chart)

https://music.a-miya.jp/koe-hz/#i-2 によると

【男声】
* バス 87～294Hz
* バリトン 98～392Hz
* テノール 131～440Hz

【女声】
* アルト 175～784Hz
* メゾ・ソプラノ 220～880Hz
* ソプラノ 262～1047Hz

となっているので 87Hz-1047Hz拾えれば十分すぎる。大体のマイクがこの声域を拾えるようになっている。のであまり気にしないでも良いかもしれない。

# 候補のマイクをリストアップ

以下の方法で表を作成

1. amazon, yodobashi, bigcamera を適当にまわる。
1. [17 Best Cardioid Condenser Microphones – For Vlogs, YouTube, & More](https://microphonebasics.com/best-cardioid-condenser-microphone/#best6) を読む
1. おすすめリンク等周遊

| name | unidirectivity | price| mute switch | Frequency Response|
| -------- | -------- | -------: | -------- | ------- |
| [Audio-technica AT2020USB+](https://www.amazon.co.jp/audio-technica-%E3%82%AA%E3%83%BC%E3%83%87%E3%82%A3%E3%82%AA%E3%83%86%E3%82%AF%E3%83%8B%E3%82%AB-USB-%E3%83%9E%E3%82%A4%E3%82%AF%E3%83%AD%E3%83%9B%E3%83%B3-AT2020USB/dp/B00Q3K32I8/ref=psdc_2130076051_t2_B000Y0FBY6) | Cardioid | ¥17,368 | - | 20Hz–20kHz |
| [Razer Seiren X](https://www.yodobashi.com/product/100000001003771691/) | Super-Cardioid  | ￥12,320 | 〇 | |
| [888M マランツプロ USBコンデンサーマイク MPM2000U](https://www.amazon.co.jp/dp/B01GJ9IUNY/ref=vp_d_pb_TIER2_cml_lp_B084K53F5Z_pd?_encoding=UTF8&pd_rd_i=B01GJ9IUNY&pd_rd_w=LweXd&pf_rd_p=36dea1d5-dd4a-4c9f-baca-d2c0b0542db8&pf_rd_r=f4314235-bc89-4c0e-8432-fb23408e1f19&pd_rd_r=f4314235-bc89-4c0e-8432-fb23408e1f19&pd_rd_wg=Y7Z1n) |  Cardioid | ¥9,656 | - | 20Hz-18kHz |
| [Blue Microphones Snowball iCE USB](https://www.amazon.co.jp/gp/product/B0822PPCMG/ref=as_li_tl?ie=UTF8&tag=akigametv0e-22&camp=247&creative=1211&linkCode=as2&creativeASIN=B0822PPCMG&linkId=95733dbc0885ab03dea8d0012dd42ece) | Cardioid | ¥7,399 | - | 40Hz-18KHz | 
| [HyperX QuadCast](https://www.amazon.co.jp/%E3%82%AD%E3%83%B3%E3%82%B0%E3%82%B9%E3%83%88%E3%83%B3-HyperX-QuadCast%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89%E3%82%A2%E3%83%AD%E3%83%B3%E3%83%9E%E3%82%A4%E3%82%AF-%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%82%AF%E3%83%AA%E3%82%A8%E3%83%BC%E3%82%BF%E3%83%BC-HX-MICQC-BK/dp/B07NZZZ746/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=HyperX+QuadCast&qid=1595530484&sr=8-5) |Cardioid / Omnidirectional / Strereo / Bidirectional|	¥16,667| 〇 | 20Hz–20kHz | 
| [Blue Microphones Yeti USB](https://www.amazon.co.jp/Blue-Microphones-Midnight-BM400MB-2%E5%B9%B4%E9%96%93%E3%83%A1%E3%83%BC%E3%82%AB%E3%83%BC%E4%BF%9D%E8%A8%BC/dp/B0822PZGDJ/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=blue%2Byeti&qid=1595668529&s=computers&sr=1-3&th=1) | Cardioid / Omnidirectional / Strereo / Bidirectional | ¥17,100| 〇 | 20Hz–20kHz |
| [Blue Microphones Yeti Nano USB](https://www.amazon.co.jp/Blue-Microphones-%E3%82%B3%E3%83%B3%E3%83%87%E3%83%B3%E3%82%B5%E3%83%BC-BM300SG-2%E5%B9%B4%E9%96%93%E3%83%A1%E3%83%BC%E3%82%AB%E3%83%BC%E4%BF%9D%E8%A8%BC/dp/B0822NRR6M/ref=sr_1_4?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=blue+yeti&qid=1595668529&s=computers&sr=1-4) | Cardioid / Omnidirectional | ¥14,100 | 〇 |  20Hz–20kHz |
| [FIFINE USBマイク コンデンサーマイク K670](https://www.amazon.co.jp/FIFINE-%E3%82%B3%E3%83%B3%E3%83%87%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%9E%E3%82%A4%E3%82%AF-%E3%83%9E%E3%82%A4%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%89%E9%AB%98%E3%81%95%E8%AA%BF%E7%AF%80%E5%8F%AF-%E3%82%A4%E3%83%A4%E3%83%9B%E3%83%B3%E3%82%B8%E3%83%A3%E3%83%83%E3%82%AF%E4%BB%98%E3%81%8D-K670/dp/B079HRX2ZP/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=FIFINE+USB%E3%83%9E%E3%82%A4%E3%82%AF+%E3%82%B3%E3%83%B3%E3%83%87%E3%83%B3%E3%82%B5%E3%83%BC%E3%83%9E%E3%82%A4%E3%82%AF+K670&qid=1595664306&s=musical-instruments&smid=A2ZDHB8YQ324B9&sr=1-1) | Cardioid | ¥6,699 | - | 50Hz-15KHz|

# 結局

最初はRazer Seiren Xがいいなと思ってたけど、音質に関してネガティブな評価が散見されてたので躊躇。
マランツ MPM2000UかBlue Snowballあたりが値段的にも良い気がしてくるが、ミュートスイッチってあると便利だよなって思う瞬間が何度かあったのでそれは欲しい。そう考えると機能的にはHyperX QuadCastがいいんだけど、ちょっと値段が高い。

そんな疑問を抱きながらyoutubeを検索してたら以下の動画を発見。

{{< youtube T1g4XOp6LgM>}}

やはり、HyperX QuadCast のタップミュートはすごく良いなぁ。正直どのマイクもそこまで大きな差を感じなかったのですが、ちょっと気になったのはBlue YetiとYeti Nano。この２つは値段がそこそこで、ミュートボタンがついている。後、ちょっとRazerの時にもやっとしていたのが、マイクメーカーじゃないところのマイクを買うことへの軽い抵抗感。これは個人的な好みの問題。

{{< youtube Aw82ctVsQjs>}}

Yeti Nanoでも良さげ。ミュートはあるし。音質も良さそうだし。単一指向性と無指向を切り替えられるし。
ただし。良いカラーリングのものがYetiの無印の方にしかないのが気になるなぁ。


