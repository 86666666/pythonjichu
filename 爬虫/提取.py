'''
import re
with open('中国大学定向爬虫.html','rt',encoding='utf-8')as duchu:
    f=duchu.read()
mingzi=re.compile(r'\"raw_title\"\:\".{0,80}\"\,')
jiage=re.compile(r'\"view_price\"\:\".{0,10}\"\,')
io=mingzi.findall(f)#r'\"raw_title\"\:\".*?\"'
ii=jiage.findall(f)
print(len(io))
print(len(ii))
for i in range(len(io)):
    print(io[i],ii[i])
'''

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
i=driver.find_element_by_css_selector('#kw')
i.send_keys('python')
i=driver.find_element_by_css_selector('#su')
i.click()
p=driver.find_elements_by_xpath('//div[@id="content_left"]/div/h3/a')
for j in p:
    print(j.text)

print('打印成功')


