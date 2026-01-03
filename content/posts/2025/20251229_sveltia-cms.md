---
title: Sveltia CMS 導入
slug: sveltia-cms
date: 2025-12-29T12:55:00
cover: /img/pexels-tolga-deniz-aran-35431759.jpg
tags:
  - hugo
  - sveltia-cms
description: hugo + github pages の本サイト に sveltia cms の導入をした話
draft: false
---
## 状況説明

このブログサイトは [Hugo](https://gohugo.io/) で作成されています。実際のweb pageの生成順番としては、

1. local で clone したrepository を更新
2. github に push
3. github actions で html生成とgithub pagesにアップロード

更に、実際には記事のレンダリング状況を確認するために hugo serve でローカルで確認してからの作業になります。

### 課題

更新をする時の環境設定が重い。出先でのラップトップや、スマホで更新することが難しい。

### 目的

現在の構成をほぼ変えずに、CMSの導入ができるか検討する

# Sveltia CMS 導入

## 選定

いくつかの候補がありましたが、 [Sveltia CMS](https://github.com/sveltia/sveltia-cms)  がメンテナンスやアップデートも盛んなので筆頭候補になりました。

## 導入前実験

**認証のためのcallbackのためのサービス**
Sveltia CMSの仕組みはシンプルで、 `index.html` でjavascriptをロードして、CMSを構成、 `config.yml` から設定を読み込みしています。これで任意のURLを叩けばCMSを使えます。さらに認証は、githubの oauth を使用しています。ここで、oauthからのcallbackの受け先サーバーが必要で、以下の候補があります。

* Netlify
* Cloudflare works

Netlifyを試したところ、認証のポップアップの戻りの部分でうまくいかず、Sveltia CMS が提供している [svelitia-cms-auth](https://github.com/sveltia/sveltia-cms-auth) を使用することにしました。結果 、cloudflare worksを使用することに。

## 導入手順

### 1. index.html を設置

Sveltia CMS  は Decap CMS から派生しているので、インストールの参考情報は Decap 側にあります。
参考：https://decapcms.org/docs/install-decap-cms/
参考情報から、 `static/admin/index.html`  を設置その後、javascriptロード を `<script src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"></script>` に書き換える。

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Sveltia CMS</title>
    <script
      src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"
      onload="SVELTIA.start()"
      onerror="document.body.innerHTML='Failed to load Sveltia CMS'"
    ></script>
    <link href="/admin/config.yml" type="application/yaml" rel="cms-config-url" />
  </head>
  <body></body>
</html>
```

### 2. config.yml を暫定設置

`static/admin/config.yml`　を暫定設置
中身は以下の要件に従っています。

* `content/posts/YYYY/YYYYMMDD_slug` でファイル保存されること
* fields 以下は私の投稿に合わせて変更
(さらに変更したい人は sveltia-cms::widget情報を参照して下さい。)

```yml
backend:
  name: github
  repo: yourgithub/site
  branch: main
  base_url: https://sveltia-cms-auth.yourdomain.workers.dev
  auth:
    client_id: Xx00XxxxX0xXXXxXXxxX

media_folder: "static/posts"
public_folder: "/posts"

collections:
    - name: "posts"
    label: "Blog Posts"
    folder: "content/posts"
    path: "{{year}}/{{year}}{{month}}{{day}}_{{fields.slug}}"
    create: true
    extension: "md"
    format: "yaml-frontmatter"
    fields:
            - label: "Title"
        name: "title"
        widget: "string"
            - label: "Slug"
        name: "slug"
        widget: "string"
        required: true
            - label: "Date"
        name: "date"
        widget: "datetime"
            - label: "Description"
        name: "description"
        widget: "text"
        required: false
            - label: "Cover Image"
        name: "cover"
        widget: "image"
        required: false
            - label: "Tags"
        name: "tags"
        widget: "list"
        required: false
            - label: "Draft"
        name: "draft"
        widget: "boolean"
        default: true
            - label: "Body"
        name: "body"
        widget: "markdown"
```

### 3. sveltia-cms-auth を cloudflare works にデプロイ

1. Cloudflare のアカウントを持ってない人は作成
2. https://github.com/sveltia/sveltia-cms-auth?tab=readme-ov-file#how-to-use-it にある、`Deploy to Cloudflare` ボタンをクリック
3.Deploy 終了後に、 worker の URLを取得（画面上部にある `sveltia-cms-auth.{{YOUR_ID}}.workers.dev`  方式のもの）

### 4. Github Auth App を設定

1. Githubの右上アイコンから Setting を選択
2. 左カラムの下部にあるDeveloper Settingsを選択
3. OAuth Appsを選択
4. New OAuth App を選択後、

* Application name = `Sveltia CMS`
* Homepage URL = `https://callas1900.net`
* Authorization callback URL = `sveltia-cms-auth.{{YOUR_ID}}.workers.dev/callback` （worker URLに /callasback 追加したもの)

5. CLIENT_IDとCLIENT_SECRETを保管

### 5. IDとSECRETの設定

1. config.ymlファイルのclient_idをCLIENT_IDで更新
2. cloudflare worksのSettingからVariables and Secretsのセクションに以下を追加

* GITHUB_CLIENT_IDをCLINET_IDをPlaintext Typeで追加
* GITHUB_CLIENT_SECRETをCLIENT_SECRETをSecret Typeで追加
