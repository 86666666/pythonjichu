
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):  # 如果tr标签不是bs4.element.Tag类型 则过滤
            tds=tr('td') # 这里省略了findALL,实际上应该是tds=tr.findAll('td') 在tr中查找td
            ulist.append([tds[0].string,tds[1].string,tds[3].string])

def printUnivList(ulist,num):
    tblt="{0:^10}\t{1:{3}^10}\t{2:^10}"    # {3}表示 打印学校名称时 需要填充时 使用format函数中第四个变量填充 也就是chr(12288)中文空格
    print(tblt.format("排名","学校名称","总分",chr(12288))) # ^表示居中 <>分别表示左右对齐 6表示槽长度 \t表示横向制表符
    for i in range(num):
        u=ulist[i]
        print(tblt.format(u[0],u[1],u[2],chr(12288)))
    print("Successful!"+str(num))

def main():
    uinfo=[]
    url="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)
main()














