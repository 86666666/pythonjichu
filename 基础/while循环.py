i=0
while i<4:
    print(i)
    i=i+1
n=input('请输入你的名字:')#字符串相加
print('你好'+n+'新年快乐!')

#计算s=1+2+3+....+n的数字之和
n=int(input('请输入一个数'))
print('你输入的数字是'+str(n)+'你真的好聪明啊')
s=0
m=1
while m<=n:
    s=s+m
    m=m+1
print(s)
print(m)

#while循环计算五个同学的平均成绩（成绩由用户从键盘输入）
#1：要设计存储成绩的变量s
#2：在设计一个循环变量i 之后确立循环条件
#3：确立循环体 循环体中要设计循环变量的变化

s=0                 #设计存储成绩的变量
i=1                 #设计循环变量
while i<=5:         #确立循环条件
    m=float(input('请输入第'+str(i)+'个同学的成绩'))#确立循环体
    s=s+m
    i=i+1         #循环变量i的变化
print('下午好！平均成绩为：',s/5)

#while循环的退出break
i=0
while i<4:
    print(i)
    if i%2==1:
        break   #达到条件就用break中断循环并退出
    i=i+1
print(i)

#while无限循环 控制循环条件的逻辑表达式的值永远为true

i=8
while i:print(4+5)

'''
简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，
你可以将该语句与while写在同一行中
'''
#while无限循环 控制循环条件的逻辑表达式的值永远为true
i=89
while i: #循环条件的值永远为true
    m=(input('请输入一个数：'))
    print('你输入的数是'+str(m)) #循环体中没有循环变量的变化
print('滚蛋吧智障')

#while true 实现无限循环
while True:
    m=int(input('请输入学生的成绩'))
    if m>=0 and m<=100:
        break
print('你好学生的成绩为'+str(m)+'!')

#while循环中使用else语句

count = 0 #或者count=float(input('请输入一个数')) #设置循环变量
while count < 5:  #循环条件
   print (str(count)+" 小于 5")
   count = count + 1 #循环变量的变化
else:
   print (str(count)+ " 大于或等于 5")

