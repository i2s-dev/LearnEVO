Dim py, script
py     = "C:\Users\tsinclair.I2SYSTEMS\AppData\Local\Programs\Python\Python312\pythonw.exe"
script = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\")) & "main.py"
CreateObject("WScript.Shell").Run """" & py & """ """ & script & """", 0, False
