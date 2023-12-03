---
title: '[DynamicsAX2009]X++でよく使う型とそのスコープのまとめ'
date: 2010-01-16T16:45:00.006+09:00
draft: false
tags : [DynamicsAX2009]
---

X++でよく使う型とそのスコープのまとめ
--------------------

時々質問が飛んでくるので、メモ。  

### 標準的な型

  

型  

スコープ  

Deault  

int  

\-2,147,483,648 ～ 2,147,483,647  

0  

int64  

\-9,223,372,036,854,775,808 ～ 9,223,372,036,854,775,808  

0  

real  

\]-(10)127～(10)127 \[,        
  
16桁の精度を守りつつ。  

0.00  

String  

Unlimited  

""  

TimeOfDay  

0～86400(32bit)  

0  

date  

1/1/1900 ～ 31/12/2154  

1/1/1900  

utcdatetime  

1900-01-01T00:00:00 ～ 2154-12-31T23:59:59  
  
この値の最小と最大がtimeOfDay型とdate型でも最小最大である。  

1900-01-01T00:00:00  

  

realはBCD-encoding: 64 bitとあるので  (※BCD=binary coded decimals=二進化十進数)  

16桁の精度を持ったDecimal型である。  

### Boolean

表示  

Bool値  

1  

True  

0  

False  

true  

True  

false  

False  

44  

True  

  

Default : false  

  

  

**X++データ型とXSD型のマッピング**  

ついでにAIF使ってたらよく出てくるのでXSD型とのマッピングも書いておく。  

  

X++データ型  

XSD型  

String  

xsd:string,maxLength=StringSize  

Integer  

xsd:time , ISO format:HH:MM:SS  
  
(global::isTypeTime が True の場合はタイムスタンプ  

Int64  

xsd:long  

real  

xsd:decimal , fractionDigits=NoOfDecimals  

date  

xsd:date , ISO format:YYYY-MM-DD  

Enum  

xsd:string , enumeration=<EnumName>,...  

GUID  

xsd:string , pattern='\[0-9A-Fa-f\]{8}...'  

BLOB  

xsd:string , Base64 encoded