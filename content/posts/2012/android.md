---
title: 'Androidで共通鍵暗号化でつまづいたので記録に残す'
date: 2012-10-01T09:00:00.000+09:00
draft: false
tags : [Java, Security, Android]
---

Androidで文字列をセキュアに保存したい場合、  
暗号化してsqliteに保存するのがよろしいと思われる。  
  
ここではAndroid自体のセキュリティがアレだとか、Rooted端末とapktoolがあればアレをこうしてアレ出来るだとかいう話はとりあえず置いとく。  
  
まず以下のようなソースを書いた。  
  
内容は、  
  

*   共通鍵の秘密鍵を生成している箇所のみ抽出。
*   DBに鍵が保存されていない初回はif文を迂回して生成ロジックで生成後DBに保存。
*   DB保存後はDBから復元する。

```
private final static String ARGOLISM = "PBEWithSHA1And256BitAES-CBC-BC";  
  
private SecretKey getSecretKey()  
throws NoSuchAlgorithmException, InvalidKeySpecException, NameNotFoundException {  
  
   // check saved secret key is exist.  
   byte\[\] savedSecretKey = DBHelper.readByteData(context, "hoge");  
  
   if(savedSecretKey != null && savedSecretKey.length > 0){  
      return new SecretKeySpec(savedSecretKey, ARGOLISM);  
   }  
  
   // generate new secret key.  
   char\[\] pw = generatePassword();  
   int iteratorCount = 1024;  
   int keySize = 256;  
   int saltLength = 8;  
   byte\[\] salt = "00000000".getBytes();  
  
   KeySpec keySpec = new PBEKeySpec(pw, salt, iteratorCount, keySize);  
  
   SecretKeyFactory factory = SecretKeyFactory.getInstance(ARGOLISM);  
   SecretKey secretKey = factory.generateSecret(keySpec);  
  
   // here  
  
   // save secret key.  
   DBHelper.writeByteData(context, "hoge", secretKey.getEncoded());  
  
   return secretKey;  
}  

```_※DBHelperはsqliteへの簡便なアクセスを提供するクラスとする。_  
_ここで使用しているDBHelperの先にあるテーブルはマップのようにkey/valueのデータ構造をしているものとする。_  
  
上記実行したところ、  
生成後のDBから読み出した鍵が暗号化した鍵とは違うとのExceptionが発生。  
secretKey.getEncoded()の値をDB書き込み前と後で見比べてみても同じ。  
ワケワカラーン  
  
結局、Exceptionの原因はクラス差でした。  
**生成前** : com.android.org.bouncycastle.jce.provider.JCEPBEKey  
**生成後** : javax.crypto.spec.SecretKeySpec  
  
<guchi>  
両方共 [SecretKey](http://java.sun.com/j2se/1.5.0/ja/docs/ja/api/javax/crypto/SecretKey.html "javax.crypto 内のインタフェース") を実装してるんだから、うまく動いてくれよ。  
後、**com.android.**org.bouncycastle.jce.provider.JCEPBEKey の太字部位が出力されるのってバグじゃないの？  
</guchi>  
  
解決方法は  
`secretKey = new SecretKeySpec(secretKey.getEncoded(), ARGOLISM);`  
を先ほどのコードのDB書き込み直前（コードの //here の箇所）に追加して問題解決。  
  
注意：saltの値は上記では簡易てますが、本当に使う場合はきちんとランダム値を生成するように変更してください。