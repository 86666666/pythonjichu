
#没有形式参数的函数
# def hello():
#     print('wangkkaixuna')
#     print(8*9)
# hello()

# def fun(x):
#     print(x)
#     if x<0:
#         return
#     return(x*x)
#
# x=int(input('请输入一个数'))
# print(fun(x))


# def sum(m):
#     s=0 #m s p 是局部变量
#     for p in range(m+1):
#         s=s+p
#     return s
#
# m=10 #m s 是全局变量
# s=sum(m)
# print(s)

#函数中使用到主程序的全局变量要使用关键字 global
# def fun(x):
#     global  y
#     y=0
#     x=0
# x=1
# y=2
# fun(x)
# print(x,y)

# def a(x):
#     global  y
#     y=0
#     x=0
#
# def b(x):
#     global y
#     y=10
#     x=0
#
#
# x=1 #全局变量
# y=2 #全局变量
# a(x)
# b(x)
# print(x,y)

# def enter():
#     global sf
#     global cs
#     sf=input('请输入你的省份')
#     cs=input('请输入你的城市')
#
# def show():
#     print('你好你的省份是'+sf,'\t\n','你的城市是'+cs)
#
# def main():
#     enter()
#     show()
# main()

print(1,2)
print(1,2, sep='-')
print('line')
print('line',end='*')
print('end')

import bao_1
bao_1.daying()
import sys
print(sys.path)
for i in sys.path:
    print(i)
