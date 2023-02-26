import math
'''
while True:
    s = float(input('请输入一个你自己喜欢的数字'))
    if s>=0:
        a=math.sqrt(s)
        print(str(s)+'开平方的结果是'+str(a))
    if s==999:
        break
    else:
        print('负数不能开平方')
print('王凯旋是天才')

while True:
    n=float(input('输入学生的成绩'))
    if n>100 or n<0:
        print('你输入的成绩是无效的请重新输入')
    elif n>=90:
        print('优秀')
        break
    elif n>=80:
        print('良好')
    elif n>=70:
        print('及格')
    elif n<70:
        print('骚年，你连及格都没有达到')
'''
while True:
    n=float(input('请输入一个数字'))
    if n>100 or n<0:
        print('你输入的数字不合理')
    elif n>=90:
        print('你好你是优秀')
        break
    elif n>=80:
        print('你好你是良好')
    elif n<=70:
        print('你好骚年你还没有及格，请你继续努力吧')



n=True
while n:
    n=int(input('请输入一个你喜欢的数字'))
    if n==90:
        print('你可是一个大天才啊')
    elif n>=80:
        print('优秀')
        break
    elif n<=70:
        print('你太垃圾了，我劝你还是重开吧')
