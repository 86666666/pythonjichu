'''
import os
if os.name=='nt':
    print('你的操作系统是Windows')
elif os.name=='posix':
    print('你的操作系统是Linux')
else:
    print('你的操作系统是其他')




try:
    import requests
    r=requests.get('http//www,baidu.com')
    a=r.status_code
    print(a)
except Exception as err:
    print(err)
    
'''
import re
