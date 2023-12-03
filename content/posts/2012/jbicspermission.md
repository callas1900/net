---
title: 'JBとICSのPermission比較（メーカー署名関係）'
date: 2012-08-13T09:00:00.000+09:00
draft: false
tags : [JB, signature, ICS, Android]
---

以前書いた、[ICSとGingerbreadのPermission比較](http://blog.callas1900.net/2011/11/icsgingerbreadpermission.html)（メーカー署名関係）の続編。  
  
  

> 注意：今回の記事は https://android.googlesource.com/platform/manifest/android-4.1.1\_r4 を元に書いてます。

  
またしてもJBで色々と Permission 関係が変わっているのでまとめてみた。  
まず プロテクションレベルの表記が変わっている。  
以前は signatureOrSystem と書かれていた箇所が signature|system に変更。  
また謎の development も追加（詳細がドキュメントされていないので後日調査予定）  
  
まず ICS と ＪＢ のプロテクションレベルの一覧比較  
  
  
**ICS**  
  

*   dangerous
*   signatureOrSystem
*   normal
*   signature

  
**JB**  
  

*   dangerous
*   signature|system
*   normal
*   signature
*   signature|system|development
*   **signatureOrSystem**

  
JB に signatureOrSystem が混じっているのは誤表記にあらず。  
一個だけ何故か（恐らくミスだと思うけど） signatureOrSystem が混ざっている。  
  
次それぞれのプロテクションレベル毎の比較  
JB 方式の書き方だと今回はまとめにくいので、ICS方式で signature と signatureOrSystemでまとめてみる。  
  

**\[signature\]**
-----------------

> 赤字は追加分、新規追加のみ signatureOrSystem からの格上げなし

android.permission.ACCOUNT\_MANAGER  
android.permission.HARDWARE\_TEST  
android.permission.NET\_ADMIN  
**android.permission.REMOTE\_AUDIO\_PLAYBACK**  
**android.permission.GET\_DETAILED\_TASKS**  
android.permission.REMOVE\_TASKS  
**android.permission.START\_ANY\_ACTIVITY**  
**android.permission.SET\_SCREEN\_COMPATIBILITY**  
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
android.permission.INJECT\_EVENTS  
android.permission.SET\_ACTIVITY\_WATCHER  
android.permission.READ\_INPUT\_STATE  
android.permission.BIND\_INPUT\_METHOD  
**android.permission.BIND\_ACCESSIBILITY\_SERVICE**  
android.permission.BIND\_TEXT\_SERVICE  
android.permission.BIND\_VPN\_SERVICE  
android.permission.BIND\_DEVICE\_ADMIN  
android.permission.SET\_ORIENTATION  
android.permission.SET\_POINTER\_SPEED  
**android.permission.SET\_KEYBOARD\_LAYOUT**  
android.permission.CLEAR\_APP\_USER\_DATA  
**android.permission.GRANT\_REVOKE\_PERMISSIONS**  
android.permission.ACCESS\_SURFACE\_FLINGER  
android.permission.BRICK  
android.permission.DEVICE\_POWER  
android.permission.FACTORY\_TEST  
android.permission.BROADCAST\_PACKAGE\_REMOVED  
android.permission.BROADCAST\_SMS  
android.permission.BROADCAST\_WAP\_PUSH  
android.permission.CONFIRM\_FULL\_BACKUP  
android.permission.CHANGE\_BACKGROUND\_DATA\_SETTING  
android.permission.GLOBAL\_SEARCH\_CONTROL  
android.permission.COPY\_PROTECTED\_DATA  
android.permission.MANAGE\_NETWORK\_POLICY  
android.intent.category.MASTER\_CLEAR.permission.C2D\_MESSAGE  
android.permission.BIND\_PACKAGE\_VERIFIER  
**android.permission.ACCESS\_CONTENT\_PROVIDERS\_EXTERNALLY**  
  

\[signatureOrSystem\]
---------------------

> 赤字新規追加、青字は削除。  
> ただし\[signature|system|development\]への移動だから除外というのは当てはまらないかも。

android.permission.SEND\_SMS\_NO\_CONFIRMATION

android.permission.RECEIVE\_EMERGENCY\_BROADCAST  
android.permission.INSTALL\_LOCATION\_PROVIDER  
android.permission.CONNECTIVITY\_INTERNAL  
android.permission.MANAGE\_USB  
android.permission.ACCESS\_MTP  
android.permission.MODIFY\_PHONE\_STATE  
android.permission.READ\_PRIVILEGED\_PHONE\_STATE  
android.permission.WRITE\_MEDIA\_STORAGE  
**android.permission.WRITE\_SECURE\_SETTINGS**  
android.permission.WRITE\_GSERVICES  
**android.permission.DUMP**  
android.permission.RETRIEVE\_WINDOW\_CONTENT  
android.permission.SET\_TIME  
android.permission.WRITE\_APN\_SETTINGS  
android.permission.ALLOW\_ANY\_CODEC\_FOR\_PLAYBACK  
android.permission.STATUS\_BAR  
android.permission.UPDATE\_DEVICE\_STATS  
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
**android.permission.MODIFY\_APPWIDGET\_BIND\_PERMISSIONS**  
android.permission.GLOBAL\_SEARCH  
android.permission.SET\_WALLPAPER\_COMPONENT  
android.permission.ACCESS\_CACHE\_FILESYSTEM  
android.permission.CRYPT\_KEEPER  
android.permission.READ\_NETWORK\_USAGE\_HISTORY  
android.permission.MODIFY\_NETWORK\_ACCOUNTING  
android.permission.PACKAGE\_VERIFICATION\_AGENT  
android.permission.WRITE\_SECURE\_SETTINGS  
android.permission.DUMP  
  

その他
---

今回新規追加のプロテクションレベル signature|system|development と 仲間はずれの signatureOrSystem  
  

### \[signature|system|development\]

> 青字の二つは signatureOrSystem からそれ以外は dangerous からの格上げ、これのおかげで開発補助系のアプリに影響が出まくる。

android.permission.SET\_ANIMATION\_SCALE

**android.permission.WRITE\_SECURE\_SETTINGS**

**android.permission.DUMP**

android.permission.READ\_LOGS

android.permission.SET\_DEBUG\_APP

android.permission.SET\_PROCESS\_LIMIT

android.permission.SET\_ALWAYS\_FINISH  
  

### \[signatureOrSystem\]

> 一個だけぽつんとあるミスっぽいやつ。変換ミスかと思ったが以前は無かったものなのでその線は薄いか？内容的に Nexus 7 作った ASUS で足したものかもしれない。

android.permission.UPDATE\_LOCK

  

  

今回は以上

情報追加次第、色々手出して調べてみます。