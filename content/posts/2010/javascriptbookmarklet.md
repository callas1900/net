---
title: '[JavaScript]BookMarklet覚書'
date: 2010-01-30T00:48:00.005+09:00
draft: false
tags : [JavaScript]
---

BookMarkletはJavaScriptで作られた一行のプログラムです。

javaScriptで書いたものを一行にすればとりあえず動くと思って下さい。

  

サンプル実行方法はブラウザのURL入力欄に張り付けとシンプルなものです。

  

  

### もっとも単純なHello,world!

```
javascript:alert('Hello,world!');   

```

  

上記コードをブラウザのURL入力欄に入れてみてください。

Hello, world!とポップアップウィンドウが表示されるはずです。

  

### 処理を関数化したHello,world!

```
javascript:(function(){function%20helloWorld(){alert('Hello,world!');}helloWorld();})();   
  

```

  

先程までとまったく同じ動きをするプログラムですが、

  
```
javascript:(function(){  
//スクリプト内容  
})();   

```

というフォーマットに従って書いています。

  

通常BookMarkletの変数はvar宣言してもグローバル変数になってしまうのですが、

このように無名ファンクションのインスタンス呼び出しにすることで変数をローカル扱いすることができます。

  

  

また関数を内部で定義し、後に呼び出すといったことも出来ます。

  

```
javascript:(function(){function%20msgAlert(msg){alert(msg);}  
var%20txt;txt='Hello,world!';msgAlert(txt);})();   

```

  

時々出てくる'%20'は半角スペースのURLエンコードです。

これ以外にも日本語を使用するためにはURLエンコードが必要になります。

URLエンコードはサイトを探せばなんなりと出てきますのでGoogle先生にでもお尋ねください。