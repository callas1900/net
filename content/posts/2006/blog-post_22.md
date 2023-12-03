---
title: 'ご無沙汰ご無沙汰'
date: 2006-03-22T10:46:00.000+09:00
draft: false
tags : [日記]
---

最近、転職を決意しましたcallasであります。  
  
  
ほぼ中心的な業務だったものを渡してしまえば、  
  
結構気楽な日々だったりします。  
  
  
来月には無職になるのだなぁって思うと、ちょっとアレですが。  
  
  
ま、これも次へのステップアップだと思ってがんばります！  
  
  
  
  
注：下の方でカオスな内容になっているのは精神的に不安定だったから思われ＾＾；  
  
  
  
  
今日のネタ  
  
メールアドレスの検閲というものがPHPなどではあります。  
  
私が触っているxmlでもXMLSchemaなるものを使用して入力されたデータが正しいか？  
  
という事を考えたりします。  
  
  
  
上の例に従いメールアドレスを検閲するとすると  
  
  
  
\[\\w\\.-\]+(\\+\[\\w-\]\*)?@(\[\\w-\]+\\.)+\[\\w-\]+  
  
  
  
となります。教科書的ですね。（個人的には\[\\w\\.-\]+@(\[\\w-\]+\\.)+\[\\w-\]+で十分だと思うのですけど・・・）  
  
  
  
今回見つけたのは  
  
ハイ  
  
  
  

  
^\[0-9,A-Z,a-z\]\[0-9,a-z,A-Z,\_,\\.,-\]+@\[0-9,A-Z,a-z\]\[0-9,a-z,A-Z,\_,\\.,-\]+\\.(af|al|dz|as|ad|ao|ai|aq|ag|ar|am|aw|ac|au|at|az|bh|bd|bb|by|bj|bm|bt|bo|ba|bw|br|io|bn|bg|bf|bi|kh|cm|ca|cv|cf|td|gg|je|cl|cn|cx|cc|co|km|cg|cd|ck|cr|ci|hr|cu|cy|cz|dk|dj|dm|do|tp|ec|eg|sv|gq|er|ee|et|fk|fo|fj|fi|fr|gf|pf|tf|fx|ga|gm|ge|de|gh|gi|gd|gp|gu|gt|gn|gw|gy|ht|hm|hn|hk|hu|is|in|id|ir|iq|ie|im|il|it|jm|jo|kz|ke|ki|kp|kr|kw|kg|la|lv|lb|ls|lr|ly|li|lt|lu|mo|mk|mg|mw|my|mv|ml|mt|mh|mq|mr|mu|yt|mx|fm|md|mc|mn|ms|ma|mz|mm|na|nr|np|nl|an|nc|nz|ni|ne|ng|nu|nf|mp|no|om|pk|pw|pa|pg|py|pe|ph|pn|pl|pt|pr|qa|re|ro|ru|rw|kn|lc|vc|ws|sm|st|sa|sn|sc|sl|sg|sk|si|sb|so|za|gs|es|lk|sh|pm|sd|sr|sj|sz|se|ch|sy|tw|tj|tz|th|bs|ky|tg|tk|to|tt|tn|tr|tm|tc|tv|ug|ua|ae|uk|us|um|uy|uz|vu|va|ve|vn|vg|vi|wf|eh|ye|yu|zm|zw|com|net|org|gov|edu|int|mil|biz|info|name|pro|jp)

  
  
ドーン  
  
なんじゃこりゃあああああ（マツダユーサクLOVE  
  
  
  
正規表現のみですべて検閲しちまおーっていう挑戦的な正規表現ですなぁ・・・作ったやつは馬鹿だね（笑