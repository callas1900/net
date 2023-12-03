---
title: '[JavaScript][VBScript]VBScript + Javascriptで簡単プロジェクト内ツール。その２'
date: 2010-07-08T13:55:00.001+09:00
draft: false
tags : [JavaScript, VBScript]
---

#### ０埋めはsliceを使え。

数値の０埋め処理のやり方

  

３桁０埋め

  
```
function zeroPadding3(num){  
    return ("000" + num).slice(-3);  
}  

```  

#### 日付型は6/31日とかセットするとちゃんと7/1になってくれる。

```
//月は0で1月、5で6月  
alert(new Date(2010,5,31));  

```  

実行結果

Thu Jul 1 00:00:00 UTC+0900 2010

  

#### ショートカットを実装するにはshortcuts.jsが便利。

サンプル

```
shortcut.add("Ctrl+B",function() {  
	alert("The bookmarks of your browser will show up after this alert...");  
}  

```  

参考URL:

[http://www.openjs.com/scripts/events/keyboard\_shortcuts/#add\_docs](http://www.openjs.com/scripts/events/keyboard_shortcuts/#add_docs "http://www.openjs.com/scripts/events/keyboard_shortcuts/#add_docs")

  

#### setTimeoutの繰り返しは自己呼び出しで

```
function hoge(){  
	alert("hoge");  
	setTimeout(hoge,1000);  
}  

```

ただしこれをhogeと関数オブジェクトで呼び出さずに

hoge()とするとブラウザが壊れるので要注意。

  
以上で細々とした備忘終わり。