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

以上になります。
