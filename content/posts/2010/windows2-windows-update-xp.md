---
title: '[Windows][続報]2月 Windows Update で XP がブルースクリーンになる現象について'
date: 2010-02-22T23:57:00.000+09:00
draft: false
tags : [Windows]
---

[\[Windows\]2月 Windows Update で XP がブルースクリーンになる現象について](http://blog.callas1900.net/2010/02/windows2windowsupdatexp.html "[Windows]2月 Windows Update で XP がブルースクリーンになる現象について")  
の続報  
  

#### 結局MS10-015が悪いの？

どうやらMS10-015が悪い訳ではなく。  
ブルースクリーンが発生するのは、**Alureon** ルートキットなるマルウェアの感染が原因。  
  
（Alureon ルートキットが Windows カーネルのバイナリを変更することが原因で、  

システムが不安定になるためにブルースクリーン等が発生していた模様）  
  
後、Alureonは64bitシステムには影響しないため、  
64bit環境ではMS10-015を適用しても問題ないそうです。

(うちの仕事先の環境はWindows Server 2008 64bitだからよかったよかった。）  
  
現在マイクロソフトではAlureonを発見・駆除するためのソフトを開発中だそうです。  
（数週間かかるそうです）  
  
  
参考資料：  
Alureonに関する情報  
[http://www.casupport.jp/virusinfo/2006/win32\_alureon\_family.htm](http://www.casupport.jp/virusinfo/2006/win32_alureon_family.htm "http://www.casupport.jp/virusinfo/2006/win32_alureon_family.htm")  
  
MS日本セキュリティチームのブログ  
[http://blogs.technet.com/jpsecurity/archive/2010/02/18/3313624.aspx](http://blogs.technet.com/jpsecurity/archive/2010/02/18/3313624.aspx)