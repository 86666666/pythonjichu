# with open('90.txt') as txt1:
#     wq=txt1.read()
#     print(wq.rstrip())

# with open('90.txt') as txt2:
#     print(type(txt2))
#     for i in txt2:
#         print(i.rstrip())

with open('90.txt')as txt3:
    w=txt3.readlines()

print(w)
for i in w:
    print(i.rstrip())






'''
with open("C:\\Users\86666\Desktop\python文件处理\文件1.txt",'rt')as p:
    print(p.read().strip())
print('23')


wang=['南京','天津']
f=open("C:\\Users\86666\Desktop\python文件处理\文件2.txt",'at')
f.write('wangkaixuan\n王凯旋是天才')
f.writelines(wang)
f.close()
import requests
r=requests.get('https://static.runoob.com/images/dashang/alipay.jpg')
r.encoding=r.apparent_encoding
with open('wenjian1.png','ab')as p:
    p.write(r.content)
print('写入成功')

import json
wang={2:4,'bei':'斤','天津':'湖南'}
#wang=json.dumps(wang,ensure_ascii=False)
print(wang)
print(type(wang))
with open('C:\\Users\86666\Desktop\python文件处理\json1.json','at') as p:
    json.dump(wang,p,ensure_ascii=False)

import json
with open('C:\\Users\86666\Desktop\python文件处理\json1.json','rt')as n:
    wenjian=json.load(n)
print(wenjian)
print(type(wenjian))

import requests
a=('https://www.uc123.com')
b=('https://www.baidu.com')
r=requests.get(b)
print(r.status_code)
r.encoding=r.apparent_encoding
print(r.text)
print(r.url)
print(r.request.headers)

import requests
def geturl(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.status_code
        return r.text
    except:
        print('出现错误')
print(geturl('https://www.baidu.com'))

import requests

headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
p=requests.head('https://www.baidu.com',headers=headers)
print(p.headers)
print(p.status_code,p.url)
print(p.request.headers)

import requests
try:
    r=requests.get('https://www.qq.com/robots.txt')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    a=r.text
    with open(r'C:\\Users\86666\Desktop\python文件处理\robots.txt', 'at')as wenjian:
        wenjian.write(a)
        print('写入成功')
except Exception as err:
    print(err)

import requests
headers=({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'})
we={'wd':'python'}
r=requests.get('https://www.baidu.com',params='wd=pyhton')

print(r.status_code)
r.encoding=r.apparent_encoding
print(r.url)
print(r.request.headers)
'''












































































































































































































































































































































































































































































































































