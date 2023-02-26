'''
x=2
y=3
r=4
NAME=('你是不是一个大笨蛋')
print(x,y,r)
print(x,y,x+y)
print('王凯旋可是一个天才啊')
'''
# import math
# while True:
#     s=float(input('请输入一个你自己喜欢的数字'))
#     if s>=0:
#         s=math.sqrt(s)
#         print(str(s)+'开平方的结果是'+str(s))
#     elif s==999:
#         break
#     else:
#         print('负数不能开平方')
n='256'
u=3
y=123.2
print(type(n),type(u),type(y))
n=int(n)
n1=float(n)
print(type(n),type(n1))
print(n,n1)
print('%6d'%22)
#'%wd'%整数 w为位数
print(len('%6d'%22))#%wd输出一个整数，如果w大于零，则右对齐，如果w小于零，则左对齐，
print('%-12d'%6666)#左对齐
print('|%012d|'%6666666)
print('|%-012d|'%6666666)


#输出时间和日期
#输出时间和日期（王凯旋）
year=201.5
month=2
day=1
hour=8
minute=12
second=0
print('现在的时间是：： %04d-%02d-%02d----%02d-%02d-%02d'%(year,month,day,hour,minute,second))
print('现在的时间是')



#浮点数的格式化输出
m=12.124514132
print('|%6.2f|'%m)#保留两位小数
print('|%-10.1f|'%m)#保留一位小数 负数要左对齐


#字符串的格式化输出

m='王凯旋是天才，王凯旋是天才'
print('|%-20s|'%m)#左对齐
print('|%20s|'%m)#右对齐
print('王凯旋可是一个大天才啊')
print(8//5)
print(3>4)
print(3<4)

#输入一个数输出它的绝对值
n=int(input('请输入一个数字'))
if n>=0:
    print(n)
else:
    print(n)

#输出学生的成绩然后输出学生成绩的等级
while True:
    n=float(input('输入学生的成绩'))
    if n>100 or n<0:
        print('你输入的成绩是无效的请重新输入')
        break
    elif n>=90:
        print('优秀')
        break
    elif n>=80:
        print('良好')
    elif n>=70:
        print('及格')
    elif n<70:
        print('骚年，你连及格都没有达到')