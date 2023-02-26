c=int(input('请输入a的值'))
d=int(input('请输入b的值'))
def max(c,d):
    if c==d:
        c1='您输入的'+str(c)+'和'+str(d)+'一样大'
    elif c>d:
        c1=c
    elif d>c:
        c1=d
    #print(c)
    return c

print(max(c,d))

def laji():
    for i in range(8):
        print('你是大傻逼')

laji()

#比较哪两个数字最小
def min(a,b):
    d=a
    if a<b: #找出最大值最小值只有大于等于符号上面的变化
        d=b
    else:
        d=a
    return d
print(min(6,8))

def fun(x,y):
    print('函数内的变量')
    global p
    p=800

    global h
    y=900

p=100
h=200

print('调用函数之前x和y的值'+str(p)+str(h))
fun(p,h)

print('调用函数之后x和y的值',p,h)

ui=90
def enter():
    global sf
    global city
    sf=input('请输入你所在的省份')-
    city=input('请输入你所在的城市')

def show():
    #函数内部的使用的变量在函数内部没有创建时 使用的是全局变量
    print('你好你所在的省份是'+sf+'城市是'+city+'你的年龄是'+str(ui))

enter()
show()







