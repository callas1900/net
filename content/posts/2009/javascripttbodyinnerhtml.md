---
title: '[JavaScript]tbodyのinnerHTML'
date: 2009-02-25T23:02:00.002+09:00
draft: false
tags : [JavaScript]
---

ちょちょいとした計算ツールを使用するのにJavaScriptは便利だ。

  

だが問題がある、IEとFirefoxでは同一のスクリプトが動いたり動かなかったりすることがある。

  

今回はtbodyタグに関する話。

  

計算結果を表形式で表したい時にHTMLのtableタグを使用する。

得にtbodyタグの中身を可変編集することはよくするテクニックの一つだ。

  

以下のコードを見てもらいたい。

  

\---HTML

<table>

<thead>

<tr>

<th>index</th><th>内容</th>

</tr>

</thead>

<tbody id="tableBody"></tbody>

</table>

  

\---javaScript

  

function main(){

//HTML上のtbodyを取得

var tb = document.getElementById("tableBody");

//書き込む内容を作成

var tbHTML = '<tr><td>1</td><td>hoge</td></tr>'

           + '<tr><td>2</td><td>hogehoge</td></tr>';

tb.innerHTML = tbHTML;

}

  

上記コードはFireFoxやChromeだと動くのだが、

IEでは動かない。

  

ﾅﾝﾃﾞｴｴｴと思って調べてみると。

**Internet Explorer で **

**PRB エラー設定 table.innerHTML**  

[http://support.microsoft.com/kb/239832/ja](http://support.microsoft.com/kb/239832/ja)  

  

tbodyのinnerHTMLは読取り専用だと！

  

なのでこう書かないといけない。

  

\---javaScript

function main(){

//HTML上のtbodyを取得

var tb = document.getElementById("tableBody");

//DOMオブジェクトを作成

var tr = document.createElement('tr');

        var td1 = document.createElement('td');  

        var td2 = document.createElement('td');  

  

        //作成したオブジェクトを組み合わせてtbodyの中を作成  

        for(var i = 1; i < 3; i++){  

            td1.innerHTML = i;  

            td2.innerHTML = (i==1) ? "hoge"

                                               : "hogehoge";  

  

            tr.appendChild(td1);  

            tr.appendChild(td2);  

tb.appendChild(tr);

        }  

}