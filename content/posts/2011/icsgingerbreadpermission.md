---
title: 'ICSとGingerbreadのPermission比較（メーカー署名関係）'
date: 2011-11-28T13:45:00.001+09:00
draft: false
tags : [Gingerbread, signature, ICS, Android]
---

ICSのテストをしていると、前まで動いていたところでSecurityExceptionをはきました。  
端末不具合かソースが変わったのかを調べる為に  
公開されているICS(Android 4.0)とGingerbread(Android 2.3.3)のAndroidManifest.xmlを比較してみました。  
  

> AndroidではAndroid自体をビルドする時に使用されている署名（所謂メーカー所有の署名）とその他の署名の間に格差があり、特定のAPIを叩く際に必要となるpermissionの値が、"signatureOrSystem" もしくは"signature"となっている時は、実行する為にこのメーカー署名が必要となります。  
>   
> それらAPIを叩くためには、メーカーに依頼して出来たAPKに署名を入れてもらうか、  
> rootを取る、もしくは自分でAndroidをビルドして実機に焼く等を行う必要があります。

  
それぞれ、frameworks/base/core/res/AndroidManifest.xml  
を比較し、ICSで増えた箇所を赤字＋太字で表示しました。  
※ICSで減ったものはなかった。  
  
**\[signatureOrSystem\]**  
**android.permission.SEND\_SMS\_NO\_CONFIRMATION**  
**android.permission.RECEIVE\_EMERGENCY\_BROADCAST**  
android.permission.INSTALL\_LOCATION\_PROVIDER  
**android.permission.CONNECTIVITY\_INTERNAL**  
android.permission.MANAGE\_USB  
**android.permission.ACCESS\_MTP**  
android.permission.MODIFY\_PHONE\_STATE  
**android.permission.READ\_PRIVILEGED\_PHONE\_STATE**  
**android.permission.WRITE\_MEDIA\_STORAGE**  
android.permission.WRITE\_SECURE\_SETTINGS  
android.permission.WRITE\_GSERVICES  
android.permission.DUMP  
**android.permission.RETRIEVE\_WINDOW\_CONTENT**  
android.permission.SET\_TIME  
**android.permission.WRITE\_APN\_SETTINGS**  
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
**android.permission.BIND\_REMOTEVIEWS**  
android.permission.BIND\_APPWIDGET  
android.permission.GLOBAL\_SEARCH  
android.permission.SET\_WALLPAPER\_COMPONENT  
android.permission.ACCESS\_CACHE\_FILESYSTEM  
**android.permission.CRYPT\_KEEPER**  
**android.permission.READ\_NETWORK\_USAGE\_HISTORY**  
**android.permission.MODIFY\_NETWORK\_ACCOUNTING**  
**android.permission.PACKAGE\_VERIFICATION\_AGENT**  
  
**\[signature\]**  
android.permission.ACCOUNT\_MANAGER  
android.permission.HARDWARE\_TEST  
**android.permission.NET\_ADMIN**  
**android.permission.REMOVE\_TASKS**  
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
**android.permission.BIND\_TEXT\_SERVICE**  
**android.permission.BIND\_VPN\_SERVICE**  
android.permission.BIND\_DEVICE\_ADMIN  
android.permission.SET\_ORIENTATION  
**android.permission.SET\_POINTER\_SPEED**  
android.permission.CLEAR\_APP\_USER\_DATA  
android.permission.ACCESS\_SURFACE\_FLINGER  
android.permission.BRICK  
android.permission.DEVICE\_POWER  
android.permission.FACTORY\_TEST  
android.permission.BROADCAST\_PACKAGE\_REMOVED  
android.permission.BROADCAST\_SMS  
android.permission.BROADCAST\_WAP\_PUSH  
**android.permission.CONFIRM\_FULL\_BACKUP**  
android.permission.CHANGE\_BACKGROUND\_DATA\_SETTING  
android.permission.GLOBAL\_SEARCH\_CONTROL  
android.permission.COPY\_PROTECTED\_DATA  
**android.permission.MANAGE\_NETWORK\_POLICY**  
android.intent.category.MASTER\_CLEAR.permission.C2D\_MESSAGE  
**android.permission.BIND\_PACKAGE\_VERIFIER**