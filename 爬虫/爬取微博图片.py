import requests
'''
r=requests.get("https://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/33/2018new_xixi_org.png")
print(r.status_code)
with open('weibo.png','wb')as i:
    i.write(r.content)
print('下载成功')
'''
headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'cache-control': 'max-age=0',
    'authority': 'developer.mozilla.org',
    'cookie': '_ga=GA1.2.541029757.1586226540; _gid=GA1.2.767250102.1587811123; lux_uid=158781112654359811; _gat=1',
    'referer': 'https://blog.csdn.net/wcg541/article/details/98469880?ops_request_misc=&request_id=&biz_id=102&utm_source=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-7',
}

r = requests.get('https://developer.mozilla.org/zh-CN/docs/learn', headers=headers)


print(r.status_code)