---
title: '[DynamicsAX2009][X++]安全なクラスキャストとシステム日付'
date: 2010-02-11T14:02:00.002+09:00
draft: false
tags : [X++, DynamicsAX2009]
---

X++の小技を自分メモ用に紹介。  
X++に対してgoogle-code-prettifyがうまく動作するか不安だがやってみる。  
  

1.  [安全なクラスキャスト](#_)
2.  [システム日付](#__28003452723446687)

  

[](http://www.blogger.com/post-edit.g?blogID=20219551&postID=5928169760714323016)安全なクラスキャスト
-------------------------------------------------------------------------------------------

  
```
static pulic void main(Args \_args)  
{  
    binaryIO b;  
    textIO t;  
    ;  
    b = SysDictClass::as(t,classIdGet(b));  
}  

```  

ちなみにObjectを使用して安全でないクラスキャストもできる。

  
```
static pulic void main(Args \_args)  
{  
    binaryIO b;  
    textIO t;  
    Object o;  
    ;  
    o = t;  
    b = o;  
}  

```  

[](http://www.blogger.com/post-edit.g?blogID=20219551&postID=5928169760714323016)システム日付
---------------------------------------------------------------------------------------

utcDateTime型とDate型で取得  
  

```
void method1()  
    {  
        utcDateTime utc;  
        Date d;  
        ;  
        utc = DateTimeUtil::applyTimeZoneOffset(  
                    DateTimeUtil::getSystemDateTime(),   
                    DateTimeUtil::getUserPreferredTimeZone()  
                    );  
  
        d = DateTimeUtil::date(utc);  
  
        print utc;  
        print d;  
    }  

```

  
実行結果

> 2010/12/12 12:12:12  
> 2010/12/12