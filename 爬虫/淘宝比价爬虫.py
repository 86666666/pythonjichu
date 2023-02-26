from bs4 import BeautifulSoup
import requests
import re
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://s.taobao.com')
'''模拟登陆'''

wi=driver.find_element_by_css_selector('#fm-login-id')
wi.send_keys('17596972042')
passw=driver.find_element_by_css_selector('#fm-login-password')
passw.send_keys('17596972042gg')
den=driver.find_element_by_css_selector('#login-form > div.fm-btn > button')#定位登陆元素
den.click

r=driver.find_element_by_css_selector('#q')
r.send_keys('书包')
dianji=driver.find_element_by_css_selector('#J_SearchForm > div > div.search-button > button')
dianji.click()
try:
    ri=driver.find_element_by_css_selector('#login-form > div.login-blocks.sns-login-links > a.alipay-login')
    ri.click()
except:
    print('请用支付宝扫码登录')
time.sleep(15)#关键等待操作
u=driver.page_source
#print(u)
print('操作成功')
print(u)
'''
#查看获取到的网页源代码
with open('中国大学定向爬虫.html','wt',encoding='utf-8')as wen:
    wen.write(u)
print('写入成功')
'''
