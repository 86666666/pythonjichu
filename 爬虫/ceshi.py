from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import re




#加载启动配置 从本地直接读取cookie
option = webdriver.ChromeOptions()
option.add_argument(r'C:\Users\86666\AppData\Local\Google\Chrome\User Data')
'''
刷新数据集
'''
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
    "value": "H4sIAAAAAAAEAJ1Yy3arurL9onMHApO93Aw2wiaWCEIPUGcPQE4wCBsnOMZ8_S281nl1buM2MghIKklVs2bN8vERN1VUn5JTnIl5j-hp_73vx0Fv9i_7tvYp33sJ1yHh3ZS2TZjOnx6Z4ygROkhnGrAt8eC5JaFwkm3n0zY8HTbxiubpYtPK7oIKG38V_dCWu4HQDM3cY0mCg4AKO0pHLPOdY_66zH-TKD19pP9zhGMZtZjYr-iMW7IN7_rkIM2L6cBZX7ThmGxpUzwcP9kWE4lCT8MRCX9dzA21RxZzF7Nj93q-_Bw86tQP3yuV31WemQ-9b81m3dJt4ZCtORVgm0SFA7ZPlL-OhUqnIkNdEsUNafcTjWinOfnZn-6nUmFn314m2gqXtsVM-H6CPW9FX5ySNnQpL-A7mUgbgivlqgZXEl6ghIN7efgg2f1UKPQAG6d6Z7rFZoHWlyKnl-VbhmSirSRpT1Bm9YpgbZMQzxWys3ks4dFNpez3Ua5vYMcua6SDE_YcM4Pp5S13fZgjFh9sSjV9P8-dB42O2HNfuNPj0NbToRX3Q9utlvGqx6POIOxdPFTR_fPfNv2fqqfPfeBeAIf9g8z7Ge53f75vQ-_Q-S88N1qiDql8kCb0rxmXZTq_3pVl8thNedYjeuykwyWTxEE7zoOy7OIvrpCqBApZ3yTS6WalEDO4e8h-pCV_vXPLNHEmUUbTu0TW4TzGRzvknLN3GQ5fSrIv8oTt-g9sP-9FK-bCjZuDKhzK05FG8kRO6FS0ujuo9EF7wFNLm4SnDs2ea2_1LraVXM_lE3cxP_BwpJkD8XIAVwKRtliR7d4_8L37xNx2wdvnSOZPn2yLx-IXenJm2kJCbMDmOUC_be1h7iv46_VOhAxg7YoJFi4-r_vPZfx-6LDiAiPjsq8jDjIhJTY525moczPVCN4yLwnjfabYRe3iSES1e5RWi_x1LFG8kSFOi8fq9MQhYOLPvvdC-QPpdJjlUsqeokrSdzZrTNRAmF1_UPQ5lm66ykJ7Pgjws2yyzDFPnJvIdkvMizl16fbVK_r9SHnQ043jFAtuFO6ICke9bU7FggnOWh0BiSxrYd86l_Y_cHhacHg4m6bqzauJMKw3j8qT90NPf6rMb6slhmd5h-fLvn9i8GZcfNNO4BRwT-3FPyZ_vRXueoQ1t-c-ORuWM5Z57CfcehWOL4xrT6P4i25lQ0ITpEt8z9rWi902vJFnbMygd0-OONHZ9pC7jt44s1YFxDeF-HbAL6FDHo5H-_2UcGaTLWBg2y0-vhe9nXVOASvr2x-8NIQDT83ptOCl4LQHOz7w0li0EPuN4-mFKwCPhdo7pBf_tONU7veTKo_icteyCUqxHrJuVETigYf0rYziXeHa91IMXOZDTIQ_ZDmNq76edEhj2tlr1mOpwvjAOVYG2bEO41z2TSnaOFIylvUO4u41ORc6E5jy5_qc3VX3_1zfdjedWzgby4V6nu1Hh01mXPpSeZoA5pCSZkUVeVRA-1XP4K4oM30681yeKlnc-ZZu4P0hz1ZXanSVbDZ1aAfj2kaF_kumhh_g2r1ogzYLHZfvOv_Ysz2s70g_IdXVPnGpT3MJ07ALvMNI54cpp7oSwBOWbSrhb8k20KWVHscmKh2Us5yVLGoG4I34KJAQ_VAyJF_4zsa1Y8cqarrU6VzgKQ2-vioe07I3PpcU6kc8Ao_FZb9e8X6QsN9V5fadhXa1xKqK5D5d_NGJx5O3YLzwGgr7z5lCUWm7-emvDv9-7-mQcR2XnfwTa5wn0dOfG9npKO0lT7ZMMaE3wAlRDf5QnT3AuYRq8aUK_Z3e6VJi6cst_mZShhVu3hm-IOno-1EO2Gx1xlSTylC3R-EXigda4bgoOhYJbCS3TVNZ_SW3tGQuDlWPs9JLXTFjVnfPeGg5Yx_icS86e0tbWqbO0P0-L92n56Bc_AXjZ-D1HOoAlWE8cswUnO8K_k4YGgC85E5D58H6gcjo2wH_YcCa0Auvh3LFBX36n51Ny9wJeN0kR2GvlWtpKezirxJyIa921MrWAr7qqQqf44qE-l2cf8dP74KukoC_7R4t8-VvfG4LwCOM_8FXfFGdyf5lv7M-j4b2GE5XmRtS9t9Opuwz3uzMSvG83_hWQy4a1_zXfkn-7_vDfWD9AHEfLoA3TUJfiOf99cBVN5XSXlU_Eomwz3sE9x-uvG_eJQ6hztE_9iTgffgubAF4x__MLwH-xFBXOdlZKuZg9ayjAgE-GWVhh2A8Jt06VHlDWTQu42cTohc9S8ow3A8teId6sBuS0uIX3j33g3jiBs4zcNfGxxCFaT6AP7DHpVTpYo-zTMoY__YHHfWTi6zHozGSiEnWQh2w8UMvGEVSAW47wNdeh-aLWJqXWIrS7ueCB1FqsWRdzOQTz5Bn__UuoxRpzCzWR86e-XCEfHnmk7hMxRyro_wEPmEt-NMv5r1vpC3EOQA982c--EvvZCNn2RczzYCfdkv8ATMD1KgJxnnWMwL4fdHYxE-u7RuahYWrIx_Ob3ZVtD7J2abSAjlACQOdwavOfyu84a2yZIb8b6utTSRu7hIXE_inrCI2q96__8mXbsHvk7-kfRE8TlgYLromhviJtEfJUxcp0EnOlDPQOdKRjurYBeaLLLdU4vgK-ATd9Nse3OdeoEZV-PNBVXOSSC7xegPiy487uvDrBfi1SxXbQdSJdJlftFSB_ZGf9UnM8gq15hlveTanUix4Rb_x7AGfLnzdBhuCbZECPxJncDVuAiO7R5IzAjyKfsefLf5e-G_gQiAq4zyRMs-wfnDRqDpcS5ZbJWUxATaWeP-uNRbwDPhaag3LJU2dJZ_9rsbDnv-JD_ijpXJY-BXyBS86D3ThmgN_J2VfL_g-H0M_5JBPoP-AT0D34UHoGScyDOF89ynJ_JR3diqdb1QDH6Z5cErC4cOEg1y0nXGKUbcd1Hh7T2fZHHNTZC7U4G7SLNIQT5PUc9wa3HzVrtlTa7JS0FBbfEpRMzKFvqhrX4y4uJWXjrU7gdaiLcXr4BjZstoG31B7xkywIe3rlVzOxmMLcf_h7rozs4Zx-U63uq1l4xvwC8f4W-bBS8VtcZT7SZ2h8Jx1c-y-H4WDrBTrCznXcxmuoAdgbSL1DTghKncYODaYhauvEDenkCxkefBV8OYmIyygLjIVmih3Jw6tm4SeoU_UHc78CzCL3zRi1vR3v-z8huYg_bAphBOH0N69kG5SWkxBBbpW9GQU0PTp-dXn3ToAnpxFZK0OV8ApUGM6vzxipo0CenMaasLO4e4I90VSezIkwDPSMR9lrrsqGoJkB_Vwfp103mgd2rvorACcQw20d9XrBHJpD_f9D300PrTSD_2nPyIbP5AdCkxuutJrUrFwSC4d5rEB8HWR4coxc7MBTduVuHkwG5wpaAwlF805ZqllgYjILVWgDTscMIGDVKQj6F8C2kHx2bC6Z512hjNFxppzHGiHzblnWMptmkQNS5T5KXnzRebmDM-34w6fj3kxV1BHjq39IDuTQu44mWvuB7kmKsI_ql9H8tzBPilSO1Buzrjh_RhneUyl689Ql1EWIsRCH7HZXI5i0iYCjROtaarolCPDq3OMgXuC0hmuoNsf1Ma9dsYROs6D6icrgPPSfvKyc4hAdz6Usj9ajZTYppOuTStu4mom91QOKPdYBnWKkhy0i6fvZVsgAi2FxOBH0HBAcDPv0A50-puKoNjI4QDvV4k_fRHSRPBPl0N-pmcMeUqvcIcvLrq77ug7wXEqukkway-5yzDUy7jisSsUayG_Zo5B52OBVIQC4JQ34nyuiKBf5U5foPnZ855MBjqpuotP3K0R2cUB5EpYzaANwv0EXBdmnumJG7Nlvmw16MXpO7X2rBG5G66vEnhZAk-D1mOA0avxxF30VNV5Y2tJpioHDhAGSfnpHk8O4Iy-QK_9VTsFKm09ZVHcKfE",
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
    "value": "JvD3tQEedsh3wroD64uokn6WsIv9CZ_lWnc1Y7YIXpnRQYirNbrjqEH8UApXSRR8V9E-Fa94I6Pcj9CgH4Z8PnF6pEyt6xknhAoftLk7JmajQOgD956WLnxz_p_agbudBLtHAqNsQcrbg87hJPRwnW7w1kbzzDkMdhhvvtAZu_BG7gVYublg-rER0mSvPKurt52PYDOmZ3UA_R0JeJoNA10YoA5i6WQc8tH31D0qMlUyRRBdHnuW2dOJN1oqHVKioIwp9CIJcwTvdm7eDiKXJQb-4DgJdiqmL-DFkQTUHyHRGGBew6slS9GOW4L1Xt1TwLaP83LyQcOrJLpi5Mre6xYdjqwnkUUkdibKZIC4NLc9UaEShBtMPzYGdbQd4KabcpXEmnphmzEEdcYe3g1qe-1XhMNCVdpt7TUu3NJNiHEWvC9Cl7_ThQI1Y_1Qu8CJnbxl_dYpZQrEKOtE1I9hzEiEn1qNUtHove32h7ngphJ_XecD5edhlSMZVOFniBUlhzcp0_k3szJlifa3C8ZRyMyhMe4nil4NkVkLeGcygp6NnCjcAJY_KVnppHoPGXDfSma6UY_A7PhSZ4yV5N0oub9wGkkQG9miCIg9ksgsfxNP5scM8VXrPwnEuHXmg3EK_A7Wdv7pHix-lG7-psPmAnsarrNxKuQZG0--sxz_EFSshBiBpsypd6Jxd3ZfOtNXOHr6vR6jhuX72ygH00-yndOWqjuzjuPwm1O7vpN2PZFvDX_gJffAL4Z8vdMvKpQ9PgX_LSN5MZNsCevLK9dO6X991HjulkvPC20d0PzEYhzk_VY8fR3k_Jeex3p98e9wFQ93LOd_sX_JNHNV9973fvk77cEDV5vVBtvsHvPtJG66SNnX2IfQY-H46LH_Qi9eetBr-TyzscY6Hw-b1TrLgzaj7JwEeJKfXe7K9TKS9LN93oB3q_dn5hr3iGgW2PtOh9pitzvC9HfpCTbPOpnpvY6vBB1oBMvN4WM5XneV3tYGx7p_7SmCM33v_3su5A9buRKb_sef3nWzh-efMLG_uZR7bGv0fa_llgvUO3fz32hR4rvJM9s-a-K8z7Zzlp9OqrWxWPv52EV7f0F9bdkLiZOWvt5G2gZbHY3uxm79XTfhji7wjSH98_Lz-Mubvj-A6Hepj_DX_-vKcXz3D6d_Cf-mu28vneJs_nL-3n-ofpBwQf-AT-ogelwfUaP22bvi17X6CvwSJkmF4u7j317ewbq8vuC11vLs1eemyNzeb_0E_P6vj2_Wvv4Li-iv_GmR6fnfK422brVX-TS8XvZ_uF_V9JF62uZ27AH-uV2v_6_jx1-W0Nnb1dXvZJ8F6rK-S3YdfvoncFa_5-4ftv8uHkXlHx-jXdHi9bF52hWr92b5Gw-pbq-bvd_uer_rz7fX88w-e3fg-QO3d__v8ObzfyHvQbK_r_K9v5ZNVCGgw6nj6groVjgrl6f8CdfIZ5igXAAA",
    "id": 5
},
{
    "domain": "app.powerbi.com",
    "expirationDate": 1656666057,
    "hostOnly": 'true',
    "httpOnly": 'false',
    "name": "ai_session",
    "path": "/",
    "sameSite": "unspecified",
    "secure": 'true',
    "session": 'false',
    "storeId": "0",
    "value": "GHPzK|1656651980452|1656664257853.1",
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
    "expirationDate": 1656667855.144466,
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
    "expirationDate": 1688200254,
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
#加载启动配置



#代码继承于淘宝刷新

def gethtml(url):
    #driver=webdriver.Chrome()#构造一个Chrom浏览器对象用来控制浏览器
    # 打开chrome浏览器
    #没有提示提醒
    driver = webdriver.Chrome(options=option)
    driver.get(url)  # 根据具体的url访问网页
    #添加cookie
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
    time.sleep(14)
    driver.find_element_by_xpath('//*[@id="leftNavPane"]/section/nav/div[1]/button').click()
    print('10 点击工作区')
    time.sleep(4)
    try:
        driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[7]/div[2]/span/a').click()
    except:
        driver.find_element_by_xpath('//*[@id="artifactContentView"]/div[1]/div[2]/div[2]/span/a').click()
    print('11 数据集')
    time.sleep(14)


    #无限循环 目的无限刷新
    i=0
    while True:
        i=i+1
        #点开数据集刷新页面
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
                    driver.find_element_by_xpath('//*[@id="mat-menu-panel-11"]/div/button[1]/pbi-office-icon/svg').click()
                    print('A3成功')
                except:
                    try:
                        # A4
                        driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                        print('A4成功')
                    except:
                        try:
                            # a5
                            driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/button[1]').click()
                            print('a5成功')
                        except:
                            print('全部失败')

        print('13 开始刷新数据集')
        time.sleep(120)
        print('14 数据集刷新成功')
        print('第'+str(i)+'次刷新数据集成功')
        time.sleep(300)

url='https://app.powerbi.com/groups/me/list?ctid=c46407bb-50f4-4b50-ad1a-d8ba2214cde3&language=zh-Hans&refreshAccessToken=true'
w=gethtml(url)

print('19 关闭浏览器')



























