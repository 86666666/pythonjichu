'''
在Pyhon中程序运行时出现错误后程序会终止，这种错误不是程序设计的错误，而是在
程序运行中因数据输入不正确而导致的运行错误，称为运行时错误（Runtime Error）,
处理这种错误要用到try/except异常处理语句

Pyhon 的try/cxcept异常处理语句
try:
    语句块1 #若语句块1能全部正确执行完毕，则try语句执行完毕
except Exception as err:
    语句块2 #语句块1出现错误被except捕获后转化为Exception异常类对象后执行语句2

#注：若语句块1执行到某一句语句出现异常就转语句块2执行，语句块1剩余语句不再执行


 #正确的格式
import math
n=input('请输入你想输入的数字进行开平方运算')#输入语句里有一部分在try语句里执行
try:
    n=int(n)  #数字类型的转化在try语句里进行
    print(math.sqrt(n))
    print('循环结束')
except Exception as err:
    print(err)
print('循环结束')


 #正确的格式  
import math
try:
    n=input('请输入你想输入的数字进行开平方运算')#输入的语句全部在try语句里执行
    n=int(n)
    print(math.sqrt(n))
    print('循环结束')
except: Exception as err:
    print('你错了请重新输入')    #也可以 print('王凯旋是天才'+str(err))
print('循环结束')


 #错误的格式 
import math          #输入的语句在try语句之外执行
n=float(input('请输入你想要输入的数字进行开平方运算'))#应该在try语句里执行
try:
    print(math.sqrt(n))
    print('循环结束')
except Exception as err:
    print(err)
print('循环结束')

#异常抛出错误示范

try:
    print(5584)    
    n=1/0     #语句块一执行到某一句语句出现异常就立即转到except语句二执行，剩下语句不执行
    raise Exception('王凯旋')
except Exception as err:
    print(err)
#raise 语句抛出异常（异常抛出语句）



#应用异常处理，输入一个整数，计算它的平方根。用到try/except语句
import math
while True:  #无限循环
    try:    
        n=int(input('请输入一个数'))
        if n<0:    #if条件逻辑值为true(正确) 达到条件抛出异常
            raise Exception('不能输入负数')
        break    #控制循环的退出
    except Exception as err:
        print('输入错误：',err)
print(math.sqrt(n))
print('程序结束')
'''

#python简单异常语句 不关心异常信息只要捕获到异常就可以
import math
while True:  #无限循环
    try:    
        n=int(input('请输入一个数'))
        if n<0:    #if条件逻辑值为true(正确) 达到条件抛出异常
            raise Exception()   #异常信息为空白
        break    #控制循环的退出
    except:                    #没有写Exception as err:
        print('输入错误,请重新输入，必须要输入整数')
print(math.sqrt(n))
print('程序结束')


'''
python简单异常                           Python复杂异常                               python简单异常语句
                                                    
    try:                                    try:                                        try:                                        
        语句1                                   语句1                                       语句1
    except Exception as err:                    if 条件：                                except:
    pritn('输入你想输入的提示语句',err)              raise Exception ('异常信息')             print('输入你想提示用户的错误信息')
                                            except Exception as err:
                                                        print(err)

            
'''       
    
'''
#异常处理与测试文本有多少个单词
try:
    with open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','rt') as ui:
        yi=ui.read()
        print(yi)
except Exception as err:
    print(err)
ji=yi.split()
print(len(ji))
  
    
