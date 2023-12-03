---
title: 'Docker registry を構築した後のimage整理'
date: 2016-04-04T12:38:00.001+09:00
draft: false
tags : [docker, bash, 技術, docker registry]
---

Docker registry を作って、別チームに任せて放置する
---------------------------------

Docker registry で image 管理をすると段々とゴミが溜まってきます。API([https://docs.docker.com/v1.6/reference/api/registry\_api/#delete-a-repository](https://docs.docker.com/v1.6/reference/api/registry_api/#delete-a-repository))で削除できるのはTAGがついているimageだけなので、  
TAGが外れているimagesがどんどん残っていきます。

エラーが起きる
-------

ずーっと管理せずに放置していると、ある日こんなエラーと出会います。

```
HTTP code 500 while uploading metadata: "invalid character '<' looking for beginning of value"
```

これは、message push しようとしたり、する必要があるかをregistryに確認したところ、正常なjsonレスポンスではなく、htmlのエラーページが帰ってきたため起きたエラーです。

不要なimageを削除する。
--------------

以下スクリプとが非常に有用です。  
jqのインストールが必須になります。

[kwk/remove-orphan-images.sh](https://gist.github.com/kwk/c5443f2a1abcf0eb1eaa)  
[https://gist.github.com/kwk/c5443f2a1abcf0eb1eaa](https://gist.github.com/kwk/c5443f2a1abcf0eb1eaa)

追記:実行時のエラー
----------

私の場合、実行時に下記エラーが出ました。

```
parse error: Invalid numeric literal at line 144, column 114
```

これは直前に表示されたrepository名のindexファイルが破損していたため、起きた現象でした。手修正でindexファイルを修正したところ、うまく動きました。