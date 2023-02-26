from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import re
from weworkbot import Bot as bill


def fasong(a):
    a = str(a)
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=734d17c7-697f-4453-8e70-579f0e217eff'
    rs = bill(url).set_text(a).send()


# 加载启动配置 从本地直接读取cookie
option = webdriver.ChromeOptions()
option.add_argument(r'C:\Users\bill.wang.TAP-GROUP\AppData\Local\Google\Chrome\User Data')
'''
刷新数据集
'''


def gethtml(url):
    # driver=webdriver.Chrome()#构造一个Chrom浏览器对象用来控制浏览器
    # 打开chrome浏览器
    driver = webdriver.Chrome(options=option)
    driver.get(url)  # 根据具体的url访问网页
    # 添加cookie
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
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '1 全屏打开成功')
        time.sleep(10)
        driver.find_element_by_id("email").send_keys("bill.wang@tap-group.com.cn")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '2 输入账号成功')
        time.sleep(6)
        driver.find_element_by_id("submitBtn").click()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '3 提交')
        # 判断是否能点击工作区，不能点的话，执行except语句
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '4 使用cookie登录成功')
    except:
        try:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '5 cookie 疑似失效，切换第二种登录方法')
            time.sleep(10)
            driver.find_element_by_id('i0118').send_keys('123@abb')  # 输入密码
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '6 输入密码成功')
            time.sleep(5)
            driver.find_element_by_id("idSIButton9").click()  # 确认登录
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '7 确认登录')
            time.sleep(2)
            driver.find_element_by_id("idSIButton9").click()  # 保持登录状态
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '8 保持登录状态')
            # 判断是否能点击工作区，不能点的话，执行except语句
            time.sleep(6)
            driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
        except:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '9 两种登录方式都失败了，请联系bill处理')

    # 点击工作区，然后点击数据集
    time.sleep(14)
    driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '10 点击工作区')
    time.sleep(4)
    try:
        driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[2]/div[2]/span').click()
    except:
        driver.find_element_by_xpath('').click()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '11 数据集已打开')
    time.sleep(14)

    # 无限循环 目的无限刷新
    i = 0
    while True:
        i = i + 1
        # 点开数据集刷新页面
        try:
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
            time.sleep(6)
            print('点击数据集成功')
        except:
            driver.refresh()
            time.sleep(40)
            driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
            print('点击数据集成功')
        ##刷新数据集
        try:
            # A1
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A1成功')
        except:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '失效准备使用A2')
            try:
                # A2
                # 点开数据集刷新页面
                driver.refresh()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '重新刷新了页面')
                time.sleep(40)
                driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
                time.sleep(6)
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A2成功')
            except:
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A2失效准备使用A3')
                try:
                    # A3
                    # 点开数据集刷新页面
                    driver.refresh()
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '重新刷新了页面')
                    time.sleep(40)
                    driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
                    time.sleep(6)
                    time.sleep(2)
                    de = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                    ActionChains(driver).double_click(de).perform()  # 双击元素
                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A3双击成功')
                except:
                    try:
                        # A4
                        # 点开数据集刷新页面
                        driver.refresh()
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '重新刷新了页面')
                        time.sleep(40)
                        driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
                        time.sleep(6)
                        time.sleep(2)
                        driver.find_element_by_xpath("//div[3]/div[3][@class='cdk-overlay-connected-position-bounding-box']//button[1]").click()
                        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A4成功')
                    except:
                        try:
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '回到工作区重新开始')
                            # 点击工作区，然后点击数据集
                            time.sleep(30)
                            driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '10 点击工作区')
                            time.sleep(30)
                            try:
                                driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[2]/div[2]/span').click()
                            except:
                                driver.find_element_by_xpath('').click()
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '11 数据集已打开')
                            time.sleep(30)
                            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'A1成功')
                        except:
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '全部失败')
                            driver.find_element_by_xpath("//div[3]/div[3][@class='cdk-overlay-connected-position-bounding-box']//button[1]").click()
                            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '全部失败之后最后一次尝试成功')

        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '13 开始刷新数据集')
        time.sleep(120)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '14 数据集刷新成功')
        fasong(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '   第' + str(i) + '次刷新数据集成功')
        time.sleep(400)


url = 'https://app.powerbi.com/groups/me/reports/e7d0d8c2-ea93-4e77-b4a0-415cc77d6448/ReportSection?ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3'
try:
    gethtml(url)
except Exception as err:
    fasong(str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '    Hill bill 刷新数据集程序运行失败，请及时处理')
    print('下面是具体的报错日志')
    print(err)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), '19 关闭浏览器')



























