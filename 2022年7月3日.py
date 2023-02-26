import requests
import json

#初始化一个session
re_session=requests.session()
headers={
	"Host": "api.powerbi.com",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
	"Accept": "*/*",
	"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	"Accept-Encoding": "gzip, deflate",
	"Access-Control-Request-Method": "POST",
	"Access-Control-Request-Headers": "activityid,content-type,requestid",
	"Referer": "https://app.powerbi.com/",
	"Origin": "https://app.powerbi.com",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-site",
	"Te": "trailers",
}

#登录输入密码的地方
date={"emailAddress":"bill.wang@tap-group.com.cn","ctid":"c46407bb-50f4-4b50-ad1a-d8ba2214cde3"}
url='https://app.powerbi.com/singleSignOn?route=groups%2fme%2fdatasets%2f2012678f-bf1b-474d-8ba4-3afd363e5012%2fdetails%3fctid%3dc46407bb-50f4-4b50-ad1a-d8ba2214cde3%26refreshAccessToken%3dtrue&ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3&refreshAccessToken=true&ru=https:%2f%2fapp.powerbi.com%2f%3froute%3dgroups%252fme%252fdatasets%252f2012678f-bf1b-474d-8ba4-3afd363e5012%252fdetails%253fctid%253dc46407bb-50f4-4b50-ad1a-d8ba2214cde3%2526refreshAccessToken%253dtrue%26ctid%3dc46407bb-50f4-4b50-ad1a-d8ba2214cde3%26refreshAccessToken%3dtrue%26noSignUpCheck%3d1'

re=re_session.post(url,date,headers=headers)
print(re.status_code)
print(re.cookies)
print(re.text)


# url2='https://login.microsoftonline.com'
# date2={'passwd':'123%40abb'}
# re2=re_session.post(url2,date2)
# print(re2.status_code)
# print('re2.cookie',re2.cookies)
# print(re2.text)









