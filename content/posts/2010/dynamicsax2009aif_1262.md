---
title: '[DynamicsAX2009]AIFの実行環境設定'
date: 2010-01-21T00:49:00.001+09:00
draft: false
tags : [DynamicsAX2009]
---

AIFの実行環境設定
==========

  

AXのBasicメニューより以下を設定する。

  

1.  [AIFの実行環境設定](#AIF_)
    1.  [Local endpoints設定](#Local_endpoints__8968848049685931)
    2.  [Transport adapters設定](#Transport_adapters_)
    3.  [Channels設定](#Channels_)
        1.  [File System Adapter](#File_System_Adapter)
        2.  [BizTalk Adapter](#BizTalk_Adapter)
    4.  [Endpoints設定](#Endpoints_)
        1.  [Data policies設定](#Data_policies__8025217221087917)
        2.  [Endpoint有効化](#Endpoint_)

  
  
  

Local endpoints設定
-----------------

  
会社毎にLocal endpointsを設定する。  
Local endpointsはI/Oを許可した会社の別名と考えれられる。  
  
Newボタンを押し以下項目を設定する。  
  

![](http://docs.google.com/File?id=dhr8vrth_256gg2h7gf9_b)

  

Company 

セレクトボックスより設定したい会社名

Local endpoint

任意の名前

  
  

Transport adapters設定
--------------------

  
どのアダプターを使用するかを決定する。  
  
通常は**File System Adapter**を使用するが、  
**BizTalk Adapter**等の特殊な設定も存在する。  
  

![](http://docs.google.com/File?id=dhr8vrth_257cb2p3hfs_b)

  

  

Adapter class

セレクトボックスより設定したいAdapterClass名称を選択。

Name

Adapter classより自動設定される。

Active

チェックを入れる。

Direction

Adapter classより自動設定される。  

  
  

Channels設定
----------

AIFで使用するXMLファイルのI/Oの場所設定を行う。

  

### File System Adapter

Outboundを作成してから、Inbound作成すること

そうしなければResponse channelの設定で少しつまる。

  

Response channelの設定は、  
Inboundの場合は対応するOutboundを、

Outboundの場合はブランク、

Bothの場合は自信の設定を入力する。  
  

### BizTalk Adapter

DirectionがBothになることと、  
Response channelが自分自身になること、  
それから**Configureボタンでサーバー名称の設定をすること**を忘れない。  
  
※他環境から設定をインポートする際にここの変更を忘れることが多い。  
  

  

[![](http://docs.google.com/File?id=dhr8vrth_258f3f7mkc4_b)](http://docs.google.com/File?id=dhr8vrth_258f3f7mkc4_b)

  

Channel ID

任意のID

Name

任意の名前

Active

チェックを入れる

Adapter

Transport adapters設定で作成したAdapter

Direction

Inbound(入力)  
Outbound(出力)  
Both(両方)  

Parallel processing

チェックを入れなくてもよい

Address

File System Adapterの場合はサーバーのフォルダ。  
BizTalk Adapter等の場合はIPアドレス等

Response channel

※上記参照

  
  

Endpoints設定
-----------

**Endpoint追加**

まずはNewボタンで新規設定を追加

  

![](http://docs.google.com/File?id=dhr8vrth_259hcxpzjwv_b)

  

  

次にGeneralタブに切り替え**Endpoint ID**と**Name**を任意の名称で追加。

**Outbound channel ID**にChannels設定で追加したものを設定。

**Local endpoint ID**にLocal endpoints設定で追加したものを設定。

  

![](http://docs.google.com/File?id=dhr8vrth_261c6z4zgcr_b)

  

  
Constraintsタブに切り替えてNo constraintsチェックボックスを有効にしておく。

  

![](http://docs.google.com/File?id=dhr8vrth_262gq77frfm_b)

  

Usersタブに切り替えてNewボタンを押し、

AIFを許可するユーザーもしくはユーザーグループの設定を追加し、保存する。

  

![](http://docs.google.com/File?id=dhr8vrth_263dsdfrvcn_b)

  

例では

User type

User group

Application user or group

Admin

Name

自動設定

  
  
**Action policy設定**

次にAction policiesボタンを押し

（保存ボタンを押していないとエラーが出るので注意）

  

Action IDをセレクトボタンより設定する。

  

ここで\[サービス名称.アクション名称\]を選択し設定するのだが、

この一覧にサービスを表示させるためには、

  

Setup > Services の中でEnableチェックボックスを有効にする必要がある。

  

選択したらStatusをEnabledにしておく。

  

[![](http://docs.google.com/File?id=dhr8vrth_264f79smscw_b)](http://docs.google.com/File?id=dhr8vrth_264f79smscw_b)

  

### Data policies設定

次にData policiesボタンを押し、ポップアップしたウィンドウの中のData policiesボタンを押す。

公開したいField項目にEnabledを設定する。

  

![](http://docs.google.com/File?id=dhr8vrth_265dkm7fjd4_b)

  

  

### Endpoint有効化

Endpointウィンドウに戻り、

Overviewタブで作成したEndpointのActiveチェックボックスにチェックを入れる。

  

  

以上。