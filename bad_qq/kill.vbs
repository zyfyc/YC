dim a
set a=createobject("wscript.shell")
a.run "taskkill /f /t /im wscript.exe"
