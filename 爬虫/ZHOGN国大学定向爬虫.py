'''
import requests
from bs4 import BeautifulSoup
import bs4

def gethtml(url):
    '''获取html页面'''
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return('获取网页成功')

def list1(ulist,html):
    '''获取HTML页面关键信息添加到列表里'''
    re=BeautifulSoup(html,'html.parser')
    for tr in re.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr.find_all('td')#返回类表类型，存储查找的结果
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printlist(ulist):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校","总分"))
    for i in range(100):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))

def main():
    ulist=[]
    url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
    html=gethtml(url)
    list1(ulist,html)
    printlist(ulist)
main()
'''
