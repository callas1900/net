---
title: '[Eclipse][Flash]フリーなFLASH　FAME!'
date: 2007-02-23T19:15:00.002+09:00
draft: false
tags : [Flash, Eclipse]
---

フリーなFLASH　FAME!  
  
前の記事でFAMEというフリーのFlash開発環境を見つけたと書きました。  
FAMEの環境が整ったので、それについて書こうと思うます。  
  
  
そもそもFAMEとは何か。  
  
これはFlashout＋ASDT＋MTASC＋Eclipseの頭文字をとったものです。  
  

Flashout ：

ActionScript、ログ吐き

ASDT ：

ActionScript Development Tool

MTASC ：

ActionScriptのコンパイラ

Eclipse ：  

java系PGには欠かせないフリー開発環境ツール

  
  
Eclipseをコアとし、  
残り３つのツールを組み合わせることで  
フリーのFlash作成ツールFAMEとなります。  
  
実際の環境構築において参考にしたサイト  

*   [技術系のシバチョがコラムを書く](http://d.hatena.ne.jp/shibacho/20051009 "技術系のシバチョがコラムを書く - "Getting Started With MTASC for Flash Development"の日本語訳")
*   [神原日記 - FAMEを始める](http://d.hatena.ne.jp/kambara/20060323/1143128330 "神原日記 - FAMEを始める")

  
  
上記二記事を参考にやると、得に躓くことなく環境構築できました。  
  
  
FAMEを触ってみる  
実際動かしてみた感想として、  
javaやEclipseでの開発に慣れた人なら使いやすいが、  
今までMacromedia Flash で  
Flash作成してきた人は正直きついんじゃないか？と思います。  
（一部のActionScriptでガリガリ書いてる人は除く、そういう人にはむしろFAMEお勧め）  
  
ピュアActionScriptというのか・・・  
FAMEで全て作ろうとすると全部スクリプトでflashを作成しなければなりません。  
（これはこれで最軽量なFlashが作れるので魅力的なのですが・・・）  
図形描画など、かなり肩が凝る作業になってしまいます  
  
やはりグラフィカルな作業はMacromedia Flashのほうが楽楽です。  
FAMEは使えるか？  
物理モデルを映像化したり（惑星の動き、自由落下など）  
数式ありきな自然現象をFlashで表現したい場合は超お勧め。  
（後はフラクタルなども）  
  
それ以外としては、  
グラフィカルな編集をMacromedia Flashで  
ロジカルな編集をFAMEで、  
といったツールを使い分けるのもいいかも。  
  
そうなると今までの、  
デザイナーはscriptが苦手、 プログラマはグラフィックが苦手、 でも編集するのは同じflaファイル  
  
な状況から脱却し、  
それぞれをその道に特化した人が担当する事により  
素晴らしい作品が出来るかもしれません。  
  
  
蛇足？  
今回紹介したFAMEですが、  
これだけだとswfに画像を埋め込む事は出来ません。  
（外部読み込みで表示する事になる）  
  
swfに画像やFontを埋め込むには、  
[swfmill](http://swfmill.org/ "swfmill")  が必要です。（FAMESというらしい）  
  
swfmillはxml（swfmlとか言うらしい）  
からコンパイルするデータを取得しコンパイルするコンパイラです。  
  
あれ？どこかで聞いたようなツールだな。  
そうjavaやってる人なら欠かせないAntです。  
なので、さらにAntをかませる事によって。  
FAMES + Ant で完全なGUI環境を整えれるよーです。  
・・・ここまではまだ手が出ないな。