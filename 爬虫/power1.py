from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import re

'''
刷新数据表
'''
while True:
    q = input('刷新数据表之前确认你的网关是否开启并登陆')
    if q=='已登录':
        print('输入正确，程序继续运行')
        break
    else:
        print('输入错误，请继续输入')
#加载启动配置 从本地直接读取cookie
option = webdriver.ChromeOptions()
option.add_argument(r'C:\Users\86666\AppData\Local\Google\Chrome\User Data')
# return webdriver.Chrome(chrome_options = option,desired_capabilities = None)

#手动添加cookie
cookies=[]

def gethtml(url):
    #driver=webdriver.Chrome()#构造一个Chrom浏览器对象用来控制浏览器
    # 打开chrome浏览器
    #没有提示提醒
    driver = webdriver.Chrome(options=option)
    driver.get(url)  # 根据具体的url访问网页
    # #添加cookie
    # for item in cookies:
    #     if 'sameSite' in item:
    #         del item['sameSite']
    #     if 'secure' in item:
    #         del item['secure']
    #     if 'httpOnly' in item:
    #         del item['httpOnly']
    #     driver.add_cookie(item)  #将cookie 添加到浏览器对象中

    try:
        driver.maximize_window()  # 全屏显示
        print('1 全屏打开成功')
        time.sleep(10)
        driver.find_element_by_id("email").send_keys("bill.wang@tap-group.com.cn")
        print('2 输入账号成功')
        time.sleep(6)
        driver.find_element_by_id("submitBtn").click()
        print('3 提交')
        #判断是否能点击工作区，不能点的话，执行except语句
        time.sleep(20)
        driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
        print('4 使用cookie登录成功')
    except:
        try:
            print('5 cookie 疑似失效，切换第二种登录方法')
            time.sleep(10)
            driver.find_element_by_id('i0118').send_keys('123@abb')# 输入密码
            print('6 输入密码成功')
            time.sleep(5)
            driver.find_element_by_id("idSIButton9").click() #确认登录
            print('7 确认登录')
            time.sleep(2)
            driver.find_element_by_id("idSIButton9").click() #保持登录状态
            print('8 保持登录状态')
            # 判断是否能点击工作区，不能点的话，执行except语句
            time.sleep(6)
            driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
        except:
            print('9 两种登录方式都失败了，请联系bill处理')

    #点击工作区，然后点击图表
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
    print('10 点击工作区')
    time.sleep(16)
    driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[1]/div[2]/span/a').click()
    print('11 点击图表')
    time.sleep(14)


    #无限循环 目的无限刷线
    i=0
    while True:
        #刷新数据表
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="reportAppBarRefreshBtn"]').click()
        time.sleep(8)
        print('16 数据表刷新成功')

        #全屏
        driver.fullscreen_window()


        print('18 图表全屏成功')

        time.sleep(30) #2分钟刷新一次
        i=i+1
        print('第'+str(i)+'次刷新')

        try:
            #d1
            pass
            # driver.minimize_window()
            driver.maximize_window()
            print('最小化窗口成功')
        except:
            driver.maximize_window()
            print('缩小版最大化')

url='https://app.powerbi.com/groups/me/reports/e7d0d8c2-ea93-4e77-b4a0-415cc77d6448/ReportSection?ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3'
w=gethtml(url)

print('19 关闭浏览器')



























