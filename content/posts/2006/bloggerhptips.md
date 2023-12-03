---
title: 'Bloggerで自分のHP上にブログを公開する時のTIPS'
date: 2006-04-16T18:12:00.000+09:00
draft: false
tags : [Blogger]
---

BloggerにはFTP情報を登録して、  
自分のサイト上にHTMLファイルを吐き出させ表示すると言うことが出来る。  
  
実際、  
  
[http://www.callas1900.net/blog/](http://www.callas1900.net/blog/)  
  
にて効果しているわけだけど、以前は  
  
[http://callas1900.blogspot.com/](http://www.callas1900.net/blog/)  
  
でbloggerのブログホストを利用してホスティングしていました。  
  
で・・・今回独自ドメインをとったので、自分のＨＰスペース上で公開してみたんだけど、  
大抵の友達が前のブログにブックマークしてたので、  
前のＵＲＬからこちらのＵＲＬへとリダイレクトさせる方法を書いておきます。  
  
まず、blogspotの方でテンプレートの編集よりHTMLをいじり  
<head>～</head>に  
  
<meta equiv="refresh" content="5;url=http://www.callas1900.net/blog/" />  
  
を追加する  
（※bloggerはXHTMLなのでタグの末尾に～/>で終わる事と全部小文字で書くという事を忘れずに）  
  
後は、最後の記事を書き一度ホスティングする。  
そして、ＦＴＰ情報を書き込み自分のＨＰスペースにブログを公開する。  
きちんと公開できた事を確かめたら、  
上記メタタグをテンプレートの中から消去する。  
  
以上の結果が下記ＵＲＬとなる  
  
[http://callas1900.blogspot.com/](http://www.callas1900.net/blog/)