---
title: 'Strutsハマリチュウ'
date: 2007-01-12T00:37:00.000+09:00
draft: false
tags : [WorkLog]
---

本日は曇天ではあるけど、早めに起きれたので朝はゆったり。  
遅刻する心配もまったくねーやと思い、余裕で出発  
そんな日に限って電車事故  
会社につけば、2,3分のほんのり遅刻  
ま、記録に残らないからいいけどね（列車遅延の証明書を提出したので）  
  
仕事ではいい意味でも、悪い意味でもStrutsにはまっています。  
（正確にはStrutsを基盤にした別フレームワークなんだけど、会社名がその名前の中に含まれているので、公表を控えます）  
  
PGやっている上で何が快感かと問われれば、  
答えは幾通りもあると思いますが、  
  
私の場合は「未知の言語を読み解いた瞬間」かな。  
  
もちろん自分が作った物が動いた時も嬉しいけど、  
知らなかった言語などの読み方がわかった瞬間は  
異星人と対話に成功したようなカタルシスがあります。  
例えば、  
  
<!-- 氏名入力欄 -->  
<field property="nameInput" depends="size,mask">  
<msg name="size" key="CMDATXSE003" />  
<arg0 key="${var:nameInput}" resource="false" />  
<arg1 name="size" key="CMDATXKM001" />  
<arg2 name="size" key="${var:size}" resource="false" />  
<var>  
<var-name>nameInput</var-name>  
<var-value>氏名入力欄</var-value>  
</var>  
<var>  
<var-name>size</var-name>  
<var-value>20</var-value>  
</var>  
<var>  
<var-name>mask</var-name>  
<var-value>${omit}</var-value>  
</var>  
</field>  
  
  
  
  
といったものを見せられても、  
普通の人はチンプンカンプンなわけです。  
  
でも私たちは他の資料も多少必要ですが、  
これを見れば  
  
「ああ、氏名入力欄は半角なら20文字、全角なら10文字で入力しないといけないんだなぁ」  
「間違えるとエラーメッセージが -氏名入力欄は全角10文字半角20文字で入力してください- と出るのか」  
「あ～、使っちゃいけない文字何個かあるけどSQLインジェクション回避のためかな？」  
  
なんていう情報を読めたりします。  
ただ、読めるようになるまでは頭かきむしりうなる毎日。  
ある日、ふと読めるようになるとプワァ～と頭の中がスッキリしてモヤモヤが消し飛ぶ、  
その瞬間がたまりません。