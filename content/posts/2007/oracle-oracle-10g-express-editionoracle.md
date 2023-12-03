---
title: 'Oracle 10g Express Editionのインストールメモ'
date: 2007-10-29T16:13:00.000+09:00
draft: false
tags : [Oracle, WorkLog]
---

Oracle備忘録  
仕事のテスト環境用に[Oracle 10g Express Edition](http://www.oracle.com/technology/products/database/xe/index.html)（Oracle 10gの無料版）を使用する機会があったのでそのインストールメモ  
  
Oracle : Oracle 10g Express Edition  
OS : WindowsXP  
  
とりあえずExeファイルを実行してインストール  
サクっと終了  
  
インストール中には**SYSTEM**のパスワードだけ設定。  
  
とりあえずSYSTEMでログイン  
後、新規ユーザー作成  
ここでは**FOO**としておく。  
  
これでとりあえずはスキーマ作成完了。  
  
次に他PCよりOracleに接続を試みる。  
  

1.  [まずはIPを固定](http://www.iodata.jp/support/advice/np-bbrm/ipkotei.htm "まずはIPを固定")
2.  ついでにOracle Clientをインストール
3.  次に  
    「すべてのプログラム」→「Oracle - OraClient10g\_home1」  
    →「コンフィグレーションおよび移行ツール」  
    →「Net Configuration Assistant」を選択  
    

  
後は以下のとおり  
  
ローカルネットワークサービス名構成を選択。  

![](http://docs.google.com/File?id=dhr8vrth_131hfrkxhdg)

  
追加を選択  

![](http://docs.google.com/File?id=dhr8vrth_132f7fqrbc6)

  
EXpressEditionはサービス名がデフォルトで定められており、  
複数設定することはできない様子。  
デフォルト名は「XE」  

![](http://docs.google.com/File?id=dhr8vrth_133dgk5gggr)

  
TCPを選択  

![](http://docs.google.com/File?id=dhr8vrth_134cqxxfzsh)

  
Oracle 10g Express EditionをインストールしたPCのローカルIPを入力  

![](http://docs.google.com/File?id=dhr8vrth_135cp2jwf9c)

  
後は接続設定をして開発者と猫の名前を除去して。  
自分が作ったスキーマ名とそのパスを入力してテスト成功すればOK!  
  
**注意点**  
Oracle DataBase を入れているPCのファイヤーウォールの1521ポートをあけておくこと