'''
定义（建立）函数

def 函数名称（形参）:   def jkk(a,b,c):       
    函数体                  d=(a*b*c)
                            d=78+d
                            print(d)


调用函数

函数名（实际参数）      jkk(5,6,3)
#实际参数可以由键盘获取
#实际参数可以由用户输入

#函数返回值return+表达式
return +表达式  语句用于退出函数，选择性地向(函数)调用方返回一个表达式的值


def jkk(a,b,c):   #定义函数
    d=(a*b*c)
    d=78+d
    print(d)
    


a=int(input('请输入一个数：'))
b=int(input('请输入一个数：'))
c=int(input('请输入一个数：'))

jkk(a,b,c)     #调用函数



def fun(x):
    print(x)
    if x<0:   #达到条件执行return选择性返回函数值并退出函数
       return
    print(x*x)

fun(5)

def fun():
    return print('王凯旋是天才')
fun()   
'''

#def 定义函数 while循环判断一个数是否为素数

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
                print('n是素数')
                return('n是素数')
            else:
                print('n不是素数')
                return('n不是素数')
        except:
            print('输入的数字错误，请重新输入')
            return('你输入的数字无效')
    print('你好循环结束')


q=wangkaixuan()
print(q)

