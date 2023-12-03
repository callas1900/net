---
title: '[BizTalk2009]BizTalk2009プロジェクト管理にVSS2005を使うとエラーポップアップ！'
date: 2010-02-28T14:50:00.000+09:00
draft: false
tags : [BizTalk2009]
---

VisualStudio2008でBizTalkServer2009のプロジェクトを作り、  
管理をVSS2005でしていたところ、  
開発メンバーからアップデート・チェックイン・チェックアウトが出来ないと苦情がきた。  
  
エラー表示ポップアップが出るそうだ。  
  

> Error: Not Implemented  
> File: vsee\\pkgs\\vssprovider\\csolutionnodebase.cpp  
> Line number:2111

ネットのフォーラムを漁ったところ、以下の記事を発見。  
  
[Error in Visual SourceSafe when checking in from Visual Studio 2008（＠Microsoft Connect)](http://connect.microsoft.com/VisualStudio/feedback/ViewFeedback.aspx?FeedbackID=350985 "Error in Visual SourceSafe when checking in from Visual Studio 2008（＠Microsoft Connect)")  
  
BizTalk Server 2009 プロジェクトを Visualk Studio 2008 で作成し、VSS2005でソース管理しようとした時に  
よく起きるバグらしい。（勘弁してくれー）  

#### 回避策１：エラーポップアップを無視

エラーメッセージボックスのOKボタンを何度か押して消していると  
モーダルが解けて後ろのボタンを押せるようになる。  
押せば問題なく、チェックイン等のアクションが成功する。  
  
  

#### 回避策２：ツリービューをフラットビューに変更する。

  
  

![](http://docs.google.com/File?id=dhr8vrth_282fqq88kfx_b)

  
どうやらツリービューの描画でエラーがおきているようだ。  
とりあえずこうすることでポップアップが出る現象は回避できた。  
  
ツリービュー or フラットビューの状態は各アクションごとに記憶されるので、  
各アクション一度はフラットビューへの変更を行わないといけないが、  
この方法が一番ストレスなくその後の作業に従事できるためオススメ。  
  
  
  
しかし・・・  
ほんとにコレでいいのか！BizTalkServer2009！