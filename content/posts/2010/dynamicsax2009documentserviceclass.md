---
title: '[DynamicsAX2009]DocumentServiceClassのアップデート'
date: 2010-03-19T02:33:00.000+09:00
draft: false
tags : [DynamicsAX2009]
---

AIFサービスのベースになっているテーブルの定義変更をした場合に  
DocumentServiceClassのアップデートを行わなければならない。  
  
  

### Query復元

AOTのQueryオブジェクト上で **Restore **を実行  
  

### Document Service の更新

#### Ax<Table>Class より parm Method と set Method を消去する

1.  Ax<Table> ClassをAOT上で表示し、フィールド一覧を展開し、表示する。  
      
    
2.  変更フィールド名称が含まれている **parm Method** を消去する。  
      
    
3.  変更フィールド名称が含まれている **set Method** を消去する。  
      
    例）  
    Fooテーブルの Barフィールドに変更を加えたのなら、  
    AxFoo ClassのparmBarメソッドを消去し、  
    setBarメソッドを消去する。

  

#### Update document serviceを実行する

1.  **Tool > Development tools > Application Integration Framework > Update document service** を起動する。  
      
    ![](http://docs.google.com/File?id=dhr8vrth_656c36z6rhb_b)  
      
    
2.  Service class name で サービス名を選択する。  
      
    
3.  変更内容がフィールドの削除だった場合は  
    **Regenerate data object classes** にのみチェックを入れる。  
      
    変更内容がフィールドの変更ないしは、追加だった場合は、  
    **Update AxBC classes** にもチェックを入れる。  
      
    
4.  OKを押す。  
      
    
5.  終わった後に ServiceのRefresh、  
    AOTのノードでのCompile & Synchronize を実行する。  
      
    

参考URL  
[http://msdn.microsoft.com/en-us/library/ee330229.aspx](http://msdn.microsoft.com/en-us/library/ee330229.aspx "http://msdn.microsoft.com/en-us/library/ee330229.aspx")