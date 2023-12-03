---
title: '[VB.NET]文字列型列挙体の実装'
date: 2008-12-24T11:29:00.002+09:00
draft: false
tags : [VB.NET]
---

**enum**とか使っていると、文字列型列挙体が欲しくなってきます。  
  
VB.NETはまだ初心者ですけど、ちょっと考え付いたのでメモ書き。  
  
以下コードと解説  
  
  
  
コード  

* * *

  
`Public Structure sampleStructure  
      Public Const hoge As String = "hogehoge"  
      Public Const fuga As String = "fugafuga"  
      Public Const foo As String = "foofoo"  
      Public Const bar As String = "barbar"  
  
      '構造体用インスタンスメンバをダミー実装  
      Private dummy As String  
  
      '構造体のReferenceEqualsを参照出来なくする。  
      Private Shadows Function ReferenceEquals() As Object  
          Return New Object  
        End Function  
  
      '構造体のEqualsを参照出来なくする。  
      Private Shadows Function equals() As Object  
          Return New Object  
        End Function  
  End Structure  
  
`  

* * *

  
解説  
  
ポイントはインスタンスメンバのdummy実装と、shadowsによる参照制限  
  

  
インスタンスメンバのdummy実装はもしかしたら何とかできるかもしれない。  
とりあえずメンバ変数がConstのみだとコンパイラに怒られるので、  
Private宣言でdummyを実装してみた。  
  

  
もちろん インスタンスメンバをPrivate宣言に変更し、  
ReadOnly Property でゲッターメソッドのみを定義すれば

dummy実装なんていらないんだろうけど。  
  
構造体自体の可読性を重視して廃止。  
  
  
次に構造体はequalsメソッドと、`ReferenceEqualsメソッドを実装している。  
`

`これらがあると、この構造体を参照した時に両メソッドが参照されてしまう。  
  
`  

![](http://docs.google.com/File?id=dhr8vrth_148hb6s47hr_b)

  
それを防ぐためにShadowsで両メソッドをPrivateで上書きする。  
  
そうすると。候補から両メソッドが消える。  
  

![](http://docs.google.com/File?id=dhr8vrth_149c7d2hggb_b)

  
以上で解説終わり。