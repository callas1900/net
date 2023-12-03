---
title: '[DynamicsAX2009]Admin グループの権限が外れた場合の対処方法'
date: 2010-05-13T21:58:00.001+09:00
draft: false
tags : [DynamicsAX2009]
---

DynamicsAxにはデフォルトで管理者グループ「Admin」が存在します。

Adminは全ての画面・機能へのアクセス権限を持ち、それを修正することは出来ません。

  

しかしながら、開発時DBの差し替え、aodファイルによる定義差し替え等によって

Adminの権限が外れてしまう場合があります。

  

その状態を修正しようにも「Adminは全ての権限を持っている、かつ、修正する必要はない」

の要件が邪魔をして修正できません。

  

その際の対処方法を提示します。

  

#### Adminグループの権限を確認する方法

1.  Administration > Ad,omostratopm Area の  
    Setupセクション User group permissions を起動。  
      
    
2.  **Admin **を選択している状態で **Permissions **タブを選択  
      
    
3.  全て、**Full control** になっていることを確認する。  
      
    

#### Adminグループの権限を編集する方法

1.  AOTから Forms > SysUserGroupSecurity.isAdminをEditする。  
      
    
2.  **return true;　**をコメントアウトする。  
      
    
3.  これで先程のUser group permissions 画面で編集出来るようになる。  
      
    

  
ソース例  
  
```
#admin  
boolean isAdmin()  
{  
    if (userGroupInfo.Id == #AdminUserGroup &&  
       (domainInfo.Id    == #AdminDomain || !useDomains))  
    {  
        //return true;  
    }  
    return false;  
}  

```