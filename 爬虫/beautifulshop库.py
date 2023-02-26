'''
from bs4 import BeautifulSoup
import requests
r=requests.get('http://www.baidu.com')
print(r.status_code)
r.encoding=r.apparent_encoding
#print(r.text)
ui=(r.text)
shop=BeautifulSoup(ui,'html.parser')
                    #html解析器
print(shop.title)#查看title标签
print(shop.a)#查看第一个a标签
print(shop.a.attrs)#查看a标签的属性
print(shop.a['href'])#查看a标签属性的字典
print(shop.a.name)#查看a标签的名字
print(shop.a.parent.name)#查看a标签的父标签名字
print(shop.a.string)#a标签中的字符串
print(shop.p)#查看p标签
print(shop.p.parent)#查看父标签
print(shop.p.parent.name)#查看父标签的名字

#从本地打开HTML文档
from  bs4 import BeautifulSoup
import requests
wj=open('jjk.html',encoding='utf-8')
r=BeautifulSoup(wj,features='html.parser')
print(r.head.contents)#获得儿子节点
print('head标签的儿子节点有'+str(len(r.head.contents))+'个')#获得儿子节点的数量
print(r.head.contents[2])
for i in r.head.children:
    print(i)
    print(r.a['href'],r.a.string)

#标签美化prettify
from bs4 import BeautifulSoup
import requests
u=open('jjk.html',encoding='utf-8')
r=BeautifulSoup(u,features='html.parser')
print(r.prettify())
with open('jj.html','wt',encoding='utf-8')as k:
    k.write(r.prettify())
print('写入成功')
'''
#标签检索<tag>.find_all函数
from bs4 import BeautifulSoup

r=BeautifulSoup(open('jj.html',encoding='utf-8'),features='html.parser')

for i in r.find_all('a'):
    print(i['href'],i.string ,)
    wenjian=str((i['href'],i.string))
    wenjian=wenjian.strip()#去掉空格
    with open('jjj.xls','at')as d:#写入文件
        d.write(wenjian)








