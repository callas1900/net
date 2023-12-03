---
title: '[Flash]FAME環境でXML読み込み'
date: 2007-03-14T18:21:00.001+09:00
draft: false
tags : [Flash]
---

FAMEでActionScriptを書こうとすると色々と不便なことがある。  
（まだまだ開発されたての環境なので致し方ないが）  
  
さて先日ある案件でXMLデータを読みこんで処理したいといった内容があったのだが、  
  
いかんせん、MacromediaFalshのように簡易的に書くとコンパイルエラーで落ちてしまう。  
また、XMLでの検索は面度なのでActionScript用のJSONクラスを用意しても  
JSONクラスで落ちてしまう。  
  
結局手書きでやることにした。  
  
作業の流れとしては  
  

1.  XMLインスタンス作成
2.  インスタンス.ignoreWhite プロパティをtrueに設定。
3.  XMLインスタンのonLoadにファンクション設定。
4.  XMLインスタンスに外部XMLをload

  
XML.onLoad はLoadが実行され終了されて初めて動作するプロパティです。  
さて実際に以下に書いてみましょう。  
  

### XMLデータ内容

> <?xml version="1.0" encoding="UTF-8"?>  
> <node>  
> <campany>  
> <name>test1</name>  
> <url>http://xxxx.co.jp</url>  
> </campany>  
> <campany>  
> <name>test2</name>  
> <url>http://yyyy.co.jp</url>  
> </campany>  
> <campany>  
> <name>test3</name>  
> <url>http://zzzz.co.jp</url>  
> </campany>  
> <campany>  
> <name>test4</name>  
> <url>http://aaaa.co.jp</url>  
> </campany>  
> <!--ここより下には記入しないで下さい。-->  
> <end><!--このタグは消さないで下さい--></end>  
> </node>  

  

### ActionScript内容

> //XMLインスタンス作成  
> var my\_xml :XML = new XML();  
>   
> // 改行などを無視  
> my\_xml.ignoreWhite = true;  
>   
> //onLoadのイベントハンドラにfunctionを設定  
> my\_xml.onLoad =  
> function(success) {  
> if (success) {  
> my\_xml = this;  
> // XMLエレメントの取得  
> var my\_xmlnode :XMLNode = my\_xml.firstChild;  
>   
> var name :String = "";  
> var url :String = "";  
> var i :Number = 0;  
>   
> while ( my\_xmlnode.childNodes\[i\].hasChildNodes() ){  
> name = my\_xmlnode.childNodes\[i\].childNodes\[0\].childNodes;  
> url = my\_xmlnode.childNodes\[i\].childNodes\[1\].childNodes;  
> trace  ( name );  
> trace  ( url );  
> i++;  
> }  
> }  
> }  
>   
> //xmlファイルをロード（swfファイルからの相対パスであることに注意  
> my\_xml.load("data.xml");  

  
呼び出したデータを配列に入れるなりなんだなりすれば、使いまわしも出来る。  
ただ、そうなるとコードが長めになってしまうので、  
別関数もしくはクラスとして定義すればいいだろう。  
もっとCoolな書き方はあると思うが、  
とりあえず動いたのでメモ残し。  
  
諸注意  

*   <end>タグはhasChildNodes()でfalseを出させるために使用。
*   trace()はデバッグ領域に書き出す関数