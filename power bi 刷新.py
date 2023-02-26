import requests
import time
from datetime import datetime




a='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSIsImtpZCI6IjJaUXBKM1VwYmpBWVhZR2FYRUpsOGxWMFRPSSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvYzQ2NDA3YmItNTBmNC00YjUwLWFkMWEtZDhiYTIyMTRjZGUzLyIsImlhdCI6MTY1NjMyMDY0MywibmJmIjoxNjU2MzIwNjQzLCJleHAiOjE2NTYzMjYzMDEsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVFFBeS84VEFBQUFzU3B6R3hoMkFWN1hiS0hkdGxLbVpUVjIxTmJTNG43emw3Mk5IaThZME8yVHk1VnFqVlhYTXU0MC9pR1ZBUzhuIiwiYW1yIjpbInB3ZCIsInJzYSJdLCJhcHBpZCI6Ijg3MWMwMTBmLTVlNjEtNGZiMS04M2FjLTk4NjEwYTdlOTExMCIsImFwcGlkYWNyIjoiMiIsImRldmljZWlkIjoiODE1YzcyZjQtYzBiNy00OWI3LWJlNTItYzg5Yjc1MDAxZDU5IiwiZmFtaWx5X25hbWUiOiJXQU5HIiwiZ2l2ZW5fbmFtZSI6IkJpbGwiLCJpcGFkZHIiOiIxMTYuMjMzLjc4LjE3OCIsIm5hbWUiOiJCaWxsIFdBTkciLCJvaWQiOiI4MGI1M2NiYS1mNDU0LTRlYjItYmI2ZC1kMjZhMGYzYTk0NDUiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTE1NTI2ODAyOS0yNjg2MTA5MTE4LTM4OTA2MjkyMjYtMzY0MzQiLCJwdWlkIjoiMTAwMzIwMDFFQTg2OEVERCIsInJoIjoiMC5BVk1BdXdka3hQUlFVRXV0R3RpNkloVE40d2tBQUFBQUFBQUF3QUFBQUFBQUFBQlRBUGMuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiYTBxenZwUlhpaG1vT1VOUGFjOEpzSXMyZ0tyZnJfTU16U1dWOGZXbGZ6ayIsInRpZCI6ImM0NjQwN2JiLTUwZjQtNGI1MC1hZDFhLWQ4YmEyMjE0Y2RlMyIsInVuaXF1ZV9uYW1lIjoiYmlsbC53YW5nQHRhcC1ncm91cC5jb20uY24iLCJ1cG4iOiJiaWxsLndhbmdAdGFwLWdyb3VwLmNvbS5jbiIsInV0aSI6IlNHa3hxUE5zQ0U2aGJKQURLb3FyQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.lLvALr7DwStb0PDLCEk0rsp_ygaamVmdjLp8Vxp8zhhmQPqJ0FWfC0Qa5qhsUraEEabZ4hRhdl2YY7_nJul0wOwOKNGmFBd0csc-dQ6wiPGZNWLMFwyCbeFVBvFXdYt6_SNYQQ3mfNAmEe6AxliegSpLOhZlotiwD6dYTgKzTkdPLkQliQkD1AwRMVBh-uP1DgzG0TM4d2NHoN7-yAD4KIHjdsmNKl9lJzd2_VR8cobLqx4th9iirAR_V28ruX-Ql8G-SYPkOItmw-Z0EkHvcIlz_golGvh9wYKW7qulXErWBRFT1yLTfnl5hqR_SWCIGl300CXM4mp7YXlCD0xyEA'
headers = {
'Host': 'wabi-mc-sha-redirect.analysis.chinacloudapi.cn',
'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept': 'application/json, text/plain, */*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'ActivityId': 'a20c5d78-b651-41b6-9375-6118605cd6e2',
'RequestId': 'f9d60746-5257-74f5-28c5-213b56b464ad',
'Authorization':a,
'Content-Type': 'application/json;charset=UTF-8',
'Origin': 'https://app.powerbi.cn',
'Connection': 'keep-alive',
'Referer': 'https://app.powerbi.com/',
'Content-Length': '0',
'TE': 'Trailers'}

refresh_url= 'https://wabi-south-east-asia-redirect.analysis.windows.net/powerbi/content/packages/8786261/refresh/'
response=requests.post(refresh_url,headers=headers)
print(response.status_code)
#print(response.text)

# while True:
#     print(datetime.now())
#     response = requests.post(refresh_url, headers=headers)
#     print(response)
#     time.sleep(10)