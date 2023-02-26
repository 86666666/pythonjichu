import requests
# url=' http://111.200.241.244:54101'
# print(requests.get(url).text)
url2='http://111.200.241.244:49703/?a=1'
b={'b':2}
print(requests.post(url2,data=b).text)