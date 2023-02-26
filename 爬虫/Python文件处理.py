#下载一个视频

import requests
url=('https://vd3.bdstatic.com/mda-jk4ryvcmwaxkdk3r/mda-jk4ryvcmwaxkdk3r.mp4')
r=requests.get(url)
print(r.status_code)

f_name='mv.mp4'
with open(f_name,'wb') as i:
    i=i.write(r.content)
print('下载成功')

'''
import  requests
r=requests.get('http://www.baidu.com')
print(r.status_code)
r.encoding='utf-8'
print(r.text)
with open('93.txt','at') as i:
    i=i.write(r.text)

#爬虫的通用代码框架
import requests
def gethtml(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ('产生异常')


print(gethtml('http:www.baidu.com'))

import requests
ui={1:5,2:4}
r=requests.get('https://www.baidu.com',params=ui)
print(r.url)




#更换user——agent名片反爬虫
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
#r=requests.get('https://www.amazon.cn/?tag=youhuijia63-23',headers=headers)
#r=requests.get('https://www.baidu.com/robots.txt',)爬取百度的robots协议

#r.encoding=r.apparent_encoding
#print(u.text)
print(r.status_code)
print(r.text)
print(r.url)
print(r.request.headers)#准确显示头部信息user——agent
print(r.headers)#全面显示头部信息


#关键词提交
#百度的关键词接口 http://www.baidu.com/s?wd=keyword
#360搜索引擎关键词接口http://www.so.com/s?q=keyword
import requests
#反爬虫
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}

d={'wd':'王凯旋'}
r=requests.get('https://www.baidu.com/s',params=d,headers=headers)
print(r.status_code)
print(r.request.url)
print(r.request.headers)
print(len(r.text))
r.encoding=r.apparent_encoding
print(r.text)

#查询ip地址的归属地
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}

p={'ip':'202.204.80.112'}
r=requests.get('https://ipchaxun.com/',params=p,headers=headers)
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)

#下载一个html文件
import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
r=requests.get('http://www.xinhuanet.com/politics/xxjxs/2019-04/15/c_1124367882.htm',headers=headers)
print(r.status_code)
r.encoding=r.apparent_encoding
u=r.text
with open('jjk.html','wt',encoding='utf-8')as i:
    i.write(u)
print('写入成功')
'''







