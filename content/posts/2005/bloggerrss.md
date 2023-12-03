---
title: 'bloggerのrss情報を拾ってみる。'
date: 2005-12-28T12:10:00.000+09:00
draft: false
tags : [Blogger]
---

試しにこのブログのrssを拾ってみる  
<link rel="alternate" type="application/atom+xml"  
title="Exteml" href="[http://callas1900.blogspot.com/atom.xml](http://callas1900.blogspot.com/atom.xml)" />  
link要素のrelがalternateの場合それは代価文章を表すので  
このURIがrss情報を表すはずだ  
うーむ、予想通りatom+xmlって書いてるってことはatomに対応しているなぁ・・・  
ていうかxml形式だし・・・  
  
さてさて上記ハイパーリンクを開いてみる。  
あれ・・・いつもならxmlのソースちっくなものが出てくるのにきっちり整形されてるなぁ  
cssの定義をきっちりしているのか？  
とりあえずソースソースっと・・・あら？  
xmlはダメーって中身見せてくれねーな。xmlが外部プラグインだからそんなもんなんか・・・  
んじゃURIの前にime.nu/ってつけてDLっとふむふむ・・・  
なんじゃこりゃ・・・・ああ・・とりあえず予想通り  
<?xml-stylesheet href="[http://www.blogger.com/styles/atom.css](http://www.blogger.com/styles/atom.css)" type="text/css"?>  
でスタイルシートは定義されてるなうーん・・・わからんのは  
  
<link href="[https://www.blogger.com/atom/20219551](https://www.blogger.com/atom/20219551)" rel="service.post" title="Exteml" type="application/atom+xml"/>  
<link href="[https://www.blogger.com/atom/20219551](https://www.blogger.com/atom/20219551)" rel="service.feed" title="Exteml" type="application/atom+xml"/>  
  
の二列で読み込まれてるrel要素の"service.post"と"service.feed"  
だな・・・なーんじゃこりゃ・・・  
後、FC2のRSSなんかはCDATAで文章が定義されていたのに・・・  
なんぞいやこりゃ・・・  
んーあー（ﾟДﾟ)y─┛~~  
もしかして  
<title mode="escaped" type="text/html">;（ﾟДﾟ)y─┛~~ﾏｽﾞｰ</title>  
<content type="application/xhtml+xml" xml:base="[http://callas1900.blogspot.com/](http://callas1900.blogspot.com/)" xml:space="preserve">  
<div xmlns="[http://www.w3.org/1999/xhtml](http://www.w3.org/1999/xhtml);右近からタバコもらった・・・<br/>秋山さんから肺に入れろといわれた<br/>入れてみた<br/>むせた<br/>むせた<br/>二度と吸うものか・・・・</div></content\>  
  
の部分でxml情報からxhtmlに変更してるのか・・・？  
そうすれば、ブログの情報を綺麗に流せるなぁ・・・（Bloggerはxhtml1.0で書かれていた)  
なるほどなるほど、そうすればxhtmlの利用価値も高まるよなぁ（ﾟДﾟ ）  
後気になるのは、元々のblogのソースの方で  
やはり<link>のrel要素でservice.postが書かれている点  
(httpsでsslを通してるのも気になるし、あ、ちなみにブログのIDとPASSで中に入れました。中身はブログの発行されてたXMLと同じです。)  
EditURIなんてのもある・・・  
今日はここらでお手上げー∩(ﾟ∀ﾟ∩)