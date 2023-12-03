---
title: '[ANT][Eclipse][Weblogic]ANTのタスクでこける時の対処'
date: 2007-10-23T22:30:00.002+09:00
draft: false
tags : [Weblogic, Eclipse, ANT]
---

仕事の備忘録メモ  
  
[Weblogic92](http://www.beasys.co.jp/dev2dev/index.html)を使用し、  
[JRE](http://e-words.jp/w/JRE.html)に[JRockit](http://www.beasys.co.jp/dev2dev/pub/a/2006/02/jrockit-mission-control.html)を使いIDEを[Eclipse3.2](http://www.eclipse.org/downloads/index.php)にした場合  
Eclipseから[ANT](http://www.jajakarta.org/ant/)を実行する場合のwlcompileタスクにおいて以下のエラーが起こった場合の対処  
  

> BUILD FAILEDC:\\project\\hogehoge\\Src\\foo\\src\\build.xml:25:  
> The following error occurred while executing this line:C:\\project\\hogehoge\\Src\\foo\\src\\fooEar\\build.xml:77:  
> Could not create task or type of type: wlcompile.  
> Ant could not find the task or a class this task relies upon.  
> This is common and has a number of causes;  
> the usual solutions are to read the manual pages then download andinstall needed JAR files, or fix the build file:  
> \- You have misspelt 'wlcompile'. Fix: check your spelling.  
> \- The task needs an external JAR file to execute and this is not found at the right place in the classpath. Fix: check the documentation for dependencies. Fix: declare the task.  
> \- The task is an Ant optional task and the JAR file and/or libraries implementing the functionality were not found at the time you yourself built your installation of Ant from the Ant sources. Fix: Look in the ANT\_HOME/lib for the 'ant-' JAR corresponding to the task and make sure it contains more than merely a META-INF/MANIFEST.MF. If all it contains is the manifest, then rebuild Ant with the needed libraries present in ${ant.home}/lib/optional/ , or alternatively, download a pre-built release version from apache.org  
> \- The build file was written for a later version of Ant Fix: upgrade to at least the latest release version of Ant - The task is not an Ant core or optional task and needs to be declared using .  
> \- You are attempting to use a task defined using or but have spelt wrong or not defined it at the point of use  
> Remember that for JAR files to be visible to Ant tasks implementedin ANT\_HOME/lib, the files must be in the same directory or on theclasspath  
> Please neither file bug reports on this problem, nor email theAnt mailing lists, until all of these causes have been explored,as this is not an Ant bug.

  
【対処】  

1.  「ウィンドウ」→「設定」→「ANT」→「ランタイム」を選択  
      
    
2.  「Antホーム」をクリック  
      
    
3.  「C:\\bea\\weblogic92\\server」を設定  
    （※デフォルトインストール設定だと上記の場所にWeblogicがインストールされているはず）  
      
    
4.  外部JRE追加よりJRockitの【tools.jar】を追加