---
title: '[BizTalk2009]VisualStudio2008でBizTalk新規プロジェクトが作れなくなる。'
date: 2010-02-19T02:49:00.002+09:00
draft: false
tags : [BizTalk2009]
---

BizTalk Server 2009 のプロジェクトをVisual Studio 2008 で作ってると  
ある日突然新規プロジェクトを作成しようとしても、  

> Creating project 'project name'… project creation failed.

が返ってきて失敗してしまうようになる。  
  
  
これはVisual Studio 2008 のバグである。  
修正方法が以下のブログにあったので書き記しておく。  
  
  

**Visual Studio 2008 fails to Create new BizTalk projects**

[http://blogs.msdn.com/biztalkcrt/archive/2009/08/21/visual-studio-2008-fails-to-create-open-biztalk-projects.aspx](http://blogs.msdn.com/biztalkcrt/archive/2009/08/21/visual-studio-2008-fails-to-create-open-biztalk-projects.aspx "http://blogs.msdn.com/biztalkcrt/archive/2009/08/21/visual-studio-2008-fails-to-create-open-biztalk-projects.aspx")  
  
  
修正するにはレジストリの編集が必要になる。  
レジストリはファイル名を指定して実行の欄で「regedit」と入力すれば編集出来る。  
  
  

#### Visual Studio 2008 32bit の場合

\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\VisualStudio\\9.0\\Projects\\{FAE04EC0-301F-11d3-BF4B-00C04F79EFBC}\]  
  
の中の  
  
"PossibleProjectExtensions"="csproj"　を  
  
"PossibleProjectExtensions"="csproj**;btproj**" に変更する。  
  
  

#### Visual Studio 2008 64bit の場合

\[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\VisualStudio\\9.0\\Projects\\{FAE04EC0-301F-11d3-BF4B-00C04F79EFBC}\]  
  
を上記32bitと同じように編集する。  
  
  

まとめ
---

上記のレジストリキーはデフォルトでは "csproj" であり、  
BizTalk2009のインストール時に "csproj;btproj" に変更されます。  
  
ただし、Visual Studio側に何らかの更新（Windows Update等）が入ったタイミングで、  
レジストリの値が元に戻されてしまうことがあります。  
  
つまり、何度でもこの事態は起きるので、プロジェクトの新規生成でこけたら  
とりあえずレジストリチェックを覗くようにしましょう。  
（覗きたくないですね！）