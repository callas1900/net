---
title: 'LMDE2のNVIDIA Driverを更新する'
date: 2016-01-14T00:28:00.001+09:00
draft: false
tags : [Linux, GPU, LMDE2, 技術]
---

LMDE2 に NVIDIA のグラフィックドライバを入れます。

*   [Inspect your graphic board](#inspect-your-graphic-board)
*   [Download a driver Installer](#download-a-driver-installer)
*   [Prepare Installation](#prepare-installation)
*   [Installation](#installation)

Inspect your graphic board
==========================

terminalで

```
lspci -vnn | grep VGA -A 12
```

Download a driver Installer
===========================

NVIDIAの公式サイトからLinux X64用のDriver Installerを手に入れます。  
私の場合は以下から  
[http://www.nvidia.com/download/driverResults.aspx/77525/en-us](http://www.nvidia.com/download/driverResults.aspx/77525/en-us)

**NVIDIA-Linux-x86\_64-340.32.run** というシェルファイルを手に入れました。

Prepare Installation
====================

reboot し grub で recovery mode を選択し、  
ログイン画面で、`Ctrl` + `Alt` + `F1` を押してCUIモードになります。  
ユーザーログイン後、

```
sudo update-initramfs -u
```

を実行します。  
これはNVIDIAシェルがカーネルモジュールを追加するため必要になります。  
これが実行されない場合  
Nouveau kernel driver を止めてくれとのエラーメッセージが表示されます。

Installation
============

再度再起動し、recovery modeになり、CUIモードにログインします。  
X serviceを止めます。

```
sudo service mdm stop
```

インストールを実行します。

```
sudo sh ~/Downloads/NVIDIA-Linux-x86_64-340.32.run
```

後は画面の支持に従い、選択していくだけです。  
終了後は再度再起動して、ログインしましょう。