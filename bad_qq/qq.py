#-*- coding: UTF-8 -*-
#Mode by yc:3365487579
import os

def main():
	
	rules()
	Layout()
	key = raw_input("Input the key:")
	if key=="c2FueWl6eWY=":#grade user
		print "Your grade is user"
		user()
		kill_wscript()
	elif key=="amlzaHVidXp5Zg==":#grade admin
		print "Your grage is admin"
		admin()
		kill_wscript()
	elif key=="YXV0aG9yenlm":#grade root
		print "Your grage is root"
		root()
		kill_wscript()
	else:
		print "Bad key"
		print "Destroying the program now"
		print "bye-bye"
		destroy()
		
def rules():
	os.system("@echo off");
	os.system("title mode by 3365487579");
	os.system("color c");
	os.system("mode con cols=77 lines=40");
	
def Layout():
	print "+--------------------------+"
	print "|                          |"
	print "|       YC:3365487579      |"
	print "|                          |"
	print "+__________________________+"    
	
def destroy():
	os.system("""echo set fso=createobject("scripting.filesystemobject")>>byebye.vbs""")
	os.system("""echo set sfile=fso.getfile("..\\qq\\bad__qq.exe")>>byebye.vbs""")
	os.system("""echo sfile.delete>>byebye.vbs""")
	os.system("""byebye.vbs""")
	
def user():
	os.system("""echo dim a>>user.vbs""")
	os.system("""echo set a=createobject("wscript.shell")>>user.vbs""")
	os.system("""echo dim loc>>user.vbs""")
	os.system("""echo loc=inputbox("input the address:","","")>>user.vbs""")
	os.system("""echo times=inputbox("input the times:")>>user.vbs""")
	os.system("""echo msgbox "Please copy the content at this point">>user.vbs""")
	os.system("""echo a.run loc>>user.vbs""")
	os.system("""echo wscript.sleep 2000>>user.vbs""")
	os.system("""echo for i=1 to times>>user.vbs""")
	os.system("""echo a.sendkeys "^v">>user.vbs""")
	os.system("""echo a.sendkeys "^{ENTER}">>user.vbs""")
	os.system("""echo next>>user.vbs""")
	os.system("""echo a.sendkeys "%{F4}">>user.vbs""")
	os.system("""echo wscript.quit>>user.vbs""")
	
def admin():
	os.system("""echo dim a>>admin.vbs""")
	os.system("""echo set a=createobject("wscript.shell")>>admin.vbs""")
	os.system("""echo dim loc>>admin.vbs""")
	os.system("""echo loc=inputbox("input the address:","","")>>admin.vbs""")
	os.system("""echo times=inputbox("input the times:")>>admin.vbs""")
	os.system("""echo wo=inputbox("input the content you want to say")>>admin.vbs""")
	os.system("""echo dim word>>admin.vbs""")
	os.system("""echo set word=createobject("Word.Application")>>admin.vbs""")
	os.system("""echo word.documents.add>>admin.vbs""")
	os.system("""echo word.selection.text=wo>>admin.vbs""")
	os.system("""echo word.selection.Copy>>admin.vbs""")
	os.system("""echo wscript.sleep 1000>>admin.vbs""")
	os.system("""echo a.run loc>>admin.vbs""")
	os.system("""echo wscript.sleep 1000>>admin.vbs""")
	os.system("""echo for i=1 to times>>admin.vbs""")
	os.system("""echo a.sendkeys "^v">>admin.vbs""")
	os.system("""echo a.sendkeys "^{ENTER}">>admin.vbs""")
	os.system("""echo next>>admin.vbs""")
	os.system("""echo a.sendkeys "%{F4}">>admin.vbs""")
	os.system("""echo wscript.quit>>admin.vbs""")	
def root():
	print "Sorry,This function is disallowed to you"
	
def kill_wscript():
	os.system("""echo dim a>>kill.vbs""")
	os.system("""echo set a=createobject("wscript.shell")>>kill.vbs""")
	os.system("""echo a.run "taskkill /f /t /im wscript.exe">>kill.vbs""")
	

if __name__=='__main__':

	main()
	