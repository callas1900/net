---
title: '[Flash]FAMEでFlashのバージョン取得'
date: 2007-03-15T18:33:00.001+09:00
draft: false
tags : [Flash]
---

会社で作ったFlashがFlash7で動かないとのこと、  
そりゃそうだ、Flash8で作ってるんだから。  
  
会社曰く、現在インスコされているFlashPlayerの初期は7だからそれに合わせろ。  
  
ふーん・・・7がデフォでインスコされているとは知らなかった。  
  
で、パブリッシュの書き出しで7にすれば対応できますよっとメールを送ったところ。  
  
対応できたが、一部ドロップシャドウが消失  
  
ナンデスト？  
どうやらドロップシャドウではなくシャドウ部位に使用していたグラデがFlash7だと存在しないようだ。  
（それぐらい事前に調べとけってか？ハイ、その通りですスイマセン）  
  
で、出来上がったものを見たが、  
やはりグラデが全部消えてるとちょっと嫌な感じだ。  
  
う～ん・・・そういや昔javaScriptにhttpヘッダの中読んで  
ブラウザのバージョンをGETする方法とかを見た気がする。  
  
ActionScriptで、FlashPlayerのバージョンをGETできないものだろうか？ さらにそのバージョン毎に違うswfファイルを見せること出来ないか？  
つまりFlashPlayer8以上を使用している人には8以上のバブリッシュ設定のものを  
7を使用している人には7用のswfをそれぞれ提供できないか？  
（今回最低バージョンは7としている、理由はActionScript2.0が提供されるのは7以降なので）  
  
調べた結果  
System.capabilities.version;  
  
を使用すれば望みのものを得ることが出来るようだ。  
  
以下実際のコードを書いてみる。  
(FAME環境で作ったため、Macromediaと違うところがあります）  
  

### versionManager.as

> class versionManager {  
> function versionManager (path){  
> trace(Flashout.DEBUG + "trace()");  
>   
> // \_rootのDepth=1にMovieClipのインスタンスseedを作成  
> path.createEmptyMovieClip("seed",1);  
>   
> //インスタンスseedをmcとする  
> var mc :MovieClip = path.seed;  
>   
> //バージョン情報を取得  
> var ver :String= System.capabilities.version;  
> var major\_ver = ver.split(" ")\[1\].split(",")\[0\];  
> trace ("ver = " + ver);  
> trace ("major\_ver = " + major\_ver);  
>   
> //今回パブリッシュ設定を７と８で分けたいので  
> if (major\_ver > 7) {  
> //バージョン８以上対応のswf読み込み  
> mc.loadMovie("swf/8.swf");  
> } else {  
> //バージョン７対応のswf読み込み  
> mc.loadMovie("swf/7.swf");  
> }  
> }  
>   
>   
> static function main () :Void {  
> var base :versionManager = new versionManager(\_root);  
> }  
> }  

  
これをコンパイルすればＯＫ  
注意点）  

*   コンパイルする時Flash7で書き出さないと本末転倒。
*   swfファイルから相対バスでFlashPlayerを指定しています。

  
気になった掲示板投稿  
  
[新人が育たない… (GAC)](http://www.gac.jp/article/index.php?stats=question&category=14&id=16284&command=msg "新人が育たない… (GAC)")  
GACというBBSコミュニティに投稿されていたものなのですが、  
昨今のデザイナー、プログラマー事情を知るにはよい投稿です。