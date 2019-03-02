dim a
set a=createobject("wscript.shell")
dim loc
loc=inputbox("input the address:","","")
times=inputbox("input the times:")
wo=inputbox("input the content you want to say")
dim word
set word=createobject("Word.Application")
word.documents.add
word.selection.text=wo
word.selection.Copy
wscript.sleep 1000
a.run loc
wscript.sleep 1000
for i=1 to times
a.sendkeys "^v"
a.sendkeys "^{ENTER}"
next
a.sendkeys "%{F4}"
wscript.quit
