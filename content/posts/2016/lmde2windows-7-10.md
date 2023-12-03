---
title: 'LMDE2とデュアルブートしているwindows 7 を 10 にアップグレードする'
date: 2016-02-18T01:57:00.001+09:00
draft: false
tags : [LMDE2, Windows 10, 技術, Windows 7]
---

結論から言うと、特に何も問題なく、あっさりアップグレードできました。

参考にしたのは以下のページ  
[How to Upgrade a Linux Dual-Boot System to Windows 10](http://www.howtogeek.com/226295/how-to-upgrade-a-linux-dual-boot-system-to-windows-10/)  
[http://www.howtogeek.com/226295/how-to-upgrade-a-linux-dual-boot-system-to-windows-10/](http://www.howtogeek.com/226295/how-to-upgrade-a-linux-dual-boot-system-to-windows-10/)

環境
==

まず私の環境を再度確認。  
Windows 7 SP1 と LMDE2 とのデュアルブート環境。  
Windows の Cドライブが入っている物理ストレージに LMDE2 を同居かつ、GRUB2が入っています。

Windows10 アップグレード
=================

上記記事の内容だと、Windows 10 アップグレード後に、GRUB2に影響が出て、Windows は起動できるが、Linuxは起動できない状態になるとありましたが、アップグレード後特に問題なく起動出来ました。

注意点としては、Windows 10 アップグレード時に３〜４回ぐらい（忘れました）再起動しますが、その時はGRUB2から Windows を選択してやる必要があるため、基本的にパソコン前に張り付いておく必要があります。

Windows 10 アップグレード後、GRUB2 への影響
==============================

何もありません。  
何もないので、引き続き GRUB2 には Windows 7と表記されいます。  
上記リンク先に、 ubuntu での GRUB2 の表記を Windows 10 に更新する方法が書かれていたので、それをヒントに LMDE2 でもできるかもしれませんが、特に困った事はなかったので私 7 の表記のまま使っています。

〆
=

私はアップグレード時に、特に問題は起きませんでしたが、  
他の環境ではどうなるか分からないので、ファイルはバックアップをしっかりとってから実行して下さい。