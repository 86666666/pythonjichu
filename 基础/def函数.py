#def 定义函数 while循环判断一个数是否为素数
'''
def wangkaixuan():
    while True:
        try:
            n=int(input('请输入一个数')) 
            i=2                #循环变量赋初值
            while i<n:         #确立循环条件
                if n%i==0:
                    break
                i=i+1          #确立循环体循环体中要包含循环变量的变化
            if n==i:
                print(n,'是素数')
                break
            else:
                 print(n,'不是素数')
                 break
        except:
            print('输入的数字错误，请重新输入')
    print('你好循环结束')

    

b=wangkaixuan()
print(b)


def wangkaixuan(n):
    while True:
        try:
            i=2                #循环变量赋初值
            while i<n:         #确立循环条件
                if n%i==0:
                    break
                i=i+1          #确立循环体循环体中要包含循环变量的变化
            if n==i:
                print(n ,'是素数')
                break
            else:
                print(n,'不是素数')
                break
        except:
            print('输入的数字错误，请重新输入')
    print('你好循环结束')

    
#实验用的
print(wangkaixuan(7))


def wangkaixuan(n):
    while True:
        try:
            i=2                #循环变量赋初值
            while i<n:         #确立循环条件
                if n%i==0:
                   return ('你好循环结束',n,'不是素数')
                i=i+1          #确立循环体循环体中要包含循环变量的变化
            if n==i:
                return('你好循环结束',n,'是素数')
        except:
            print('输入的数字错误，请重新输入')


print(wangkaixuan(6))


#定义函数判断两个数的最大值   （错误的示范！！！！）
def max(a,b):
    c=a
    if a<b:
        c=b
    print(c)#错误没有用return给函数返回值导致Python默认值为None


a=int(input('请输入一个数'))
b=int(input('请输入一个数'))
d=(max(a,b))          
print(d)

        
#定义函数判断两个数的最大值   (正确的示范！！！！！)
def max(a,b):
    c=a
    if a<b:
        c=b
    return(c)


a=int(input('请输入一个数'))
b=int(input('请输入一个数'))
d=(max(a,b))          
print(d)
    
#间隔开

def wang():
    print('王凯旋是天才')


w=wang()
print(w)


#修改全局变量的值
def wangkaixuan():
    global name    #使用global 调用全局变量
    name=(666)     #x修改全局变量
    return(name)   #选择性的给函数返回一个值并退出函数


name=('hahah')    #全局变量
q=wangkaixuan()
print(q)

#多个函数共同使用全局变量要注意全局变量的值是否被修改
def A(x):
    global y  #调用全局变量
    y=0       #修改全局变量   #没有函数返回值
    x=0
    

def B(x):
    global y  #再次修改全局变量的值    #没有函数返回值
    y=('王凯旋是天才')
    x=0


x=1
y=2
A(x)
B(x)
print(x,y)  


#一个函数获取输入并输出
def shuru():
    a=input('请输入你所在的省份')
    b=input('请输入你所在的城市')
    return(a,b)
    
    
c=shuru()
print(c)


#两个函数一个获取输入一个输出

def shuru():
    global a    #调用全局变量
    global b    #调用全局变量
    a=input('请输入你所在的省份') #修改全局变量的值
    b=input('请输入你所在的城市')
    


def shuchu():
    print('你好啊你所在的是'+a+b)


a=""
b=""
shuru()     #没有返回值的函数智能单独作为一条语句
shuchu()



# and可以用于测试
(A,B)=(8,-9)
if A<9 and B<45:
    print('王凯旋是天才')


def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str = "菜鸟教程")




#python函数定义时可已预先为部分参数设置默认值好处是调用函数的时候不用再提供参数的实际值
def fun(a,b=1,c=2):
    print(a,b,c)

fun(0)
fun(1,2)
fun(1,2,3)


#参数按名称指定
def fun(a,b=1,c=2):
    print(a,b,c)

fun(0,c=4,b=2) #函数调用时实参值是按顺序赋给形参的，也可以不按顺序按指定形参名称而不按顺序调用
fun(b=2,a=34,c=89)


#全局变量和局部变量
def fun(x):
    global y
    x=0
    y=0
x=1
y=2
fun(x)    #定义的函数没有返回值所以不能放在一个表达式中去计算
print(x,y)
'''

# print 函数的默认参数
# print(value,...,sep='',end='\n',file=sys.stdout,flush=False)
print()



