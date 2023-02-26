'''
for循环是根据range函数产生的序列进行的  range()函数中的step(步长)就是循环变量的变化
for 循环变量 in range:(start(初始值),stop(终止值),step(步长)):
    循环体

#有(start,stop ,step)
#只有(stop)
#(start,stop)
#共有三种情况

for i in range(0,5,3):#（start（初始值）,stop（终止值）,step（步长））
    print(i)


for i in range(4):#只有（stop（终止值））
    i=i+1
    print(i)

for i in range(1,3):#只有（start(初始值),stop(终止值)）
    print(i)


#for循环用break中断循环

for i in range(4):#只有(stop）终止值
    if  i%2==1:
        break
    print(i)


#从键盘输入一个数(n)计算从0到这个数的累加和1+2+3+...+n
n=int(input('请输入你想要输入的数'))
print(sum(range(n)))


tff#使用while循环键入一个数（n）计算从零到这个数的累加和
i=0   #设计一个变量存储累加值
n=float(input('请输入一个数')) 
m=1   #循环变量赋初值
while m<n:#确立循环条件
    i=i+m
    m=m+1   #循环体中包含循环变量的变化
print(i)


#应该避免 step=0 的情况出现 否则就没有了循环变量的变化 for循环就没有办法进行
for i in range(1,5,0):
    print(i)

#Python for循环可以遍历任何序列的项目，如一个字符串或者一个列表

for i in '王凯旋':
    print(i)


for i in [58,96,85]:
    print(i)

#使用for循环range()函数len()函数遍历序列的项目和索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i])   #也可以 print(str(i)+ a[i])


end：在for(while)循环中，每次输出都是换行的。加入end，关闭自动换行，
将结果输出在同一行，或者在输出的末尾添加不同的字符  例如 end="王凯旋的乘法表"
使用end=""关闭换行 并用 '\n'换行



#循环的嵌套 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j," ",end=" ")
    print('\n')#第二个while循环完毕再换行
        
   


for i in range(1,10):  #---第一层循环用于确定行
    for j in range(1,i+1):# ---第二层循环用于确定一行打印多少公式
        print(str(j)+"x"+str(i)+"="+str(i*j),'  ',end='') # ---打印公式
        if i==j:
            print('\n')
        

for i in range(1,10):  #---第一层循环用于确定行
    for j in range(1,i+1):# ---第二层循环用于确定一行打印多少公式
        print(j,"*",i,"=",i*j,' ',end='') # ---打印公式
        if i==j:
            print('\n')
      

i=('123648')
for i in i:
    print(i,end=" ")#关闭自动换行将结果输出在同一行


#for循环嵌套打印1,2,3这三个数字的所有排列

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and j!=k and i!=k:
                print(i,j,k)

'''
#再循环中使用 break（直接中断循环）和 continue（回到循环开始处继续循环）
#  += 和 -= 是赋值运算符
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')


'''
n = 5     # 循环变量赋初值
while n > 0:#确立循环条件
    n -= 1    #循环变量的变化
    if n == 2:
        continue #if条件表达式逻辑值为true(对)时执行跳回循环开始除继续循环
    print(n)
print('循环结束。')


# python 打印图案
 *
 ***
 *****
 *******

for i in range(4):
    for j in range(2*i+1): #(2*i+1)为公式
        print('*',end="")   
    print('\n')
'''
for i in range(4):
    for j in range(2*i+1):
        print('8',end='')
    print()


for i in range(0,5,3):
    print(i)

for i in 'wangkaiusan':
    print(i,end='')






