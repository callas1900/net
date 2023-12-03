---
title: 'Smaller APKs : Android におけるAPKを小さく保つためのテクニック'
date: 2016-11-10T02:06:00.001+09:00
draft: false
tags : [Android]
---

Android Performance Patterns Session にいい動画が上がっていたので、備忘録として中身を書き出しておく

*   [Removing Unused Resources](#removing-unused-resources)
*   [Multi Resources Support](#multi-resources-support)
*   [Vector Drawables](#vector-drawables)
*   [Reuse Existing Resources](#reuse-existing-resources)
*   [Removing Unused Code](#removing-unused-code)
*   [Apk Analyzer](#apk-analyzer)

Removing Unused Resources
=========================

gradle file にて以下の `minifyEnabled` と `shrinkResources` をセットしておく。

```
android {  
    ...  
    buildTypes {  
        release {  
            minifyEnabled true  
            shrinkResources true  
            proguardFiles getDefaultProguardFile('proguard-android.txt'),  
            'proguard-rules.pro'  
        }  
    }  
}
```

これらはアプリ内で使用していないリソースを除去してくれます。

Multi Resources Support
=======================

Android がサポートしているリソースサイズを全て揃えるとそれだけで結構な量になるので、必要なものだけ使う。

ldpi

mdpi から自動で作られる

mdpi

tvdpi

使わない

hdpi

xxhdpi から自動で作られる

xhdpi

xxhdpi から自動で作られる

xxhdpi

xxxhdpi

*   mdpi
*   xxhdpi
*   xxxhdpi

のみ使用する

Vector Drawables
================

PNG や JPEGの代わりに vector 画像を使うようにする。

Reuse Existing Resources
========================

可能であれば画像の再利用を行う、  
例えば、下向きの矢印を上向き矢印に変更するなど。 他にもAndroid の機能を使って、以下のものを変更できる。

*   color tint(色味)
*   shapes(形)

Removing Unused Code
====================

*   ProGuard を使う
*   ProGuard を使う時は、`minifyEnabled true` を使って ProGuard の仕事量を減らす。
*   必要なライブラリの軽いバージョンを見つける、どうしてもない場合は必要な箇所のソースだけ抜いてくる。

Apk Analyzer
============

Android Studio 2.2 から搭載された apk analyzer を使う。