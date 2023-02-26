# def fun(a,b=1,c=2):
#     print(a,b,c)
#
# fun(89)
# print(fun(89))
#
# print(1,2)
# print(1,2,sep='-')
# print(1,2,end='*')
# print(1,2,3)

# i=0
# while i<4:
#     print('你是第'+str(i)+'个大傻逼')
#     i=i+1
#
# print('循环结束后i的值为',i)

# n=int(input('请输入一个数字'))
# m=1
# s=0
# while m<=n:
#     s=s+m
#     m=m+1
# print('m的值为',m)
# print(s)

# m=0
# s=1
# while s<=5:
#     i=int(input('请输入第'+str(s)+'个同学的成绩'))
#     m=m+i
#     s=s+1
# print('这个五个同学的平均成绩是',m/5)


# i=0
# while i<4:
#     print(i)
#     if i%2==1:
#         break
#     i=i+1
# print('i最后的值为',i)

# while True:
#     m=int(input('请输入1-100之间的数字'))
#     if m<0 or m>100:
#         print('您输入的数字不在1到100之间，恭喜你，循环将退出')
#         break
#     print('您输入的数字在1到100之间，请继续输入')
# s=0
# for i in range(101):
#     s=s+i
# print(s)


# u=[89,'wangkai',90,'op']
# for i in u:
#     print(i)

# s=0
# i=1
# while i<=100:
#     s=s+i
#     i=i+1
# print(s)

# u=[89,'wangkai',90,'op']
# # print(type(u))
# # if type(u)==list:
# #     print('u的类型为列表')
# #
# for i in range(len(u)):
#     print(i,u[i],sep='-',end='*')

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,' ',end='')
#     print()
#
# q=input('请输入一个数字')
# def UI():
#     q1=int(q)
#     print(6+q1)
#
# UI()

# while True:
#     try:
#         import math
#         n=int(input('请输入一个数字'))
#         print(math.sqrt(n))
#         break
#     except:raise
#         print('您输入的数字错误请继续输入')
#


# try:
#     import math
#     n=int(input('请输入一个数字'))
#     print(math.sqrt(n))
# except Exception as iny:
#     print('您的输入有错，爆出的异常是',iny)
#

# print('start')
# try:
#     print('in try')
#     raise Exception('程序出现了错误')
#     print('程序运行结束')
# except Exception as err:
#     print(err)
# import math
# while True:
#     try:
#         n=int(input('请输入一个数字'))
#         if n<0:
#             raise Exception()
#         print(math.sqrt(n))
#         break
#     except:
#         print(n,'是一个小于零的数字，没有办法开平方')

# def fun():
#     print('start')
#     n=1/0
#     print('end')
#
# try:
#     fun()
# except Exception as err:
#     print(err)

def fun():
    print('开始')
    n=1/0
    print('结束')

    print('零不能被作为除数')

try:
    fun()
except Exception as err:
    print(err)














