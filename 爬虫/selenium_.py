
from selenium import webdriver
import time

url=('https://www.baidu.com')
dr=webdriver.Chrome()
dr.get(url)
wenji=dr.find_element_by_css_selector('#kw')#su
wenji.send_keys('中华人民共和国')
wenji=dr.find_element_by_css_selector('#su')#获取copy-copy selector
wenji.click()#鼠标点击
wenji=dr.find_elements_by_css_selector('#page > a.n')
wenji.click()

driver=webdriver.Chrome()#打开浏览器页面
driver.get('https://www.baidu.com')#driver.get(url)打开一个网页
#driver.get('https://www.csdn.net/')#driver.get(url)再次打开一个网页
wi=driver.find_element_by_css_selector('#kw')
wi.send_keys('56')
wi=driver.find_element_by_css_selector('#su')#定位百度一下元素位置
wi.click()#点击百度一下
#print(driver.page_source)
time.sleep(8)
#driver.close()

from selenium import webdriver
import time
url=('https://www.bilibili.com/video/BV17i4y147wV')
r=webdriver.Chrome()
r.get(url)
script = 'Object.defineProperty(navigator,"webdriver",{get:() => false,});'
ui=r.find_element_by_css_selector('#bilibiliPlayer > div.bilibili-player-area.video-state-pause.video-control-show.video-state-blackside > div.bilibili-player-video-wrap > div.bilibili-player-video-control-wrap > div.bilibili-player-video-control > div.bilibili-player-video-control-bottom > div.bilibili-player-video-control-bottom-left > div.bilibili-player-video-btn.bilibili-player-video-btn-start.video-state-pause > button.bilibili-player-iconfont.bilibili-player-iconfont-start > span > svg > path')
ui.click()


#分割
from lxml import etree
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=')
time.sleep(5)
try:
    for i  in range(11):
        js='var q=document.documentElement.scrollTop=10000'
        driver.execute_script(js)
        time.sleep(3)#休眠时间不能设置的太短否则系统反应不过来例如设为0.2就不行
except:
    print('程序出现错误')



#js

try:
    js='var q=document.body.scrollTop=0'
    driver.execute_script(js)
except Exception as err:
    print(err)

js='window.scrollTop(0,document.body.scrollHeight)'
driver.execute_script(js)

'''
from selenium import webdriver
from selenium .webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.set_window_size(1000,800)
driver.get('https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=')
time.sleep(8)




