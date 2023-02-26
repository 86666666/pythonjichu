import requests
from lxml import etree
'''获取网页源代码'''
try:
    r = requests.get('http://quotes.toscrape.com/page/1/')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
except:
    print('出现错误')
html1 = etree.HTML(html)
wenben = html1.xpath('//div[@class="quote"]/span[1]/text()')
zuoze = html1.xpath('//div/span[2]/small/text()')
#tags = html1.xpath('//div[@class="quote"]//div[@class="tags"]/a/text()')
tags=html1.xpath('//div[@class="quote"]//div[@class="tags"]/a[1]/text()')
#tags=html1.xpath('/html/body/div/div[2]/div[1]/div[1]/div/text()')
#print(wenben) 打印列表
#print(zuoze)  打印列表
#print(tags)   打印列表
if len(wenben)==len(zuoze):
    print('对的')
print(len(wenben))
ulist=[]
for i in range(len(wenben)):
    ulist.append([wenben[i],zuoze[i],tags[i]])
print(ulist)

print('{0:<130}\t{1:^20}{2:^8}'.format('名言','作者','标签'),chr(12288))
for i in ulist:
    print('{0:<130}\t{1:^20}{2:^8}'.format(i[0],i[1],i[2]),chr(12288))

