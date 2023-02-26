
'''
#while循环判断输入的一个正整数是否为质数
i=2
n=int(input('请输入一个数'))
while i<n:
    if n%i==0:
        break
    i=i+1   #while循环结束后 i=n由循环变量的变化条件得出的
if n==i:
    print(n,'是质数（素数）')
else:
    print(n,'不是质数')
'''

#while有限次数循环

i=0
while i<5:
    print(i)
    i=i+1   # python中的赋值运算符 a+=1等同于a=a+1 a+=2等同于a=a+2
print(i)


i=0
while i<5:
    print(i)
    i+=1     # python中的赋值运算符  a+=1等同于a=a+1 a+=2等同于a=a+2
print(i)
'''
    

    
    
