---
title: 'JB_MR1(4.2)とJB_MR2(4.3)のPermission比較（メーカー署名関係）'
date: 2013-11-01T12:40:00.001+09:00
draft: false
tags : [signature, JB_MR1, 4.3, 4.2, Android, JB_MR2]
---

Android 4.3 (JELLY\_BEAN\_MR2) が出て結構時間がたちました、恒例のsignatureがらみのPermission比較やらなきゃーと思って放置してたら4.4(Kitkat)が出ちゃったので慌てて更新します。  
前回までのPermission比較は  
  

*   [ICSとGingerbreadのPermission比較（メーカー署名関係）](http://blog.callas1900.net/2011/11/icsgingerbreadpermission.html)
*   [JBとICSのPermission比較（メーカー署名関係）](http://blog.callas1900.net/2012/08/jbicspermission.html)
*   [JB(4.1)とJB\_MR1(4.2)のPermission比較（メーカー署名関係）](http://blog.callas1900.net/2012/12/jb41jbmr142permission.html)

  
にあります。  
  

  

何調べてるの？
-------

本記事は署名関係の Android Permission に注目してバージョン間の差分を比較しています。  
これらの Permission が要求されるAPIに関してはOSビルド時の署名が必要になります。

メーカー端末であれば販売メーカーに依頼を出して署名をしてもらう必要がありますが、

通常出来ません。  
よって3rdパーティアプリを作成する場合これらの Permission を要求されるAPIは使用不可能になります。  
Androidはバージョンアップを重ねる毎にこれら Permission の締め付けがきつくなってるのでバージョンアップ毎にチェックしています。

  

JB MR1 と JB MR2 のプロテクションレベルの一覧比較
--------------------------------

  
**JB MR1**  

*   dangerous
*   signature|system
*   normal
*   signature
*   signature|system|development
*   system|signature
*   signatureOrSystem

**JB MR2**  

*   dangerous
*   signature|system
*   normal
*   signature
*   signature|system|development
*   system|signature
*   signatureOrSystem

特に変更はありませんね。

  

  

Permission増減調査(JB MR1(4.2) > JB MR2(4.3))
-----------------------------------------

### \[signature\]

  

> これはメーカー署名がないと使用出来ないもの

android.permission.BLUETOOTH\_STACK  
android.permission.ACCOUNT\_MANAGER  
android.permission.HARDWARE\_TEST  
android.permission.NET\_ADMIN  
android.permission.REMOTE\_AUDIO\_PLAYBACK  
android.permission.INTERACT\_ACROSS\_USERS\_FULL  
android.permission.GET\_DETAILED\_TASKS  
android.permission.REMOVE\_TASKS  
android.permission.START\_ANY\_ACTIVITY  
android.permission.SET\_SCREEN\_COMPATIBILITY  
android.permission.ACCESS\_ALL\_EXTERNAL\_STORAGE  
android.permission.FORCE\_STOP\_PACKAGES  
android.permission.SET\_PREFERRED\_APPLICATIONS  
android.permission.ASEC\_ACCESS  
android.permission.ASEC\_CREATE  
android.permission.ASEC\_DESTROY  
android.permission.ASEC\_MOUNT\_UNMOUNT  
android.permission.ASEC\_RENAME  
android.permission.DIAGNOSTIC  
android.permission.STATUS\_BAR\_SERVICE  
android.permission.FORCE\_BACK  
android.permission.INTERNAL\_SYSTEM\_WINDOW  
android.permission.MANAGE\_APP\_TOKENS  
android.permission.FREEZE\_SCREEN  
android.permission.INJECT\_EVENTS  
android.permission.FILTER\_EVENTS  
android.permission.RETRIEVE\_WINDOW\_INFO  
android.permission.TEMPORARY\_ENABLE\_ACCESSIBILITY  
android.permission.MAGNIFY\_DISPLAY  
android.permission.SET\_ACTIVITY\_WATCHER  
\+ android.permission.GET\_TOP\_ACTIVITY\_INFO  
android.permission.READ\_INPUT\_STATE  
android.permission.BIND\_INPUT\_METHOD  
android.permission.BIND\_ACCESSIBILITY\_SERVICE  
android.permission.BIND\_TEXT\_SERVICE  
android.permission.BIND\_VPN\_SERVICE  
android.permission.BIND\_DEVICE\_ADMIN  
android.permission.SET\_ORIENTATION  
android.permission.SET\_POINTER\_SPEED  
android.permission.SET\_KEYBOARD\_LAYOUT  
android.permission.CLEAR\_APP\_USER\_DATA  
android.permission.GRANT\_REVOKE\_PERMISSIONS  
android.permission.ACCESS\_SURFACE\_FLINGER  
android.permission.CONFIGURE\_WIFI\_DISPLAY  
android.permission.CONTROL\_WIFI\_DISPLAY  
android.permission.BRICK  
android.permission.DEVICE\_POWER  
android.permission.NET\_TUNNELING  
android.permission.FACTORY\_TEST  
android.permission.BROADCAST\_PACKAGE\_REMOVED  
android.permission.BROADCAST\_SMS  
android.permission.BROADCAST\_WAP\_PUSH  
android.permission.CONFIRM\_FULL\_BACKUP  
android.permission.CHANGE\_BACKGROUND\_DATA\_SETTING  
android.permission.GLOBAL\_SEARCH\_CONTROL  
android.permission.READ\_DREAM\_STATE  
android.permission.WRITE\_DREAM\_STATE  
android.permission.COPY\_PROTECTED\_DATA  
android.permission.MANAGE\_NETWORK\_POLICY  
android.intent.category.MASTER\_CLEAR.permission.C2D\_MESSAGE  
android.permission.BIND\_PACKAGE\_VERIFIER  
android.permission.ACCESS\_CONTENT\_PROVIDERS\_EXTERNALLY  
\+ android.permission.BIND\_NOTIFICATION\_LISTENER\_SERVICE  

  

両権限共に新規追加  
  

### \[signature|system\]

  

> メーカー署名があるか、プリインストールのシステムアプリでしか使用出来ないもの

  
\- android.permission.SEND\_SMS\_NO\_CONFIRMATION  
\+ android.permission.SEND\_RESPOND\_VIA\_MESSAGE  
android.permission.RECEIVE\_EMERGENCY\_BROADCAST  
android.permission.BIND\_DIRECTORY\_SEARCH  
android.permission.INSTALL\_LOCATION\_PROVIDER  
\+ android.permission.LOCATION\_HARDWARE  
android.permission.CONNECTIVITY\_INTERNAL  
android.permission.RECEIVE\_DATA\_ACTIVITY\_CHANGE  
\+ android.permission.LOOP\_RADIO  
android.permission.MANAGE\_USB  
android.permission.ACCESS\_MTP  
\+ android.permission.CAMERA\_DISABLE\_TRANSMIT\_LED  
android.permission.MODIFY\_PHONE\_STATE  
android.permission.READ\_PRIVILEGED\_PHONE\_STATE  
android.permission.WRITE\_MEDIA\_STORAGE  
android.permission.MANAGE\_USERS  
android.permission.SET\_TIME  
android.permission.WRITE\_GSERVICES  
android.permission.RETRIEVE\_WINDOW\_CONTENT  
android.permission.WRITE\_APN\_SETTINGS  
android.permission.ALLOW\_ANY\_CODEC\_FOR\_PLAYBACK  
android.permission.STATUS\_BAR  
android.permission.UPDATE\_DEVICE\_STATS  
\+ android.permission.UPDATE\_APP\_OPS\_STATS  
android.permission.SHUTDOWN  
android.permission.STOP\_APP\_SWITCHES  
android.permission.BIND\_WALLPAPER  
android.permission.INSTALL\_PACKAGES  
android.permission.DELETE\_CACHE\_FILES  
android.permission.DELETE\_PACKAGES  
android.permission.MOVE\_PACKAGE  
android.permission.CHANGE\_COMPONENT\_ENABLED\_STATE  
android.permission.READ\_FRAME\_BUFFER  
android.permission.REBOOT  
android.permission.MASTER\_CLEAR  
android.permission.CALL\_PRIVILEGED  
android.permission.PERFORM\_CDMA\_PROVISIONING  
android.permission.CONTROL\_LOCATION\_UPDATES  
android.permission.ACCESS\_CHECKIN\_PROPERTIES  
android.permission.PACKAGE\_USAGE\_STATS  
android.permission.BACKUP  
android.permission.BIND\_REMOTEVIEWS  
android.permission.BIND\_APPWIDGET  
android.permission.BIND\_KEYGUARD\_APPWIDGET  
android.permission.MODIFY\_APPWIDGET\_BIND\_PERMISSIONS  
android.permission.GLOBAL\_SEARCH  
android.permission.SET\_WALLPAPER\_COMPONENT  
android.permission.ACCESS\_CACHE\_FILESYSTEM  
android.permission.CRYPT\_KEEPER  
android.permission.READ\_NETWORK\_USAGE\_HISTORY  
android.permission.MODIFY\_NETWORK\_ACCOUNTING  
android.permission.PACKAGE\_VERIFICATION\_AGENT  
android.permission.SERIAL\_PORT  
\+ android.permission.ACCESS\_NOTIFICATIONS  

  

  
追加権限は全て新規追加、そして初めて権限の削除を見た。  
  
  

### \[system|signature\]

  

> \[signature|system\]と同じ

m android.permission.CHANGE\_CONFIGURATION  
android.permission.MOUNT\_UNMOUNT\_FILESYSTEMS  
android.permission.MOUNT\_FORMAT\_FILESYSTEMS  
  
ある意味変更無し、１権限だけ重複してた  \[signature|system|development\] にマージされる。  
  
  

###  \[signature|system|development\]

  

> メーカー署名、システムアプリ、もしくは開発中に使用出来るもの

android.permission.INTERACT\_ACROSS\_USERS  
android.permission.CHANGE\_CONFIGURATION  
android.permission.SET\_ANIMATION\_SCALE  
android.permission.WRITE\_SECURE\_SETTINGS  
android.permission.DUMP  
android.permission.READ\_LOGS  
android.permission.SET\_DEBUG\_APP  
android.permission.SET\_PROCESS\_LIMIT  
android.permission.SET\_ALWAYS\_FINISH  
android.permission.SIGNAL\_PERSISTENT\_PROCESSES  
\+ android.permission.GET\_APP\_OPS\_STATS  

  

新規追加のみ  
  
  

### \[signatureOrSystem\]

  

> \[signature|system\]と同じ

  
android.permission.UPDATE\_LOCK  
  
特に変化なし（これもどっかにマージして欲しい）