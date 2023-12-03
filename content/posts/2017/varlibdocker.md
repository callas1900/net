---
title: '/var/lib/docker の移動'
date: 2017-01-25T01:20:00.000+09:00
draft: false
tags : [Linux, docker, ubuntu16]
---

docker のホストマシン容量不足対策。

docker をインストール後稼働していると、ディスクが足りなくなることがあります。  
いらないイメージを削ればいいのですが、イメージが削れない状況もあると思います。  
外部ディスクマウント後の容量食う /var/lib/docker の移動の仕方に関して記します。

*   [docker 停止](#docker-停止)
*   [/var/lib/docker を移す](#varlibdocker-を移す)
*   [設定ファイル変更](#設定ファイル変更)
    *   [redhat系の場合](#redhat系の場合)
    *   [debian系の場合](#debian系の場合)
    *   [ubuntu 16 の場合](#ubuntu-16-の場合)
*   [docker 再起動 & 確認](#docker-再起動-確認)

docker 停止
=========

```
sudo service docker stop
```

/var/lib/docker を移す
===================

ディスク容量に余裕がある場所に /var/lib/docker を移す。(ここでは例として `/mnt/extra/docker` とする)  
インストール直後ぐらいなら、`mv` で、  
安全にやりたいなら

```
mkdir /mnt/extra/docker  
sudo rsync -aXS /var/lib/docker/. /mnt/extra/docker/
```

設定ファイル変更
========

redhat系の場合
----------

設定ファイル: /etc/sysconfig/docker  
(あれば追加で、なければ作成)

```
echo other_args="-g /mnt/extra/docker" > /etc/sysconfig/docker
```

debian系の場合
----------

設定ファイル: /etc/default/docker

```
# DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4"  
DOCKER_OPTS="-dns 8.8.8.8 -dns 8.8.4.4 -g /mnt/extra/docker"
```

と書かれていますが、手前の ubuntu 16 では動きませんでしたので

ubuntu 16 の場合
-------------

設定ファイル: /lib/systemd/system/docker.service

```
# ExecStart=/usr/bin/dockerd -H fd://  
ExecStart=/usr/bin/dockerd -g /mnt/extra/docker -H fd://
```

その後、

```
sudo systemctl daemon-reload
```

docker 再起動 & 確認
===============

```
sudo service docker start
```

確認は

```
docker info
```

の `Root Dir:` の項目を見れば良い