---
title: '[Windows]2月 Windows Update で XP がブルースクリーンになる現象について'
date: 2010-02-16T00:46:00.002+09:00
draft: false
tags : [Windows]
---

２月のWindowsUpdate適用後に  
WindowsXPがブルースクリーンになる現象が起きているそうです。  
  
多くは日本語環境以外でおきてるそうですが、油断はできません。  
  
  

現象：  
2 月MS10-015適用後に Windows Update を実行するとブルースクリーンになる。  
  
  
対象環境：  
WindowXP 32bit、WindowsVista  
  
  
対処方法：  
MS10-015 Windows カーネルのセキュリティ更新プログラム (977165) をアンインストールする。

  
  
現在WindowsのAutoUpdateでは、MS10-015の配信は停止していますが、  
手動でUpdateのチェックを行うとMS10-015のインストールが行われます。  
（止めんかい）  
  
  
この件に関して、日本のMSのセキュリティチームのブログにエントリがあります。  
  
MS10-015で再起動やブルースクリーンが発生する件について

[http://blogs.technet.com/jpsecurity/archive/2010/02/12/3312344.aspx](http://blogs.technet.com/jpsecurity/archive/2010/02/12/3312344.aspx "http://blogs.technet.com/jpsecurity/archive/2010/02/12/3312344.aspx")  
  
  
  
うーん、この前会社の開発用サーバ（Windows Server 2008 SP2)に  
MS10-015を適用してねーってMSから言われたばかりで手のひら返し  
流石MS !  
結局MSは悪くなかったってことがわかったので手のひら返しました。  
  
後、続報を書きました。  
→[\[Windows\]\[続報\]2月 Windows Update で XP がブルースクリーンになる現象について](http://blog.callas1900.net/2010/02/windows2-windows-update-xp.html)