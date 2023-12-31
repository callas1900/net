---
title: 'Oracle 10g Express Edition でチト困った'
date: 2007-12-06T11:22:00.000+09:00
draft: false
tags : [Oracle, WorkLog]
---

Oracle 10g Express Edition　は  
  

*   **AL32UTF8**
*   **WE8MSWIN1252**

  
のみのCHARACTER SETしか使用できない  
  

資料：  
**Oracle® Database Express Edition**  
[**10 Oracle Database XE Character and Language Configurations**](http://download-west.oracle.com/docs/cd/B25329_01/doc/install.102/b25143/toc.htm#BABJACJJ "10 Oracle Database XE Character and Language Configurations")  

  
  
これで非常に困った。  
  
現在数社で連携をとってＷｅｂアプリを開発しているのだけど、  
他社が作った機能の検証用テストデータとしてINSERT文が書かれたSQLファイルを送付してもらった。  
  
いざINSERTしてみると、  

ORA-12899:  
列"hoge"."foo"."bar"の値が大きすぎます  
(実際: 60、最大: 40)

  
とOracleに怒られ、データが入らない箇所がある。  
  
慌てて文字数をカウントしたが、データに間違いはない。  
  
これはなんだ？と思ったところで、  
思い当たったのが、DBモデルのバージョンが違うのではないか？ということ  
  
誤解を招く言い方かもしれないので補足を書くと、  
上記の違いとはDBのバージョンが違うという意味ではない、  
今回のプロジェクトでは（あってはならないことなんだけども）、  
客先要求の追加などで、テーブルの名前が変わったり、テーブル自体が消えてたりなどの数回のモデルチェンジが行われているのだ。  
  
そして何度かデータの最大文字数も変更されている。  
  
数社で連携をとって開発している中でのモデルチェンジだったので、  
もしかしたら各社でバージョンが違うのではないのか？  
そのバージョンでは文字数定義が違うのではないか？と思った。  
  
細かい敬意を省くために結果を述べると**「モデルのバージョンは同じ」**だった。  
  
原因は弊社と他社のDBの差にあったのだ。  
  
  
私の会社ではWindows版のOracle10gサーバーが見つからなかったので、  
他社検証用として急いでOracle10g Express Editionを導入した。  
  
無料で使える10gということでワクワクしながら環境構築していったのだが、  
構築過程でサービス名が一つしか設定できないことを知る。  
  
まぁこれは、今回プロジェクト限りで潰してもいいDBなので、問題はない。  
  
  
それから上記の問題の発生である。  
XEのインストールウィザードで文字コードの選択が出てこなかったので考えてなかったのだけど  
（浅薄だなぁ・・・）  
  
文字コードの差が問題だということが結果としてわかった。  
  
現在Oracle10g正式版は何種類かの文字コードをカバーしている。  
そしてデフォルトインストールすると、文字コードは**SHIFT\_JIS（JA16SJIS）**になるのだが、  
  
10gXEは**UTF8（AL32UTF8）**がデフォルトだ、  
[仕様書](http://download-west.oracle.com/docs/cd/B25329_01/doc/install.102/b25143/toc.htm#BABJACJJ "仕様書") を見ると、**WE8MSWIN1252**というコードも選択出来るそうなのだがこの文字コード自体初見である。  
  
じゃあ、何が困るのか？  
  
プログラマな人はとっくに原因なんて分かっていると思うけど、  
プログラマじゃない人も世の中にはいるわけで・・・説明を続けると、  
  
どうやら今回のプロジェクトにおいて10gを使用している所はすべて**SHIFT\_JIS**で設計されている。  
（日本国内のイントラネット的なＷｅｂシステムなのでこれはまぁ、いいんじゃないかな･･･怒る人もいるだろうけど）  
  
  
そうすると型**VARCHAR2**での日本語全角20文字MAX文字数の設計のは  
  

VARCHAR2 = 40\[Byte\]  

  
これは日本語の出力には**2byte分のデータ**が必要なので文字数２倍としただけである。  
  
  
さて、DBのCHARACTER SETが**UTF8**だった場合。  
日本語全角20文字は  

VARCHAR2 = 60\[byte\]  

  
となる。**UTF8**はマルチバイト文字であり、  
多言語をカバーするため1byte文字以外の出力に**2～6byte分のデータ**が必要になる。  
日本語の全角文字に必要なデータは**3byte**である。  
よって文字数３倍とした。  
  
さて、私は**10gXEと10g正式版の違いを意識せずに**提供されたCreateTable文を走らせた。  
  
  
条件は揃ったので、最初の問題に戻ろう。  
  
**SHIFT\_JIS**で設計されたテーブルデータを**UTF8**の**10gXE**にCreateし、  
全角20文字のDBのフィールド用に作られたテストデータをINSERT文で突っ込むと、  
  
DB側は設計上**VARChAR2（40byte）**という情報と、  
入力された**全角20文字のテストデータ**を見比べて  
  
**全角20文字を60byteデータと解釈**し、入力者側に  
  

ORA-12899:  
列"hoge"."foo"."bar"の値が大きすぎます  
(実際: 60、最大: 40)

  
  
というエラーを返す。  
  
  
結論　：　こっちが悪い。