# -*- coding: utf-8 -*-
# Mode by yc

import json
import re
import datetime
import urllib2
import threading
import Queue
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
from Tkinter import *


reload(sys)
sys.setdefaultencoding('utf8')

def send(web_info):
	info = web_info[17:]
	web_info = web_info[0:17]
	print web_info
	print info
	time.sleep(1)
	pwd = ""#password,cleaned by yc
	pwd = pwdencoder(pwd)#function for password
	msg = email.mime.multipart.MIMEMultipart()
	msg['Subject'] = info
	msg['From'] = ''#Your own email to send message

	msg['To'] = web_info
	
	try:
		smtp = smtplib.SMTP()
		smtp.connect('smtp.163.com','25')
		smtp.login('',pwd)#Your own email to send message
		msg = msg.as_string()
		smtp.sendmail('',[web_info],msg)#Your own email to send message
		smtp.quit()
	except Exception as e:
		pass

def pwdencoder(pwd):
	pwd = pwd+"wo"
	pwd = pass_1()
	return pwd

def pass_1():
	if "wo"=="wo":
		pwd = ""#password is false
	if "wo"=="wo":
		pwd = ""#true password
	return pwd
	
def show():
	print "\r\b"
	print
	print u'\r\b\t工具制作   by ：夜程(3365487579)'
	print u'此工具用于服务器加固，帮助网管提高服务器安全性'
	print u'有任何问题，请联系作者'
	print u'Powered by yc'
	print u'We are always so young'
	print u''
	print "\n"

flag = 0
	
def to_find(port,email):
	port = port.replace("\n","")
	email = email.replace("\n","")
	os.system("netstat -ano |findstr %s>>yc.txt"%port)
	result = os.popen("netstat -ano |findstr %s"%port)
	
	#print result.read()
	result = str(result.read())
	#print result
	cout = result.count("\n")
	if cout>=2:
		t_flag = 0
		fx = open('yc.txt','r')
		fx_list = fx.readlines()
		k = 0;
		for x in fx_list:
			if k==0:
				k = k+1
				t_flag = t_flag + 1
				pass
			else:
				judge = x.find(":%s"%port)
				if judge>18 and judge<26:
					t_flag = 1#have connecting
					try:
						fx.close()
					except:
						pass
					global flag
					if flag==0:#before is not connect
						print "ok"
						send(email+x)
						#send("bad")
					else:#before is connect
						pass
						
					
				else:
					t_flag = t_flag+1
		print t_flag
		print cout
		if t_flag==cout:
			flag = 0
		else:
			flag = 1
			
					
		fx.close()	
	else:
		pass
	
def check():
	try:
		fp = open('config.conf','r')
		configs = fp.readlines()
		for x in configs:
			if 'port' in x:
				index = x.find("port")
				port = x[index+5:]
				print port
			else:
				if 'email' in x:
					index = x.find("email")
					email = x[index+6:]
					print email
				else:
					print u'配置错误'
					print 'bye bye'
		while(1):
			time.sleep(3)
			try:
				to_find(port,email)
				
			except:
				print "Error occupied!!!"
			try:
				os.system("del yc.txt")
			except:
				print "yc.txt is not exists"
				
	except:
		print u'配置文件config.conf损坏'
		print 'bye bye'
	
		
if __name__ == '__main__':
	show()
	check()
	



