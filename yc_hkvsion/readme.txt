mode by yc

1、工具版权说明：
	大家好，我是夜程，QQ：3365487579，感谢兄弟0.1+0.2！=0.3（QQ：1351003587）的大力支持和帮助
	网站:www.lang-v.com
	QQ群:597635298
2、工具对象说明：
	该工具针对海康威视未打补丁的摄像头进行任意密码重置攻击，能有效拿下较多摄像头
3、工具使用说明：
	首先用scan，啊d网络版等工具扫描端口80，然后放到ip.txt文本里，运行y.exe(y81.exe是针对端口为81的摄像头)得到纯ip的ip_true.txt文件，然后运行c.exe验证ip是否是海康威视,结果会导出到good.txt。ok，然后使用HikvisionPasswordResetHelper.exe，使用方法是输入good.txt的ip地址，然后点击"Get User List"得到用户名，然后下面的"New Password"可以自定义密码，然后尝试"Set password for selected user"重置密码，若得到"Successfully assigned password....."则说明重置成功
4、工具注意说明：
	可能存在缓存，导致能重置的ip重置报错，可以关掉在试一次;尽量使用IE浏览器，firefox和google的插件有点麻烦
5、最最最重要的说明：
	该工具只用于测试与检查，请勿用做非法用途，否则概不负责！！！
