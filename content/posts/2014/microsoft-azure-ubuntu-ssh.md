---
title: 'Microsoft Azure で ubuntu サーバー立てて sshで繋いでみる'
date: 2014-08-25T19:00:00.000+09:00
draft: false
tags : [ssh, ubuntu, Azure]
---

AWSに関しては散々方々で語られているのでAzureに手を出してみた。  
Windowsしか作れないと思ってたらちゃんとubuntuも用意されているし、最近追加された新ビューだとMySQLも作れるようになっている。  
  

### Windows上にsshを入れる（読み飛ばし可）

  
ubuntuに繋げるためにsshが必要、鍵作成にopensslもいるので  
msygitをインストール。  
今後の事を考え、CUIベースのパッケージ管理ソフトが欲しい。  
chocolateyが流行っぽいのでchocolatey経由でmsygitをインストールする。  
  
  

1.  chocolatey installation  
    [https://github.com/chocolatey/chocolatey/wiki/Installation](https://github.com/chocolatey/chocolatey/wiki/Installation)  
    作業はPowerShellでやった。成功するとcinstコマンドが認識される。
2.  msysgitをインストールする  
      
    ```
    cinst msysgit
    ```  
      
    でmsysgitをインストールこれでsshもopensslも使える。
3.  それぞれのコマンドを打てば認識されているのがわかる。  
    もし認識されていないようだったらパスが通っていない可能性があるので通す。

  
  

### SSHの鍵作成

  
適当に鍵を作ると、サーバー作成時に以下のエラーが出てサーバー作成に失敗する。  

> The certificate is in an invalid format. X.509 standard format in a .cer or .pem file is supported.。

回避するには以下リンク先の手順通りに鍵を作成する必要がある。  
  
How to Use SSH with Linux on Azure  
[http://azure.microsoft.com/ja-jp/documentation/articles/virtual-machines-linux-use-ssh-key/](http://azure.microsoft.com/ja-jp/documentation/articles/virtual-machines-linux-use-ssh-key/)  
  
Get OpenSSL on Windowsのセクションに  
msysgitインストールからの手順が書かれている。  
鍵が出来たら、chocolateyのルートディレクトリに.sshがあるので（無ければ作る）  
そこに突っ込んでおく。  
  

### Ubuntuサーバー作成

  
Azureにubuntuを立てる方法は  
Newメニューを開いてUbuntuを選択し作るだけ（デフォルトでは12系と14系が選べる）、  
UIの画面込みで説明したいけど、すぐUI構成変わりそうなので割愛。  
  
どこに作ればいいのかは料金表と睨めっこして決める  
料金詳細：[http://azure.microsoft.com/ja-jp/pricing/details/virtual-machines/#linux](http://azure.microsoft.com/ja-jp/pricing/details/virtual-machines/#linux)  
  
  

*   作成時に、SSH用の公開鍵を指定する箇所があるので指定する。
*   指定したusernameをメモっておく。

  
Createを押して暫く待つと出来てる。  
  

### Ubuntuに繋げる

  
sshの接続には以下コマンドを使用する。  

> ssh -i  myPrivateKey.key -p <port> username@servicename.cloudapp.net

*   portに関しては何も考えずにubuntu作っておけば22番がendpointとして登録されている。別途作成したい場合はendpointの箇所で作成出来る。
*   引数-iの鍵は実際のmyPrivateKey.keyのパスを指定する。
*   usernameはサーバー作成時に作ったもの、デフォルトだとazureuser
*   serverの接続情報は作成したサーバーのプロパティを見れば、SSHと書いてる箇所があるのでそれを使う。

  

接続完了