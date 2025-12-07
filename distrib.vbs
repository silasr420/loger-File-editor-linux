Dim Msg, Style, Title, Response, MyString, Message, Default, MyValue, RetVal, Process
Msg = "Do you have python 3 installed?"    ' Define message.
Style = vbYesNo Or vbQuestion Or vbDefaultButton1  Or vbSystemModal   ' Define buttons.
Title = "loger File editor Installer"    ' Define title.
        ' Display message.
Response = MsgBox(Msg, Style, Title)
If Response = vbYes Then    ' User chose Yes.
    ' DEVKEY PROMPT
    On Error Resume Next

    Set objShell = CreateObject("WScript.Shell")

    ' Path to your exe file
    exePath = "loger_file_editor.py"

    ' Try to run it
    objShell.Run Chr(34) & exePath & Chr(34), 1, False

    If Err.Number <> 0 Then
        MsgBox "Error launching installer: " & Err.Description, vbCritical, "Launch Failed"
    End If

    On Error GoTo 0
Else    ' User chose No.
    MsgBox "Go to www.python.org, download and install any version of python between 3.11 and 3.14. Then close and reopen this program" & Err.Description, vbExclamation,"Error"
End If
