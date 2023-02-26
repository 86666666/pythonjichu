#while循环
'''
1,确立循环变量（循环如变量赋值）
2，确立循环条件
3，循环体（内包含循环变量的变化）


i=0
while i<4:
    print(i)
    i=i+1
print('i的值是',i)

n=0
while n<3:
    print(n)
    n=n+1
print('last',n)#打印到2，但是i=3


#计算s12+3+4+5+++n
n=int(input('输入一个你喜欢的数字'))
s=0
m=1#循环变量赋初始值
while m<=n:#确立循环条件
    s=s+m #循环体
    m=m+1
print(s)
print('m的值'+str(m))


n=float(input('请输入一个数字'))
s1=0
m1=1
while m1<=n:
    s1=s1+m1
    m1=m1+1
print(s1)
print(m1)
'''

# #输入五个学生的成绩，计算平均成绩
# s=0 #设置s存储总成绩
# a=1 #确立循环变量
# while a<6: #确立循环条件
#     m=float(input('请输入第'+str(a)+'个学生的成绩')) #循环体中包含有循环变量的变化
#     s=s+m
#     a=a+1
# print(s/5)

s=0
a=1
while a<6:
    n=float(input('请输入第'+str(a)+'个学生的成绩'))
    s=s+n
    a=a+1
print(s/5)

