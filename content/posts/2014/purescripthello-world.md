---
title: 'PureScriptでHello world'
date: 2014-10-14T12:44:00.001+09:00
draft: false
---

関数型言語系の本山（と思ってる）Haskell を勉強したいけど、  
折角勉強しても使い道を思いつかなかった時に PureScript を知る。  
  
PureScript は Haskell -> Javascript のコンパイラ。  
正しくは Haskell "風"らしいが、最終系は Haskell になるのだろ。  
  
Mac 上で Hello world してみる。  
まず Cabal をインストールする（ Cabal は Haskell のパッケージシステム）。  
ついでに実行環境用に node もインストール  
  
```
brew install ghc cabal-install node
```  
次に PureScript のインストール  
  
```
psc --main=Main hello.purs > hello.js
```  
もし psc と打ち込んでもTerminalが反応しなかったら以下のようにパスを通す。  
  
```
export PATH="$HOME/.cabal/bin:$PATH"
```  
Hello world を書く。ファイル名は hello.purs とする。  
  
```
module Main where  
import Debug.Trace  
main = trace "Hello, PureScript!"
```  
コンパイル  
  
```
cabal update  
cabal install purescript
```  
実行  
  
```
node hello.js  
  
> Hello, PureScript!
```  
  
参考：  
PureScript::Getting Started  
http://purescript.readthedocs.org/en/latest/start.html  
  
PureScript::Hello, PureScript!  
http://purescript.readthedocs.org/en/latest/intro.html#hello-purescript