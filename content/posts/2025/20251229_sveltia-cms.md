---
title: Sveltia CMS 導入
slug: sveltia-cms
date: 2025-12-29T12:55:00
description: hugo + github pages に sveltia cms の導入をした話
tags:
  - hugo
  - sveltiacms
  - github
draft: false
---
このサイトは Hugo で作成されていて、静的サイトを生成した後は、github pagesに公開されている状態です。今までは、ローカルでgit repositoryをcloneした状態からpushしてのみ更新していましたが、ちょっと面倒になってきたのでヘッドレスCMSの導入を試みました。

## 選定 
いくつかの候補がありましたが、 sveltia CMSがメンテナンスやアップデートも盛んなので候補にあがりました。

## 認証のためのcallbackのためのサービス
sveltia CMSの仕組みはシンプルで、 index.html と config.yml でのみ構成されています。

問題は認証方式ですが、github の oauthを使用します。

ここで、oauthからのcallbackの受け先サーバーが必要なのですが、検索したところ netlify と cloudflare works が候補にあがりました。一度 netlify で試してみたのですが、途中で詰まってしまったので、 Sveltia CMS が提供している svelitia-cms-auth を使用することにしました。結果 cloudflare worksを使用することに。

## 手順
手順は sveltia-cms-auth に詳しく書いているので、詳しくは書きません。

1. index.html を設置
2. config.yml を設置
3. sveltia-cms-auth のページから cloudflare works にデプロイ
4. Github::Developers SettingからAuth Appを設定し、IDとSECRETを入手
5. cloudflare worksに戻り、IDとSECRETを設定

参考までに以下に私の設定したconfig.ymlを置いておきます。  
使用する場合は適時値を変更してご使用下さい。


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
