---
title: '[TS][Windows2008]期限が切れたターミナルサービスの復旧方法'
date: 2010-08-18T18:00:00.001+09:00
draft: false
tags : [TS, Windows2008Server]
---

  
ターミナルサービス（TS）の無料を使ってて、期限が切れた（切れそう）なので  
ライセンスを買って設定するなんてことありますよね。  
  

Windows 2008 Server でTSのライセンスが切れたので、設定方法を残しておきます。

  
**前提条件：TS License Serverのインストールを行うサーバーはDomain controllerであること。**  

#### **ライセンスサーバーのインストール**

1.  Server Managerを起動し、Rolesの中のTerminal Servicesを選択し、  
    右クリックメニューより**Add Role Services**を選択します。  
    ![](http://docs.google.com/File?id=dhr8vrth_730gqf5gkfj_b)  
      
    
2.  **TS Licensing**にチェックを入れてNext  
    ![](http://docs.google.com/File?id=dhr8vrth_731fbsftcgc_b)   
      
    
3.  Configure Discovery Scope for TS Licensing画面が出てくるので  
    ターミナルサービスがライセンスサーバーを探す範囲を選択してNext  
    (今回は**This Domain**)  
      
    
4.  Confirm Installation Selections画面で、**Install**をクリックして完了。  
    ![](http://docs.google.com/File?id=dhr8vrth_734g7zbdjfx_b) 

#### **ライセンスサーバーの設定**

1.  **Start > Administrative Tools > Terminal Services > TS Licensing Manager** を起動します。  
      
    
2.  対象とするサーバーの状態が**Not Activated** であることを確認する。  
      
    
3.  サーバーを選択し、**Action > Activate Server**を選択。  
    Activate Server Wizardが開始します。  
    ![](http://docs.google.com/File?id=dhr8vrth_736cv9c5vd5_b) 
4.  Connection Method画面は**Automatic connection(recommended)**を選択した状態でNext  
      
    
5.  Company Information(Provide the requested company information)画面 には必要事項を入れてNext  
      
    
6.  次画面のCompany Information(Enter this optional information)画面は空欄でNext  
      
    
7.  **Start Install Licenses Wizard Now**にチェックが入った状態でNext  
    ![](http://docs.google.com/File?id=dhr8vrth_740f2c899dd_b)   
      
    
8.  確認画面が出るので更にNext  
      
    
9.  License Program画面が出てくるので、License programをそれぞれのライセンスに合わせて選択。  
      
    
10.  ライセンス入力画面が出るので入力し、Next  
      
    
11.  Product version and License Type画面で  
    
    Product version :   
    
    **Windows Server 2008**  
    
    License type :  
    
    **Windows Server 2008 TS Per User CAL**  
    
    Quantity :  
    
    **4**  
    
      
    
12.  をそれぞれ入力し、Next  
      
    
13.  **Finish**を押して終了。

  

#### **ターミナルサービスの設定**

1.  **Start > Administrative Tools > Terminal Services > Terminal Services Configuration **を起動します。  
     
2.  Edit settingsセクション内のLicensing セクションの  
    terminal Services licensing modeのプロパティを右クリックメニューから呼び出します。  
      
    
3.  LicensingタブのSpecify the terminal Services licensing mode を**Not yet configured**から  
    Per User か Per Device にライセンスにあわせて変更する。  
    （他の項目は環境にあわせて変更する可能性あり）。  
    

以上。