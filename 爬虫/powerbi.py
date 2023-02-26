from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import re

#加载启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# return webdriver.Chrome(chrome_options = option,desired_capabilities = None)

#代码继承于淘宝刷新
cookies=[
{
    "domain": ".app.powerbi.com",
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "ARRAffinity",
    "path": "/",
    "sameSite": "unspecified",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "7d3d769ddd898adad8d06a7fa8abd349f7707351aff1b46d4d3e9ddaa2f08d99",
    "id": 1
},
{
    "domain": ".app.powerbi.com",
    "hostOnly": 'false',
    "httpOnly": 'true',
    "name": "ARRAffinitySameSite",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "7d3d769ddd898adad8d06a7fa8abd349f7707351aff1b46d4d3e9ddaa2f08d99",
    "id": 2
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": ".AspNet.Cookies",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "chunks:2",
    "id": 3
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": ".AspNet.CookiesC1",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "H4sIAAAAAAAEAJ1YXXerOpL9RdOLD5N7_BhshE0sEYQ-QC-zADnBSGAS2webXz-Fc7r79qw1L_PglWChKqlq165dPj6Sto6bU3pKcj7vXXLaX_b9dVSb_cu-awLC9n7KVISZuWddG2Xzp4_nJE65CrOZhHSLffi7xRF30q0JSBedDptkRYpssWmFObulTb7Lfuyq3YhJ7s7Mp2mKwpBwexUOX953jsXr8v6bcLPTR_aPIxxLy8XEfkVm1OFtNKmT4ypW3g-M9mUXXdMtacuHE6Tb8o7jyFdwRMxeF3Nj4-PF3Fnv6NTM598HnzjNI_ArGZja1_OhD6zerDuyLR281acSbOO4dMD2ibDXaymze5m7Jo2TFnf7O4mJUQz_3p-mUyWRs-_Od9Jxj3TZnDLug89b2ZentIs8wkoPAgKhayCUYtVAKDEr3ZTtZ8KMSx7TqZTuA2ycmp02i83SXZ_LgpyX73JXpMoKnPXYza1aYaRsGqG5du2sH0t6VFtLezmK9Q3s2GWPcFBKn2t61L24FV4A7_AlBptK3i_Pcxdhq2L69At3ehy65n7o-HTozGpZr3t0VTmk3SRjHU-f_7YZ_K578vRDOgxw2D_wvJ9xF03P523kH0zwwgqthGtcWYxCR8FXzkSVza-TtFQczb3Ie5ccjXCYoAI77o6xsKpM8s2kK2vuRrRvU-GYWUqXamQeor-Sir1OzFKFnTuv4vu7cK3DWIKOdiwYo-8iGr-loN_4Cdv1H9h-TmXH59JL2oMsHcKyK4nFCZ_cU9kpc5DZg_SAp460Kcsckj_33ppdYmuxnqsn7hJ2YNGV5M4D5w7giru4K1d4uw8ObO89Mbdd8PZ5xfNngLflY4kLOTnzggmyAZtD6P7Y2sO7rxCv1wlzEcLeFeU0WmLe9J_L-nQwSDKOXO3R7yMKcy4E0gXd6dh4uWw566ifRsk-l_Qsd0nM48Y7Cqt48Xqt3GQjIpSVj9XpiUPAxB-_UymDERsV5YUQoiduLcg7nRXCcsTUrj-I-3mtvGyVR3Y4cIizaPPc0U-c69iaJeflnAGeX_2y318JC3uycZxywY1EBsvoqrbtqVwwwWinYiCRZS_4bQph_4bD04LDw6DbutevOkawXz9qX0yHnvyu86CrlxwOYoK_L_v-icGb9tBNOaFTwj2Vn_zWxeut9NZX2HN7-inouJyxKpIgZdavUXKmTPnKTb7JVrQ40mG25HdQtlnsdtENP3OjR7V7csSJzLaH2nXUxpmVLCG_GeTXAL9EDn44Pun395RRm24BA1uzxHgqezurggBW1rc_eGkxA56as_uCl5KRHuwEwEvXsoPcbxxfdeWMAY-l3Du45_-049Te5UmVR36elGjDiq_H3FwlFmhkEXmr4mRXeva94iMTxZhgHox5QZK6b-4qIgkx9ivvkZBRcmAMSe3aaxMlhejbindJLEUimh3k3W8LxlXOEWHP_QWdpPl_7u_MTRUWzkYLLp9n-62iNtceeal9hQFzrhR6RSR-1ED7dU_hrm6u-2xmhTjVopzYlmzg-SEGq2p59aRoN01kR-3ZVkbBSy7H38C1e96FXR45HtuZ4NjTPew3uL-70jQB9khACgGvIQ94h2ITRBkjqubAE5Zuah5s8TZUlRU-QzquHLegBa1o3I7AG8mRu5z3Y0Vd8cJ2Nmkce63j1mSO8YCnFMT6S7KQHK25s8FC_0iuwGNJ1a9XrB8F-PvixZhWls9LrupY7LMlHoY_nrwF51FzSETkzrl048qa-Rkvg36eezLmTCWVEX9yjYo0fsZzI4yKs16wdEsl5WqzcAIR2Z1afaKxDkrPNdyjgg9UCV_7sh_fREwR3iZG8CCG9QuDOuGMKhmNLxD_qnFVkIoEYz-Ee6Fz5Y477VshHHUphZYVUpIyAjVKI7j3xPgzH0rMKIB8TKWxt6wjVeaM5ue8ZJ8NYbXEC9YH4PUC-gDcN7kyRGUNfQDinVJ3BPDiiUTOg_YjFvHFgfghwBpXC69HYsU4ecafDrqj3h14XadHbr9qz5KK2yVeFdRCUe-IFZ0FfDX3OnquSxypdz785E_tQlMLwN927y7vix98buF-K1j_g6_kLI3O_2Xf2IDFY3eM7l-i0LjqL04uf_JNB1rx5_2ubw3Uovb0f_hLi3_fH-4D-0fI-3gGvCkcBZw_769GJs29EvZL9lcsXBSw3oX7j1-sb98FiqDPkT_2BOB9vJS2BLyjf9YXh3gi6KsM7yzhc7h69lHuQh4poZFxYT3BZh3JoiU0vi7rg47cFzULQhHcz13wDv1gt-AVvTDz9Af5RC2cZ2SeTY6RG2XFCPFAPhNCZos9RnMhEvQTD3JVTy6yPouvsXCpoB30AZs81IJRV0jArZEo2atIf2NLigoJXtn9XLIwziwS1CQA2gXPUGf_8SzizFWIWqSOjD7rAepuftYTP9_LOZFH8Ql8QjuIZ1DO-0ALW_IhBD3z532Il9qJVsyiL2eSAz_tlvwDZkboUXdYZ3lPMeD3RSGdPLm2b0kelZ6KAzi_3tXx-iRmmwkL5AAtDHQGq03wVvrjW23xDPXf1VubCtROApV3iE9Vx3SWfTA15okvs-D3yV_CvnCWpDSKFl2TQP541rvpUxdJ0EnOvaCgc4QjHGnoGd7neWGJQMkX4BN00489uM9Uuq2s0eeDyPYkXLHk6w2IrzjuyMKvZ6hvk0m6g6xj4dGg7IgE-1c2qBOfxRf0mme-xaBPFV_w6v7g2Qc-Xfi6CzcY2TIDfsTO6CnUhlqYR1pQDDzq_uSfLvFe-G9c-ElD_tSWWGqV5FYjguDM8Tqls8ggvxfI70-vsYBnwNfSa2ghSOYs9RyYBo179ic_EI-OiHHhV6gXtOg80IVrBvydVn2z4Hs4RkHEoJ5A_wGfgO5DI1czSkUUwfmme5oHey1RmcpsqmLHEwNJsaGX3F0jNoRRvg2dwheKx-SRc_Ogc7TSPGiZaaaFT9VMvzlrvxQnwJ_kLIrkA-aDc2lDrLz1UMV6p6SCHoy6nK9dNZML3X06aiBl7iBK_VDoLnyTWzJgl8J440Lfa_xGBlvBBZU7-wJ6lzZzM1WI3ytGDnzjcsLEjgwjqxHF3KqXatZ7qLlIDmEHNYZr6M2Yrw-NN5ZqR0gFvTYFbaN9-gEaD7QaeYN-88GMvtLi7KR87zM_eal8FVcDIaW8tqq3UMPZQw2QG6idzNitAj6Ge1yO_a-ZehTDOaTu0KV21_PSW6jfuJmj04rDRMKsPBT0Q0T0u0ZiV_YBZaY1yglWmW3xcdB7PJxdLdUXYKo_doIWwLWZSRDMQ1ccibFCMCJ696FxfgXHnXoju-zKirDPXLIhA1Rkf1mRiCbEif6mj64PiPlD_ZmP8CYIhXFDXWhT-W3GFw4phEN9OgK-ziJaOXpuN6BpTYXaB7XhQEBjSLFozmueWRryGN8yCdrQoJByFGY8u4L-xaAdJJs1bXoK9xoH4mqrhyRUDp0LX9OM2SxF6w2T4z3v7YuOrjvGxxfiBAOdW-ghbQB5EbUNvxTTSeaJouZJJgxCpYTesBtLGlEGPfO9jn8FeUS3wh8D4Iswc4U4WpXlBT2xCLV0GwUlT0o5iKuMFM7m9p1z99Ds-L32zvNBUuC0ZIA8jLnEc-WJPZ8JxbHghWttFcHcw1SrHfKeO66tu_aURm3IvOC7ce4wY-qPymtTVahVBRgTfYBkbO_ZkM2ya8cUCrjuQM-5LXCUmYihubLr8LgTI5lNwD3xjQeYkU4ur6S9Vmi8NzloPE-7WT9-C-6GlWcv4L-qtqTMzOXOt41DhhZVVr_jwm5zSwM167CSq5Xe2Tt5uO9lf35Q0DnErPxjPH4TThwss1XpZg8MbY6jEZgRnSQSA_R04HQ4t0ky1hGc5y5oDPUmC3JPEZ-gC6xAb3xw1_rCjojbyCnN9Q103Z6Dtq_ioJc9aakd347Ae01ED1z",
    "id": 4
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": ".AspNet.CookiesC2",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "iay6FTZl-h27WN_FnkHc6rV0yNdskOXCNc8jtQZJv6OFGmPW36JIt6FPQ75FXbcVZdeEK5t4i75IvzQjga_R5FGxTIZTykVeLzD3A7MiAZZlve-jLEdzGg7pzOCM25UiVsxiY-JwkijzR6xfQQxUeRFpFJIcevWtMUsF8xGByqcph9ACpN9lxD3rRF_OSF-o5blXoDPrmGbBcHuMgBzvfeVdeqS-uhXf2aJE9II6T7gFnXatS6H3HgU_ctis8v7qNk0wNH2_QZ4k241u1E3PuAlL7FmZafs0FYRqtb9hkvhjoTUj0m5g71GLk10yHgNeL7GmIZ7UHrTJK0P9YJs5Rmln1WaB7tWNzNsHc4YLugVZ9nuuB3Crzy6uMGrCwbyJ3z01MLk1_T6jd37lzPQNH32rza8YeiqmnSeEIDH07q4sW413j5RHaAL5P-ZyUwNE7jBBm3l1UhYgwMKqW6_ec2T2V4lyhcORWQA8JKOjjDdhOj4P4Yjx4NL2OmyFyiG8T8PPG5N7H8Qjc98vHEXDNNpty0Gm1qx0Z3UH36ZdyNo-K091RXgceo6Sy7RsHf-mO3IQZs1quL9hZX8AnygT9EsNnUEv7UfbKIRE5F7Px6a6Vcqtf8Mn9Phryrh3BZQ-9uqNUxcmDGGJk3zLMxzvwyab0ONTnNaucdsq3umeF_eZde8ERuaUo8dScoGNM87wjuSiEJ-ORKCQiGWmj-bWvJXoHW8_ZHTTBqOP1tyraaZmrf34ven3gkzORhzPh_HUi2_NEurOL7XnhaeBielYycEAftjq2v4H_YLYPbTPQURXPOfuvYpNEsO4sM3MJdovN_uXoTqfD8htZbBd-b_bd2OyNelT59Im30Wc-iMt-u59wt4fn7AVvyxfC9p_UcTnsv8DnVsEcrkF1LvbAR9z0Bva83vfR6NYbOPd2_4DnR9px-GB_H8F8gqbTR34HX3bmsXg0np11LG4avk-X39dgxjjA_7wXBmJgS5-KprfL-W56-R0D1vI_fkVBux_f-6evA3v14XMXf_P5Bnov7V6nnzNDLnbh2PSg6v7vvQ687y37_9fesI7vv7WbWDUktvHaf53pI0_W_wh_l0bbuvxv5H28Jj329AHAp0DGjX_15PuXX9zz9WcjSPu-jY-X00r9Mrlvjudf61p8z5_mr9Nrdv8g1Udx6JL3d_9DfnT4al6rY2G76RKceXDyi77hL9Ffc7I9ftVyX7LOgpj6y0PX-u3XO8yw38bB_So5Hr7FbisPIX4jr-v37-0m6PfRaXq_bBEOWPKeZOqvaTxl569H_VK8kZgcgkd6m77r7_86lEd0SU1xP9uDJsmG0y_-sbmupve91Z_8wovI_Ho95PMI_bfumeZ9f7-L5t13PlenN_5xTqtd37Rv59DZyfJr9HCVCJGpZHMa3-hpw6JxY18uta139Sm-jej2mh9NejuXyUuGQrsKR3ptzunl838Ab4WLYiYXAAA",
    "id": 5
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1656647258,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "ai_session",
    "path": "/",
    "sameSite": "unspecified",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "Sydkf|1656640775208|1656645458284.4",
    "id": 6
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1684068842,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "ai_user",
    "path": "/",
    "sameSite": "unspecified",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "lK4JN|2022-05-14T12:54:02.871Z",
    "id": 7
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "ASP.NET_SessionId",
    "path": "/",
    "sameSite": "lax",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "rya1mw3inwjctvqwvnhzxnd3",
    "id": 8
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1656648118.223389,
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "ClusterUri",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "c46407bb-50f4-4b50-ad1a-d8ba2214cde3=https://wabi-south-east-asia-redirect.analysis.windows.net/",
    "id": 9
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "LoginErrorReattemptCount",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "0",
    "id": 10
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1688019048.83699,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "PowerBISignedInFlag",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "1",
    "id": 11
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1688171525.290628,
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "PowerBIUserSignedUp",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "1",
    "id": 12
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1688180517,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "PreferredLanguage",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "zh-Hans",
    "id": 13
},
{
    "domain": "app.powerbi.com",
    "hostOnly": 'true',
    "httpOnly": 'true',
    "name": "WFESessionId",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": 'true',
    "session": 'true',
    "storeId": "0",
    "value": "a11c3411-1a3f-490a-b030-7f631f4ab42e",
    "id": 14
}
]
def gethtml(url):
    #driver=webdriver.Chrome()#构造一个Chrom浏览器对象用来控制浏览器
    # 打开chrome浏览器
    #没有提示提醒
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)  # 根据具体的url访问网页
    #添加cookie
    for item in cookies:
        if 'sameSite' in item:
            del item['sameSite']
        if 'secure' in item:
            del item['secure']
        if 'httpOnly' in item:
            del item['httpOnly']
        driver.add_cookie(item)  #将cookie 添加到浏览器对象中

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
        time.sleep(6)
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
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[7]/div[2]/span/a').click()
    print('11 点击图表')
    time.sleep(14)

    # 新建一个选项卡
    driver.execute_script('window.open()')
    #转到新建的选项卡
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://app.powerbi.com/groups/me/datasets/ad7ab2ed-3d12-4dfa-b68c-6d7c26290f15/details?ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3')
    print('12 打开新窗口成功')

    #无限循环 目的无限刷线
    i=0
    while True:
        # 转到新建的选项卡
        driver.switch_to.window(driver.window_handles[1])
        '''
        循环刷新数据集
        '''
        # 在新建的选项卡中点开数据集刷新页面
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="content"]/dataset-related-reports-container/dataset-action-bar/action-bar/action-button[2]/button').click()
        time.sleep(2)

        ##刷新数据集
        try:
            # A1
            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
            print('A1成功')
        except:
            print('失效准备使用A2')
            try:
                # A2
                driver.find_element_by_xpath('//*[@id="mat-menu-panel-10"]/div/button[1]/span').click()
                print('A2成功')
            except:
                print('A2失效准备使用A3')
                try:
                    # A3
                    driver.find_element_by_xpath(
                        '//*[@id="mat-menu-panel-11"]/div/button[1]/pbi-office-icon/svg').click()
                    print('A3成功')
                except:
                    try:
                        # A4
                        driver.find_element_by_css_selector('#mat-menu-panel-30 > div > button:nth-child(1)').click()
                        print('A4成功')
                    except:
                        try:
                            # a5
                            driver.find_element_by_class_name(
                                'mat-focus-indicator app-bar-mat-menu-button mat-menu-item ng-tns-c83-55 ng-star-inserted').click()
                            print('a5成功')
                        except:
                            print('全部失败')

        print('13 开始刷新数据集')
        time.sleep(60)
        print('14 数据集刷新成功')

        #回到报表页面
        driver.switch_to.window(driver.window_handles[0])
        print('15 回到第一个选项卡')
        #刷新数据表
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="reportAppBarRefreshBtn"]').click()
        time.sleep(20)
        print('16 数据表刷新成功')

        # 点击图表全屏下拉框
        try:
            #b1
            driver.find_element_by_xpath('//app-bar//button[3][@aria-label="视图"]').click()
            print('b1成功')
        except:
            try:
                #b2 成功两次
                driver.find_element_by_xpath('//app-bar//button[3][@aria-label="视图"]').click()
                print('b2成功')
            except:
                try:
                    #b3
                    driver.find_element_by_xpath('//app-bar//button[3][@aria-label="视图"]').click()
                    print('b3成功')
                except:
                    try:
                        #b4
                        driver.find_element_by_xpath('//*[@class="exploration-container-app-bars"]/app-bar/div/div[2]/button[3]').click()
                        print('b4成功')
                    except:
                        try:
                            #b5
                            driver.find_element_by_xpath('//*[@class="exploration-container-app-bars"]/app-bar/div/div[2]/button[3]').click()
                            print('b5成功')
                        except:
                            try:
                                #b6
                                driver.find_element_by_class_name("mat-menu-trigger rightActionBarBtn active").click()
                            except:
                                print('b系列全部失败')

        print('17 图表下拉框展开成功')
        time.sleep(6)
        try:
            #c1
            driver.find_element_by_xpath('//*[@id="mat-menu-panel-38"]/div/button[1]').click()
            print('c1成功')
        except:
            try:
                #c2
                driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                print('c2成功')
            except:
                print('c系列全部失败')

        print('18 图表全屏成功')

        time.sleep(120) #2分钟刷新一次
        i=i+1
        print('第'+str(i)+'次刷新')

url='https://app.powerbi.com/groups/me/reports/e7d0d8c2-ea93-4e77-b4a0-415cc77d6448/ReportSection?ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3'
w=gethtml(url)

print('19 关闭浏览器')



























