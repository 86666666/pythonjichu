'''
import requests
from bs4 import BeautifulSoup
import bs4

def gethtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('出现错误')

def liebiao(list, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):#不太熟
            tds = tr.find_all('td')
            list.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def print1(list):
    print(list)
    print('{:^10}\t{:^10}\t{:^10}\t{:^10}'.format('大学排名','大学名称','所在地区','总分'))
    for i in list:
        print('{:^10}\t{:^14}\t{:^14}\t{:^10}'.format(i[0],i[1],i[2],i[3]))
def main():
    list = []
    html=gethtml('http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html')
    liebiao(list,html)
    print1(list)


main()
'''

import requests
import re
from selenium import webdriver
driver=webdriver.Chrome()


def gethtml(url):
    while True:
        try:
            headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
            r=requests.get(url,headers=headers)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
            break
        except:
            print('出现错误')




def parser(list,):
    pass

def print():
    pass

def main():
    pass


