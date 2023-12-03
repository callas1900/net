---
title: '[Flash]Laszloよ、納品後の暇な時間を返せ。'
date: 2007-11-07T21:10:00.001+09:00
draft: false
tags : [Flash]
---

昨日納品が一端終わって今日は暇だ。  
  
といっても納品先から何をいってくるかわからないので待機状態なんだけどね。  
  
ついでに言うと、明日からまた忙しくなる。  
  
そんなわけでプロジェクトの仕様書なぞを読みつつ。  
  
今年の初めにちょっと触ったFAME(Flashout＋ASDT＋MTASC＋Eclipse)  
でも再度触ってみようかと思いぐーぐるで検索する。  
  
最近またFlashに興味が出てきたのだ。  
  
FAMEは中々に面白い考え方だったので、  
FAMEに関するBlogの新規エントリーが増え  
FAMEコミュニティが活性化しているかと思いきや、  
  
あらら、全然エントリーがない、一番最近のエントリーでも2005年だよ  
  
どうやらFAMEははやらなかったようだ。  
（Swifmillとの組み合わせでFAMESとかいうものもあったのになぁ）  
  
じゃあ、EclipseでFlashを作成するような環境って今他のものはあるのだろうか？  
  
一番今はやっているものは何かないかなぁ？  
  
と  
  
またまたぐーぐるにて「Flash eclipse」で検索をかける。  
  
こんな記事を見つけた。  
[Ajax，Flash，Java---オープンソースで実現するリッチクライアント 第4回](http://itpro.nikkeibp.co.jp/article/COLUMN/20050920/221409/?P=1&ST=oss "Ajax，Flash，Java---オープンソースで実現するリッチクライアント 第4回")  
  
さらに、そこからこんなものを見つけた。  
  

### **Open Laszlo**

（オープン・ラズロと読むらしい）  
  
どうやらCPLライセンスのオープンソフトみたいだ。  
CPLライセンスとは・・・麻原○晃にドッペルゲンガーである。。。  
って書いたら信者から殺されそうなので、  
  
とりあえず、未来永劫無料、商用利用にあたっても  
ラズロのソースコードの公開だけでいいという素晴らしいライセンスてことでOK。  
  
さて、オープンソースであることは非常に気にいたのだけど  
（ついでに名前の響きも面白い）  
  
調べてみるとこんなものがった。  
  
  
[EclipseプラグインでOpenLaszlo IDEを構築する](http://www.atmarkit.co.jp/fwcr/rensai/laszlo_adv01/laszlo_adv01_1.html)  
  
まさに探していたものじゃーないか！  
  
早速Open Laszoloをインストールする。  
これは驚くほどさっくりといけた。  
→[Open Laszlo DL場所](http://www.openlaszlo.org/download "Open Laszlo DL場所")  
  
次にIDE4ECLIPSEをインストールしようと  
  
Open Laszlo用のEclipseプラグインを公開している  
alphaWorksのサイトにいってみる→[ここ](http://alphaworks.ibm.com/tech/ide4laszlo/ "ここ")  
  
ここにあると書いてたけど・・・？あれ？無い！おいてない！  
  
ってことでネットの海の中血眼になって探すと  
  
LaszloJapanのフォーラムに情報があった  
→[これ](http://laszlo.jp/modules/xhnewbb/viewtopic.php?topic_id=103 "これ")  
  
[IDE4LASZLOのDL場所](http://openlaszlo.org/download-old/ "IDE4LASZLOのDL場所")  
  
ふぅ、これでDLできる  
  
やっとこさIde4laszloをインストールできると思ったら。  
  
org.eclipse.emf.ecore.resource が無いとかいって怒られた。  
  
[emf.ecoreをダウンロードしてインストール](http://www.eclipse.org/modeling/emf/downloads/?project=emf "emf.ecoreをダウンロードしてインストール")  
  
さて次こそインストール！  
  

> 必須:フィーチャー"org.eclipse.emf.ocl(1.0.0)"、または互換。

  
とまた怒られた。  
  
要するに、emf.olcのバージョン1.0.0が足りてねーっていうことだ  
  
エラーワードでググってみると、あるブログに以下プラグインを全部インストールすると解決したとあったのでぶちこむ。  
  

*   [org.eclipse.emf.ocl](http://www.eclipse.org/modeling/mdt/downloads/?project=ocl "org.eclipse.emf.ocl")
*   [org.eclipse.emf.query](http://www.eclipse.org/modeling/emf/downloads/?project=query "org.eclipse.emf.query")
*   [org.eclipse.emf.validation](http://www.eclipse.org/modeling/emf/downloads/?project=validation "org.eclipse.emf.validation")
*   [org.eclipse.emf.transaction](http://www.eclipse.org/modeling/emf/downloads/?project=transaction "org.eclipse.emf.transaction")

  
  
さーインストールだ。  
おう・・・・  
  

> 現在の構成にはエラーがあり、この操作は予測できない結果を引き起こす可能性があります。  
> OCL 2.0 Binding for UML (1.1.1.v200707131415-1007w311818242526) 必須: プラグイン "org.eclipse.core.runtime (3.3.0)"、または互換。  
> Object Constraint Language (OCL) 2.0 (1.1.1.v200707131415-3209oA55P5N7F8JDH) 必須: プラグイン "org.eclipse.emf.ecore (2.3.0)"、または互換。  
> EMF Model Query OCL Integration (1.1.0.v200706071712-10-7w311817182823) 必須: プラグイン "org.eclipse.emf.ocl (1.1.0)"、または互換。  

  
えーっと何々？org.eclipse.core.runtime**(3.3.0)**？  
Eclipseを3.3にしろと言ってるのか？  
  
あ、いや違う、インストールしたOCLがどーもバージョンが新しすぎたらしい、1.1.1をインストールしてたが、  
Eclipse3.2だと1.0.0じゃないとダメみたいだなぁ、互換性ないのかよ。  
  
1.0へのリンクが上記URLにあったのでそれをインストール。  
前バージョンをアンインストール。  
Eclipse再起動！  
  
そろそろ動け！  
  
おｋ！動いた！  
  
てなことやってたらえらい時間食ったわけで・・・  
  
OpenLaszro面白うそうではあるが、IDE4ECLIPSEの場所が変わったことをネタにしているブログがほとんどないことから考えると、もしかしたらあまりはやってないのかもなぁ。  
ま、ボチボチ触ってみます。  
  
以下にインストールの時に助けてもらったサイト  
  
参考サイト  
**Openlaszlo.jp**  
[OpenLaszlo速攻インストール(Windows版/初心者向け)](http://www.openlaszlo.jp/staticpages/index.php?page=install "OpenLaszlo速攻インストール(Windows版/初心者向け)")  
  
**Web 技術サイト Okapi Project**  
[Eclipse + IDE for Laszlo のインストール](http://www.okapiproject.com/richclient/flash/openlaszlo_install.htm "Eclipse + IDE for Laszlo のインストール")