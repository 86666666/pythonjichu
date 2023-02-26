from selenium import webdriver
import time
import re

def gethtml(url):
    '''定义函数获取html源代码'''
    '''由于淘宝是动态网页无法用requests库获取所以使用selenium模拟器'''
    driver=webdriver.Chrome()#构造一个Chrom浏览器对象用来控制浏览器
    driver.maximize_window() #全屏显示
    driver.get(url)#根据具体的url访问网页
    # 第一种滑块验证，人工操作
    i3 = driver.find_element_by_css_selector('#login > div.corner-icon-view.view-type-qrcode > i')
    i3.click()
    time.sleep(15)  # 等待15秒，用来扫码(人工操作)
    '''将进度条拉到页面最后'''
    try:
        js = 'var q=document.documentElement.scrollTop=10000'
        driver.execute_script(js)  # execute_script()函数运行js下滑脚本
    except:
        print('出现错误')
    html = driver.page_source #获取网页源代码
    driver.close()#关闭浏览器
    print('关闭浏览器')
    #print(html)
    return html

def xieru(html):
    with open("C:\\Users\86666\Desktop\python文件处理\钓鱼.html",'at',encoding='utf-8')as wenjian:
        wenjian.write(html)
        print('写入成功')
    with open('C:\\Users\86666\Desktop\python文件处理\钓鱼.html','rt',encoding='utf-8')as j:
        html2=j.read()
    return html2


def tiqu(list,html2):
    '''从获得到的网页中提取需要的信息'''
    try:
        '''提取商品名称'''
        zhengze=re.compile(r'"raw_title":".{0,40}",')#用re.compile()函数将正则表达式的字符串转化(编译)为正则表达式对象用于多次操作
        '''获得付款人数'''
        zhengze1=re.compile(r'"view_sales":".{0,30}",')
        l1=zhengze.findall(html2)
        l2=zhengze1.findall(html2)
    except:
        print('出现错误')
    if len(l1)==len(l2):
        for i in range(len(l1)):
            u=eval(l1[i].split(':')[1])
            u2=eval(l2[i].split(':')[1])
            list.append([u,u2])
    print('打印列表')
    return list

def print1(list2):
    '''按规则打印'''
    print('{0:<35}\t\t\t\t\t{1:<12}'.format('付款人数','产品名称'),chr(12288))
    for i in range(len(list2)):
        print('{0:<35}\t\t\t\t\t{1:<12}'.format(str(list2[i][0][0]),str(list2[i][1][0])),chr(12288))





def main():
    list=[]
    url=('https://s.taobao.com/search?q=%E9%B1%BC%E7%AB%BF&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306')
    html=gethtml(url)
    xieru(html)
    html2=xieru(html)
    list2=tiqu(list,html2)
    print(list2)
    print1(list2)


main()






























# #知道淘宝密码就定位元素然后调用键盘事件输入账号密码就可以了，但是淘宝的滑块验证不好搞
# #这里还是用淘宝的扫码登陆比较好，就是中间扫码这个环节要人工干预操作一下
# #第一种定位元素输入账号密码登录（不好搞）
# i=driver.find_element_by_css_selector('#fm-login-id')
# i.send_keys('17596972042')
# i2=driver.find_element_by_css_selector('#fm-login-password')
# i2.send_keys('1024863144')


# try:
#     js='var q=document.documentElement.scrollTop=10000'
#     driver.execute_script(js)#execute_script()函数运行js下滑脚本
# except:
#     print('出现错误')
# # try:
# #     for i  in range(11):
# #         js='var q=document.documentElement.scrollTop=10000'
# #         driver.execute_script(js)
# #         time.sleep(3)#休眠时间不能设置的太短否则系统反应不过来例如设为0.2就不行
# # except:
# #     print('程序出现错误')
#
#
#
# #
# # with open("C:\\Users\86666\Desktop\python文件处理\淘宝.html",'at',encoding='utf-8')as n:
# #     n.write(html)#将得到的html源代码保存到文件
# #
# # print('写入成功')
# # driver.close()
# with open('C:\\Users\86666\Desktop\python文件处理\淘宝.html','rt',encoding='utf-8')as j:
#     #print(j.read())
#     ji=j.read()
#     print('读取成功')
#
# mingzi=re.compile('"raw_title":".{0,30}",')
# jiage=re.compile(r'"view_price":".{0,10}",')
# io=mingzi.findall(ji)#r'\"raw_title\"\:\".*?\"'
# ii=jiage.findall(ji)
# print(io)
# print(eval(io[0].split(':')[1]))
# print(type(io[0]))
# print(ii)
#
# # print(len(io))
# # print(len(ii))
# # for i in range(len(io)):
# #     print(io[i],ii[i])
#




