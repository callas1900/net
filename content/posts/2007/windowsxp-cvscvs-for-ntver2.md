---
title: '[Tool]CVS for NT 2.5.03インストールメモ'
date: 2007-12-05T20:32:00.001+09:00
draft: false
tags : [Tool]
---

**インストール環境**  
サーバーサイド・クライアントサイド共に　WindowsXP  
CVSには「CVS for NT」を仕様（Verは2.5.03）  
  
  

1.  下記にてDL（右端にある）  
    [CVS  
      
    ](http://www.march-hare.com/cvspro/prods.asp?lang=JP "CVS")
2.  実行後ウィザード内で  
    【Select Components】の画面で【Server Components】にチェックを入れる  
    他はデフォルトインストール  
    （考えるの面倒だったらFullインストールすればOK)  
      
    
3.  環境変数「Path」にCVS for NT のインストールディレクトリが追加されていることを確認  
      
    
4.  コントロールパネルの中に「CVS NT Server」なるものが出来上がっているので、  
    それをダブルクリック。  
      
    
5.  【Repository Configuration】なるタブがあるのでそれを選択。  
    【ADD】ボタンから新規作成  
    
    *   Location　：　CVS管理したいフォルダをインストール
    *   Name　：　上記が入れば勝手にデフォルトが入力されるのでそれを採用
    *   Description　：　適当
    
      
    
6.  「適用」を押すと、initialize するか聞いてくるのでOK  
    この作業が終わると、Location先のフォルダに「CVSROOT」というフォルダが出来る。  
      
    
7.  コマンドプロンプトを起動してパスワードを設定。  
    
    >   
    > 
    > C:\\適当なディレクトリ>cvs -d c:\\hogehoge\\hoge passwd -r Administrator -a user01  
    > Adding user user01  
    > New Password: \[作成するユーザ(user01)のパスワードを入力\]  
    > Verify Password: \[作成するユーザ(user01)のパスワードを入力\]  
    >   
    >   
    > \[オプション説明\]  
    > \-d ： リポジトリルート  
    > \-r ： Administrator権限を持っているWindowsUser名  
    > \-a ： 作成するCVSのUser名  
    >   
    > 
    >   
    > c  
    >   
    > ※社内開発とかでイントラネットなどでやる場合はパスなんてなくても困らないです。  
    >   
    
8.  以上で終わり、後はEclipseから接続するなりなんなりと

  
**参考サイト**  
  

*   [＠IT：連載：快適なXPドライビングのすすめ 第2回](http://www.atmarkit.co.jp/im/carc/serial/xpd02/xpd02.html "＠IT：連載：快適なXPドライビングのすすめ 第2回")

[](http://www.atmarkit.co.jp/im/carc/serial/xpd02/xpd02.html "＠IT：連載：快適なXPドライビングのすすめ 第2回")*   ```
    [＠IT：連載：快適なXPドライビングのすすめ 第3回](http://www.atmarkit.co.jp/im/carc/serial/xpd03/xpd03.html "＠IT：連載：快適なXPドライビングのすすめ 第3回") 
    ```
*   ```
    [CVS(CVSNT)のリポジトリ設定](http://www.develop-memo.com/server/cvs/cvsrepository.html "CVS(CVSNT)のリポジトリ設定")  
    
    ```