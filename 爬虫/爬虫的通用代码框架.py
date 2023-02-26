#爬虫的通用代码框架
import requests
def gethtml2(url):
    try:
        u={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
        print('正在访问下载download该url对应网页')
        r=requests.get(url,params=u)
        print(r.status_code)
        r.raise_for_status() #判断是否异常
        r.encoding=r.apparent_encoding
        print('网页打印成功')
        print(r.text)
    except:
        print('访问失败')

url=('http://172.16.64.78:8001/demo2/ceshi2')
url2='https://www.thepaper.cn/newsDetail_forward_19728680'
gethtml2(url2)



