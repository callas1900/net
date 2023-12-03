---
title: '臆病者のための Ansible'
date: 2016-01-12T01:06:00.000+09:00
draft: false
tags : [serverside, 技術, Ansible]
---

*   [Target](#target)
*   [Links](#links)
*   [臆病者のための確認コマンド](#臆病者のための確認コマンド)
    *   [基本](#基本)
    *   [確認 hosts](#確認-hosts)
    *   [制限 hosts](#制限-hosts)
    *   [確認 tasks](#確認-tasks)
    *   [確認 最終](#確認-最終)
*   [〆](#〆)

Target
======

Ansible を使ってみてその便利さに驚愕するとともに、他人が作ったPlaybookを引き継ぐ怖さも知る。  
全て手順書のように書いていればいいのだが、多数のRoleを使い高度に書かれたAnsible playbookを引き継ぎ、メンテまたは代わりに実行するのはとても怖い。  
playbook実行する前に何がどうなるのか確認しまくりたい。

そんな自分のための初心者ガイド

Links
=====

実行の仕方など基礎的な事は公式ドキュメント参照

Hello world  
[http://docs.ansible.com/ansible/intro\_getting\_started.html](http://docs.ansible.com/ansible/intro_getting_started.html)

どうやって使うかのオススメ、ディレクトリ配置など  
[http://docs.ansible.com/ansible/playbooks\_best\_practices.html](http://docs.ansible.com/ansible/playbooks_best_practices.html)

確認コマンド
======

playbook は実行前に色々確認したいですよね。

基本
--

```
ansible-playbook playbook.yml
```

これで playbook が実行されます、設定がしっかりしてる環境であれば、外部サーバに実際に変更を行ったり、時には取り返しのつかない変更が実行されたりします。何も考えずに実行するのは危険

確認 hosts
--------

```
ansible-playbook playbook.yml --list-hosts
```

playbook は実行されません。  
playbookが実行される相手先をリストアップするだけです。  
host は hosts ファイルなどで定義された ansible のためのサーバー接続先設定のことです。

制限 hosts
--------

```
ansible-playbook playbook.yml -l hoge --list-hosts
```

`-l` の後に host 名もしくは hostgroup 名を入力すれば playbook の接続先を制限することができます。 `--list-hosts` と組み合わせると捗ります。

確認 tasks
--------

```
ansible-playbook playbook.yml --list-task
```

playbook は実行されません。  
各タスクの`-name`箇所が実行順番通りに列挙されます。  
`-name`をきちんと書いておけばきっちり確認になります。

私は気になる箇所は 出力内容で grep 検索しています。

確認 最終
-----

```
ansible-playbook playbook.yml -CD
```

playbook は実行されません。  
`-CD` は `-C, --check`, `-D, --diff` の合成です。  
二つ同時に実行したほうが効果的です。  
playbook は実行されませんが、実際に各 host に接続し、  
実際に実行した際のファイル差分（あれば）が表示されます。

playbook の構成によってはエラーになりますが、内容をよく見て本当にエラーか確認してください。  
例えば以下手順は playbook が正常であっても、エラーになります。

1.  ansible がファイルAを消す
2.  ansible がファイルAがないことを確認する

実際にはファイルAは消されていないので手順2でエラーになります。

また、さらに詳細に内容がみたい場合は以下実行して下さい

```
ansible-playbook playbook.yml -CD -vvvv
```

> \-v, –verbose verbose mode (-vvv for more, -vvvv to enable  
> connection debugging)

〆
=

では良いAnsibleライフを