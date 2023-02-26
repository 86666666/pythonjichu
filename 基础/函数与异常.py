'''
def fun():
    print('要开始了你准备好了吗')
    n=1/0
    print('end')


try:
    fun()
    
except:
    print('你出错了')


# 错误的示范 没有用 try/except捕获异常
def a():
    print('start')
    1/0
    print('enda')

def b():
    print('start b')
    1/0
    print('end b')

b()
print('结束了')

n=23
b=12
f=34
print('%2d:%2d:%2d'%(n,b,f)) #数据的格式化输出
'''

#时间的输入与输出
def shijian():
    n=input("请输入是几时")
    n=int(n)
    if n<0 or n>23:
        raise Exception('输入错误')
    f=input('请输入现在是几分钟')
    f=int(f)
    if f<0 or f>59:
        raise Exception('输入错误')
    s=input('请输入现在是几秒')
    s=int(s)
    if s<0 or s>59:
        raise Exception('输入错误')
    print('%2d:%2d:%2d' % (n,f,s))   # %2d   %分号在前面

try:
    shijian()
except Exception as err:   #不能用简单异常语句
    print(err)






