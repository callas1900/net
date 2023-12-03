---
title: '[DynamicsAX2009]AXのTableとDBを復旧させるための6つの事'
date: 2010-03-08T00:23:00.000+09:00
draft: false
tags : [DynamicsAX2009]
---

DynamicsAXで開発をしていたり、  

AOTからDBをいじりまくってたりするとよくTable周りでエラーが出る。  

その場合にやるべき6つのことを書いておく。

  

1.  [DynamicsAXにログインしている人たちを全員ログアウトさせる。](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#DynamicsAX__9086810667067766)
2.  [Compile](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#Compile_24089203216135502)
3.  [Synchronize](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#Synchronize_9854677263647318)
4.  [Index再作成](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#Index__9263471895828843)
5.  [クライアントキャッシュファイル削除](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#_3336683753877878)
6.  [Usage Data削除](http://www.blogger.com/post-edit.g?blogID=20219551&postID=6787775841824196995#Usage_Data_)

  

#### DynamicsAXにログインしている人たちを全員ログアウトさせる。

これからやる作業は、やっている間にAXが操作されないほうがよいのでログアウトしてもらう。

  

#### Compile

AOTのルートで右クリックコンテキストメニューを出し、**Compile **を実行する。

ここでエラーが出たものは基本的に修正したほうがよいが、X++はインタプリタ言語なので現在エラーが出ている箇所以外のものは放置してもよい。

  

#### Synchronize

Data Dictionaryで右クリックコンテキストメニューを出し、**Synchronize** を実行する。

これでAXとDBとの同期化される。

  
Compile & Synchronize である程度のDBとのアンマッチ等のErrorやWaringは除去される。  

あなたがインフラ担当ならば、昼休みと帰る前にこの二点はやっておいて損はない。

  

#### Index再作成

1.  AOSサービス停止  
      
    
2.  **Axapd.aoi** ファイルを削除する。  
    (Axapd.aoiはデフォルトで C:\\Program Files\\Microsoft Dynamics AX\\50\\Application\\Appl\\DynamicsAx1 にある。)  
      
    
3.  AOSサービス再開（もしくはWindows再起動）

  
これで大抵のものは治るはず。  
特にDBとAXのDataDictionaryのアンマッチ系はこれでほとんど治る。  
それでも駄目なら・・・  
  

#### クライアントキャッシュファイル削除

1.  AXクライアントを終了  
      
    
2.  クライアントキャッシュファイル(.auc)を削除  
      
    
    WindowsXPの場合:
    
    C:\\Documents and Setting\\<USER>\\Local Settings\\Application Data
    
    Windows2008の場合:
    
    C:\\Users\\<USER>\\AppData\\Local
    
      
    

#### Usage Data削除

1.  AXクライアントを起動  
      
    
2.  Tool > Options を起動  
      
    
3.  Usage dataを押す  
      
    
4.  General をタブで Reset を押す