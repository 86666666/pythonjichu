# import requests
# import json
# url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=734d17c7-697f-4453-8e70-579f0e217eff'
# date={
#   "msgtype": "text",
#   "text": {
#     "content": "Hi，我是机器人bill的小助手\n这是一个python发送的消息"
#   }
# }
#
# hearder={
# 'Content-Type: application/json'
# }
# re=requests.post(url,json.dumps(date),hearder)
# print(re.status_code)

from weworkbot import Bot as bill
def fasong(a):
  a=str(a)
  url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=734d17c7-697f-4453-8e70-579f0e217eff'
  bill(url).set_text(a).set_mentioned_list(["@all"]).send()
  bill(url).set_text('<font color="info">'+str(a)+'</font>', type='markdown').send()


fasong('测试')




# wBot(url).set_text("hello world").send()
# wBot(url).set_text('<font color="info">Hello world</font>', type='markdown').send()
# wBot(url).set_image_path('test.jpeg').send()