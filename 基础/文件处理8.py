'''
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

 
print("1 到 %d 之和为: %d" % (n,sum))

import re
print(re.escape('www.python.org'))

import math
while True:
    try:
        n=int(input('请输入你喜欢的数'))
        if n<0 or n==0:
            raise Exception('n不能小于零')
        print(math.sqrt(n))
        print('计算结束')
    except Exception as err:
        print(err)
print('全剧终')


#异常处理与测试文本有多少个单词
try:
    with open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','rt') as ui:
        yi=ui.read()
except Exception as err:
    print(err)
ji=yi.split()
print(len(ji))





#用函数来处理文件
def count_words(filename):
    try:
        with open(filename,'rt') as ui:
            yi=ui.read()
    except Exception as err:
        print(err)
    ji=yi.split()#读出文件的变量不能在函数外使用
    print(len(ji))

filename=('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt')
count_words(filename)

import json

nu=[2,3,4,5,6,7]

try:
    filename=('C:\\Users\86666\Desktop\自己编写的Python程序\numbers111.json','wt',encoding'utf-8')
    with open(filename) as wenjian:
        json.dump(nu,wenjian)
except Exception as err:
    print(err)

'''

nu=('[1,2,45,43]')
filename='C:\\Users\86666\Desktop\自己编写的Python程序\numbers111.txt'
with open(filename,"wt",encoding='utf-8') as hi:
    ju=hi.read()
    ju.write(nu)














































    
