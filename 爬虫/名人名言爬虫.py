import requests
from lxml import etree

def get(url):
    '''获取网页源代码'''
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        html=r.text
    except:
        return html

def jiexi(html,list):
    html1=etree.HTML(html)
    wenben=html1.xpath('//div[@class="quote"]/span[1]/text()')
    zuoze=html1.xpath('//div/span[2]/small/text()')
    tags=html1.xpath('//div[@class="quote"]//div[@class="tags"]/a/text()')







def main():
    list=[]