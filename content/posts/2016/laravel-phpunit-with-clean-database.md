---
title: 'Laravel :: phpunit with clean database.'
date: 2016-07-21T17:50:00.001+09:00
draft: false
tags : [sqlite, laravel, phpunit, PostgreSQL]
---

Laravel + postgresSQLを使ったサイトで unit test を書いてたが、既存のデータベースを使うと、テストが意図しない挙動になることがあったので、汚れていないDBを使いたくなったので、調べてやってみたら、意外と詰まってしまったという話。

*   [環境](#環境)
*   [sqlite in memory database を使う方法](#sqlite-in-memory-database-を使う方法)
    *   [config/database.php](#configdatabasephp)
    *   [config/database.php](#configdatabasephp-1)
    *   [phpunit.xml](#phpunitxml)
    *   [TestCase.php](#testcasephp)
*   [Sqliteでエラーがでる場合の対処1](#sqliteでエラーがでる場合の対処1)
    *   [Driver not found](#driver-not-found)
    *   [ALTER TABLE SYNTAX ERROR](#alter-table-syntax-error)
*   [Sqliteでエラーがでる場合の対処2](#sqliteでエラーがでる場合の対処2)

環境
==

*   laravel 5.x
*   PostgreSQL

sqlite in memory database を使う方法
===============================

config/database.php
-------------------

環境変数で default 値を差し替えれるようにする

```
'default' => env('DB_DEFAULT', 'pgsql'),
```

config/database.php
-------------------

memory database の定義を作る

```
'sqlite_testing' => [  
    'driver'   => 'sqlite',  
    'database' => ':memory:',  
    'prefix'   => '',  
],
```

phpunit.xml
-----------

環境変数追加。環境変数を与える方法は別に何でも良い。

```
~~~~~~~~~~~~~  
        <env name="DB_DEFAULT" value="sqlite_testing"/>  
    </php>  
</phpunit>
```

TestCase.php
------------

都度migrateをするようにする。

```
 public function setUp()  
  {  
      parent::setUp();  
  
      $this->artisan('migrate');  
      $this->artisan('db:seed');  
  }  
  
  public function tearDown()  
  {  
      $this->artisan('migrate:reset');  
  }
```

これで上手くいく人は上手くいく。

* * *

Sqliteでエラーがでる場合の対処1
===================

Driver not found
----------------

```
[Symfony\Component\Debug\Exception\FatalErrorException]  
Class 'Doctrine\DBAL\Driver\PDOSqlite\Driver' not found
```

が出たら。

cmposer に

```
"doctrine/dbal": "^2.5"
```

ALTER TABLE SYNTAX ERROR
------------------------

さらにエラーが出る。  
ALTER TABLE が syntax エラーと migration 中に出る。

ここからヒントをもらう。

*   [SQLite migration ALTER TABLE not working \[laracasts.com\]](https://laracasts.com/index.php/discuss/channels/testing/sqlite-migration-alter-table-not-working)

以下のスレッドの中で、[SQL Features That SQLite Does Not Implement \[sqlite.org\]](http://www.sqlite.org/omitted.html) を参照。つまり、sqliteで実装されていないので、エラーになっている。

ここを参考に、

*   [How to migrate a testing database in Laravel 5? \[laracasts.com\]](https://laracasts.com/discuss/channels/general-discussion/how-to-migrate-a-testing-database-in-laravel-5)

エラーがでない内容の migration だけを行い、  
そのsqlite file をテスト前にコピーして、テスト後破棄するというもの。

少々面倒。

また以下問題も見つかる。

*   [drop and add column of a table in one migration #2694 \[github.com\]](https://github.com/laravel/framework/issues/2694)

migration 中にエラーが出たら、エラーが出たファイルを消して、migration を終了させた後、テストを流してみたが、特定のカラムが無いというエラーが起きた。  
一つの migration ファイルの中で、**ADD COLUMN** と **DROP COLUMN** 両方を入れているとエラーにならず、追加もされない。

Sqliteでエラーがでる場合の対処2
===================

sqlite を諦め、PostgreSQL に一時的な testdb を作成し、  
そちらでテストを行い、終了後は drop database する。

script を書きそれを実行した。

```
psql -U postgres -c "CREATE DATABASE testdb"  
php artisan migrate --database=pgsql_testing  
php artisan db:seed --database=pgsql_testing  
phpunit -c phpunit.xml "$@"  
psql -U postgres -c "DROP DATABASE testdb"
```

これでようやく上手くいった。