---
title: 'Mountain LionでOpenGrok メモ'
date: 2013-10-30T17:41:00.001+09:00
draft: false
tags : [OpenGrok, Mac, ANT, tomcat]
---

このページを参考にしてOpenGrokをセットアップしてたけど何点か詰まったので備忘録として。  
  
参考ページ：[Mac OS X に OpenGrok で、今日からコードリーディング](http://qiita.com/flatbird/items/a7ad36a8d3040c9f30e1)  
こちらの状況：java, antはセットアップ済み  
  

#### 1\. OpenGrokのビルドでJFlex.jarを読み込んでくれない

確証はないが、linuxで  
[Bug#388371: jflex: JFlexTask cannot be found](http://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg238944.html)  
と報告されているので、antのlibパスにJFlex.jarを置き直したら動いた。  
  

#### 2\. tomcatが起動しない。

単純にCATALINA\_HOMEを足すだけ、  
手順にないのでOpenGrokがうまいことやってくれるのか？と期待したがそんなことはなかった。  
  
以上、自分用備忘録でした。