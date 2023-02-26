'''
import requests
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
r=requests.get('https://page.om.qq.com/page/OAYLw5pIxZfUyWZWv4hISzBw0',headers=headers)
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)

import requests
from bs4 import BeautifulSoup
r=requests.get('http://www.people.com.cn/')
if r.status_code==200:
    r.encoding=r.apparent_encoding
    ui=r.text
with open('C:\\Users\86666\Desktop\python文件处理\html3.txt','at',encoding='utf-8')as wenjian:
    wenjian.write(ui)
    print('写入成功')
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(open('C:\\Users\86666\Desktop\python文件处理\html3.txt','rt',encoding='utf-8'),features='html.parser')
#print(soup.a.string)

#print(soup.a['href'])
#print(soup.a.parrent)
#print(type(soup.a.attrs))
#print(soup.head)
#print(soup.head.contents)
#print(soup.html.prettify())
#print(soup.find_all('a'))

for i in soup.find_all('a',string=str):
    print(i.string,i['href'])
'''
from bs4 import BeautifulSoup
import requests
r=requests.get('https://python123.io/ws/demo.html')
r.encoding=r.apparent_encoding
ui=r.text
#print(r.text)
#soup=BeautifulSoup(r.text,'html.parser')
#for  i in soup.html.children:
 #   print(i)
soup=BeautifulSoup(ui,'html.parser')
print(soup.find_all('a'))
'''


















