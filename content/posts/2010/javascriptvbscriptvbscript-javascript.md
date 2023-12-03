---
title: '[JavaScript][VBScript]VBScript + Javascriptで簡単プロジェクト内ツール。その１'
date: 2010-07-08T13:44:00.001+09:00
draft: false
tags : [JavaScript, VBScript]
---

プロジェクトでIE6上で動く VBScript + JavaScript + HTML のツールを作ってみた。

なんで今更？IE6？

  

会社の中では未だに頑固にIE6が標準だーって会社は多いのさ。

  

本当は HTML5 + JavaScript で作りたかったけど仕方ない。

会社のみんなにChromeやFireFoxを強制的にインストールさせるのは面倒だからね。

  

要件はある固定長インターフェースファイルを使ったテスト用に、

  

*   テキストファイルを別のフォーマットに変えてくれ。(ファイルI/O)
*   要件は流動的に変わる。インクリメンタルにイテレーティブに。
*   実装工数はインフラの空き時間を使って。

  

この用件ならhttpアクセスで画面はHTMLインターフェースでやるのが適当かなと思った。

ついでに皆標準的に入れてるブラウザはIE6。

  

ファイル I/O　部位を VBScript に任し、

他の挙動を JavaScript で制御するのが適当か？

以下その場合の注意点

  

#### VBScript のファイルI/Oを有効化するにはIE6の設定変更が必要

1.  メニューバーの【ツール(T)】より【インターネットオプション】を起動します。
2.  【セキュリティ】タブを選択し、【レベルのカスタマイズ(C)...】ボタンをクリックします。
3.  【スクリプトを実行しても安全だとマークされている ActiveXコントロールのスクリプト実行】を有効にします。

  
これを画面の最下部に常に表記。  
  
で、まずはFile I/O部のVBScriptコード  
  

注意点は読み込んだ内容をJavaScriptに渡す場合、

配列渡しはうまくいかなかったので、

適当な区切り文字をはさんで渡し、JavaScript側でSpritしたことと、

動的な配列が定義出来なかったのでReDimとPreserveを多様したこと

  

#### 書き込み

```
Function FileOutput(FULLPATH,TXT)  
Dim objFSO, objFile  
  
  
Set objFSO = CreateObject("Scripting.FileSystemObject")  
If Err.Number = 0 Then  
    Set objFile = objFSO.OpenTextFile(FULLPATH, 8, True)  
    If Err.Number = 0 Then  
        objFile.Write(TXT & vbcrlf)  
        objFile.Close  
    Else  
        WScript.Echo "file open error: " & Err.Description  
    End If  
Else  
    WScript.Echo "error: " & Err.Description  
End If  
  
Set objFile = Nothing  
Set objFSO = Nothing  
End function  

```

#### 読み込み

```
''指定されたパスのファイルを読み取りJavaScriptに渡す。  
Function FileInput(FULLPATH)  
Dim objFSO, objFile  
Dim cnt,max  
Dim ret  
  
Dim Arr()  
ReDim Arr(10)  
  
Set objFSO = CreateObject("Scripting.FileSystemObject")  
If Err.Number = 0 Then  
    Set objFile = objFSO.OpenTextFile(FULLPATH, 1, false)  
    If Err.Number = 0 Then  
            cnt = 0  
            max = 10  
              
            While (objFile.AtEndOfStream=false)  
                Arr(cnt) = objFile.ReadLine  
                cnt = cnt + 1  
  
                ''cntが配列の配列数に達した時、定義し直して１０配列数を増やす。  
                if cnt = max then  
                    max = max + 10  
                    ''Preserveを入れると配列の中身を壊さずに再定義出来る。  
                    ReDim Preserve Arr(max)  
                End if  
            Wend  
        objFile.Close  
    Else  
        WScript.Echo "file open error: " & Err.Description  
    End If  
Else  
    WScript.Echo "error: " & Err.Description  
End If  
  
''区切り文字を使って配列を連結する。  
For Each buf in Arr  
    ret = ret & buf & "区切"  
Next  
  
Set objFile = Nothing  
Set objFSO = Nothing  
  
FileInput = ret  
  
End function  

```