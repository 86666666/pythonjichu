import requests
import json
import time

url=('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=recommend&page_limit=20&page_start=0')
user={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
r=requests.get(url,headers=user)#伪装请求头
print(r.status_code)
r.encoding=r.apparent_encoding
print(type(r.text))#查看返回的数据类型
ui=r.text
#存储要解析的json数据
with open('douband2.json','wt',encoding='utf-8')as p:
    p.write(ui)
print('写入成功')
time.sleep(2)#休眠2秒等待文件写入成功

#提取需要的信息
with open('douband2.json','rt',encoding='utf_8')as o:
    g=json.load(o)
#print(type(g))
#print(g)
movie_list=g['subjects']#获取字典里键的值
#print(movie_list)
for i in movie_list:
    ji=i['url']
    print(i['title'],i['url'])




