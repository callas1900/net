---
title: 'Android 5.0.2 以上でBLEが動かない'
date: 2016-02-03T22:48:00.001+09:00
draft: false
tags : [Bluetooth, BLE, 技術, Android]
---

*   [Occurrence -事象-](#occurrence-事象)
*   [Causes -原因-](#causes-原因)
    *   [HID とは ?](#hid-とは)
    *   [BLUETOOTH\_PRIVILEGED とは?](#bluetoothprivileged-とは)
*   [Summary -まとめ-](#summary-まとめ)
    *   [HID を使ってるかの判断](#hid-を使ってるかの判断)
    *   [禁止された Characteristic UUID](#禁止された-characteristic-uuid)
    *   [なぜ禁止されたのか？](#なぜ禁止されたのか)

Occurrence -事象-
===============

機材とAndroid を BLE (Bluetooth low energy) で繋ごうとしたところ、Android 5.0.2以上の端末で Security Exception が発生した。  
5.0.1 や 4.2 などは問題ないが、5.1や6.0で発生する。

エラー内容は以下のようになっている。

```
java.lang.SecurityException: Need BLUETOOTH_PRIVILEGED permission: Neither user 99999 nor current process has android.permission.BLUETOOTH_PRIVILEGED.
```

発生箇所は BluetoothGatt#setCharacteristicNotification

Causes -原因-
===========

StackOverflow にほぼ発生事例そのままの報告がある、  
[  
Android 5.0.2 onwards don’t allow HID access through Bluetooth LE  
](http://stackoverflow.com/questions/30579580/android-5-0-2-onwards-dont-allow-hid-access-through-bluetooth-le)

さらに、Android Issues に [\[BLE\] Reading/writing char/descr of a HID service throws an exception](https://code.google.com/p/android/issues/detail?id=174870) があり、その中で

> “Enforce BLUETOOTH\_PRIVILEGED permission for HID-over-GATT”

のメッセージのコミットが原因でHIDに対する GATTのコネクションに **BLUETOOTH\_PRIVILEGED** が要求されるようになったと書かれている。

HID とは ?
--------

HID（Human Interface Device）のことで、  
マウスやキーボードなどの入力装置を無線化するためのBluetooth用のプロファイル。  
本来上記の通り、マウスキーボードなどに使われるものだが、健康器具などにも使われているケースがある。確かに人が使うものだけど。

BLUETOOTH\_PRIVILEGED とは?
-------------------------

Android Developers によれば、

> Allows applications to pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access. This is not available to third party applications.

HIDに関係ありそうなのは、メッセージに対するアクセスかな？  
全然HIDと関係なさそうに見える。  
ただ一番大事なのは最後のサードパーティアプリはこれを有効に出来ないという一文。  
ビルドインアプリを開発するか、OSのビルド署名を貰えるようなアプリ開発の時は問題ないが、普通にアプリを作っている場合は、この権限を有効化する方法はない。

see also [AndroidDevelopers::Manifest.permission::BLUETOOTH\_PRIVILEGED](http://developer.android.com/reference/android/Manifest.permission.html#BLUETOOTH_PRIVILEGED)

Summary -まとめ-
=============

HID を使ってるかの判断
-------------

以下のコミットによると、HIDの判断は, Characteristic UUID が  
[https://android.googlesource.com/platform/packages/apps/Bluetooth/+/02bebee](https://android.googlesource.com/platform/packages/apps/Bluetooth/+/02bebee)

```
00002A4A-0000-1000-8000-00805F9B34FB  
00002A4B-0000-1000-8000-00805F9B34FB  
00002A4C-0000-1000-8000-00805F9B34FB  
00002A4D-0000-1000-8000-00805F9B34FB
```

のいずれかに該当した場合となる。

上記 Characteristic を引数にしてい BluetoothGatt#setCharacteristicNotification をコールすると SecurityException が発生するようになっている。

禁止された Characteristic UUID
-------------------------

Bluetooth Developer portal で Characteristic UUID の区分け確認できる。

Characteristic UUID

内容

00002A4A-0000-1000-8000-00805F9B34FB

HID Information

00002A4B-0000-1000-8000-00805F9B34FB

Report Map

00002A4C-0000-1000-8000-00805F9B34FB

HID Control Point

00002A4D-0000-1000-8000-00805F9B34FB

Report

see also [Bluetooth Developer portal : Characteristics](https://developer.bluetooth.org/gatt/characteristics)

なぜ禁止されたのか？
----------

わからない。  
結論から言うとわからない。なんらかのバグ修正としてコミットされているが、  
どのような背景があるのかはわからなかった。