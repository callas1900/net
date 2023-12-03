---
title: '[DynamicsAX2009]AIFファイル上限値とその解除'
date: 2010-05-07T18:07:00.001+09:00
draft: false
tags : [DynamicsAX2009]
---

#### デフォルト上限値の設定とエラー内容

DynamicsAXのAIFは外部ファイルとのやり取りを行うインターフェースの一つです。  
  

外部ファイルとのやり取り時、明示されてはいませんがファイルサイズの上限値があります。

デフォルトでは**10MB**に設定されています。  
  

これを超えるファイルのやり取りをAIFで行おうとすると下記エラーがイベントログに出力されます。

  

> The adapter is unable to send the following message to Microsoft Dynamics AX:  
> 
> MessageId: XXXXXXXX-1111-AAAA-9999-ZZZZZZZZZZZZ
> 
> Error: Error executing code: Insufficient memory to run script.
> 
> Error executing code:  object not initialized.
> 
>   
>   
>   
> 
> (C)\\Classes\\\\processRequest
> 
>   
>   
> 
> \--------------------------------------------------------------------------
> 
> Product Version : 5.0
> 
> Assembly Version : 5.0.0.0
> 
> Class : AppEventLog
> 
> Method : WriteLocalizedError
> 
> Subsystem : BizTalkDynamicsAdapter
> 
> \--------------------------------------------------------------------------
> 
>   
> 
> For more information, see Help and Support Center at http://go.microsoft.com/fwlink/events.asp.

  

#### 上限設定変更もしくは解除方法

レジストリを編集することで解除 or 上限値変更が出来ます。

  

1.  regeditを起動します。  
      
    
2.  **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Dynamics\\5.0\\Configuration\\Original (installed configuration)**  
    を開き以下のように編集。  
      
    
    Value name  
    
    maxbuffersize  
    
    Value type  
    
    REG\_SZ  
    
    Value  
    
    上限値(MB) or 0（上限値なし）  
    
      
    
3.  **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Dynamics Server\\5.0\\01\\Original (installed configuration)**  
    を開き以下のように編集。  
      
    
    Value name  
    
    maxbuffersize  
    
    Value type  
    
    REG\_SZ  
    
    Value  
    
    上限値(MB) or 0（上限値なし）  
    
      
    

※設定名でOriginal (installed configuration)設定を使用している時。  

  

#### 注意事項

上記説明ではファイルサイズとしたが上限値はファイルを展開した際のメモリの確保量になる。

なので10MB丁度のファイルをAIFで取り扱ったとしてもメモリ展開時に10MBを超えてしまうようなXML出会った場合は

エラーが出力される。

  

また、上限値なしは基本的にはお勧めしない（らしい）。

開発筋の情報では１ファイルの上限値は50,000行以下を推奨し、

100MB以上のファイルサイズのやりとりは想定していないそうだ。

  
  
参考URL:

[EMEA Dynamics AX Support : Error executing code: Insufficient memory to run script](http://blogs.msdn.com/emeadaxsupport/archive/2009/06/15/error-executing-code-insufficient-memory-to-run-script.aspx "EMEA Dynamics AX Support : Error executing code: Insufficient memory to run script")