---
title: '[BizTalk2009]BtsTaskによるバッチ作成'
date: 2010-03-23T22:56:00.005+09:00
draft: false
tags : [BizTalk2009]
---

btstaskはBizTalkアプリケーションのインストール等をコマンドライン上で行えるコマンドラインツールです。

以下に自分の使用例を書いときます。

  
  

1.  [バインド設定を省いたアプリケーションのmsiファイルを作成する方法](#_msi__9627675348892808)
2.  [バッチ例](#_7420771233737469)

1.  [msiファイルとバインド設定ファイルをエクスポートする](#msi__2998540448024869)
2.  [msiファイルからBizTalkアプリをインストールする](#msi_BizTalk_)
3.  [バインド設定をインポートする](#__8566624764353037)
4.  [msiファイルを使った対象BizTalkアプリを削除する](#msi_BizTalk__8431878918781877)

  
  

### バインド設定を省いたアプリケーションのmsiファイルを作成する方法

1.  アプリケーションネーム(ここではBizApp1とする）を指定し、リソースXMLファイルを作成する。  
    ```
    btstask listapp -a:_**BizApp1**_ -r:_**BizApp1\_Resource.xml**_
    ```
2.  _**BizApp1\_Resource.xml **を修正する。  
      
    <Resources>タグ以下の  
    <Resource Type="System.BizTalk:BizTalkBinding"  
    で始まるタグを削除する。  
      
    _
3.  エクスポート実行  
    ```
    btstask ExportApp -a:_**BizApp1**_ -p:_**<MsiFileName>**_ -r:_**BizApp1\_Resource.xml**_
    ```
4.  バインドファイルもエクスポート実行  
    ```
    btstask ExportBindings -Destination:**_BindFile.xml_** -ApplicationName:_**BizApp1**_
    ```

  

### バッチ例

#### msiファイルとバインド設定ファイルをエクスポートする

```
@setlocal  
@echo off  
  
echo ##################################  
echo %DATE% %TIME% Running export.bat  
echo ##################################  
  
REM !!!!You edit this block!!!!  
call :SUB BizApp1  
call :SUB BizApp2  
REM !!!!You edit this block!!!!  
  
@endlocal  
goto :EOF  
  
:SUB  
  
set APP\_NAME=%1  
set MSI\_NAME="%~dp0%1.msi"  
set XML\_NAME="%~dp0%1.BindingInfo.xml"  
set RES\_NAME="%~dp0%1\_Resource.xml"  
  
  
REM \#### Resource.xmlを指定して、エクスポートします。  
btstask ExportApp -a:%APP\_NAME% -p:%MSI\_NAME% -r:%RES\_NAME%  
  
REM \#### バインド設定xmlをエクスポートします。  
btstask ExportBindings -Destination:%XML\_NAME% -ApplicationName:%APP\_NAME%  

```  
  

#### **msiファイルからBizTalkアプリをインストールする**

```
@setlocal  
@echo off  
  
echo ##################################  
echo %DATE% %TIME% Running create.bat  
echo ##################################  
  
REM !!!!You edit here!!!!  
call :SUB BizApp1  
call :SUB BizApp2  
REM !!!!You edit here!!!!  
  
@endlocal  
goto :EOF  
  
:SUB  
set MSI\_NAME="%~dp0%1.msi"  
set APP\_NAME=%1  
  
echo ##################################  
echo %MSI\_NAME% %APP\_NAME%  
echo ##################################  
  
REM #### msiファイルをローカルに展開する。  
msiexec /i %MSI\_NAME% TARGETDIR="%cd%" /qn  
  
REM #### BizTalk アプリを作る  
BTSTask AddApp -ApplicationName:%APP\_NAME%  
  
REM #### BizTalk アプリの設定をインポートする  
BTSTask ImportApp -Package:%MSI\_NAME% -ApplicationName:%APP\_NAME% -o  

```  
  

#### バインド設定をインポートする

```
@echo off  
@setlocal  
  
echo ##################################  
echo %DATE% %TIME% Running importBindings.bat  
echo ##################################  
  
REM !!!!You edit here!!!!  
call :SUB BizApp1  
call :SUB BizApp2  
REM !!!!You edit here!!!!  
  
@endlocal  
goto :EOF  
  
:SUB  
set XML\_NAME="%~dp0%1.BindingInfo.xml"  
set APP\_NAME=%1  
btstask ImportBindings -Source:%XML\_NAME% -ApplicationName:%APP\_NAME%  

```  
  

#### msiファイルを使った対象BizTalkアプリを削除する

```
@echo off  
@setlocal  
  
echo ##################################  
echo %DATE% %TIME% Running remove.bat  
echo ##################################  
  
REM !!!!You edit here!!!!  
call :SUB BizApp1  
call :SUB BizApp2  
REM !!!!You edit here!!!!  
  
@endlocal  
goto :EOF  
  
:SUB  
set APP\_NAME=%1  
set MSI\_NAME="%~dp0%1.msi"  
  
REM #### アプリケーションを削除します。  
BTSTask RemoveApp -ApplicationName:%APP\_NAME%  
BTSTask UninstallApp -ApplicationName:%APP\_NAME%  
  
REM #### msiファイルを削除します  
msiexec /x %MSI\_NAME% /qb  

```