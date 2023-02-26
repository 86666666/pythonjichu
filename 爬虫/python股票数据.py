# import re
# from bs4 import BeautifulSoup
# import requests
# data={'name':'germey','age':'22'}
# pr={
#     'http':'http://112.111.77.94:9999',
#     'https':'https://112.111.77.94:9999',
# }
# # r=requests.post('https://httpbin.org/post',data=data,proxies=pr)
# # print(r.text)
# p=requests.get('https://www.baidu.com',proxies=pr,timeout=6)
# print(p.status_code)
#
#
#
import requests
import json
class King(object):
    def __init__(self,word):
        self.url=('http://fy.iciba.com/ajax.php?a=fy')#chrome抓包分析出ajax请求发送的内容
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
        }
        self.data={
            'f': 'auto',
            't': 'auto',
            'w': word
        }#模拟ajax请求送的数据包

    def get_postdata(self):
        #使用post请求发送一个post请求，data为请求的字典
        #用.content获取响应
        reponse=requests.post(self.url,data=self.data,headers=self.headers)
        return reponse.content
    def parse_data(self,data):
        '''解析json字符串转化为python字典'''
        dict=json.loads(data)
        '''提取中英文的try语句'''
        try:
            print(dict["content"]["out"])#答应获得的数据
        except:
            print(dict["content"]["word_mean"])
    def run(self):
        #编写爬虫逻辑
        #headers
        #data字典
        #发送请求获取响应
        xiangying=self.get_postdata()
        #数据解析json
        self.parse_data(xiangying)
if __name__=='__main__':
    ui=input('请输入你想要翻译的语句')
    word=King(ui)
    #print(word.data)
    word.run()
print('王凯旋是天才哈哈哈你是不是不知道啊')
print('中国可是大好人啊')

