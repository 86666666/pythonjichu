from turtle import *    #引进turtle库所有函数
from random import *    #引进random库用以产生随机数
from math import *      #引math库，用于科学计算
def tree(n,l):          #定义函数tree（）方便引用
    pd()    #下笔
    #阴影效果
    t = cos(radians(heading()+45))/8+0.25   #heading（）用于获得当前海龟的角度，radians（）用于角度弧度转换
    pencolor(t,t,t)     #画笔颜色设定（根据上一条指令，用角度计算颜色）
    pensize(n/3)        #设定画笔宽度
    forward(l)          #向前画一条线l长，即画树枝
    if n>0:
        b = random()*15+10 #右分支偏转角度,random（）用于产生0到1的随机数
        c = random()*15 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度，产生一个随机长度，且一定小于l，最长是0.95倍l
        #右转一定角度,画右分支
        right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        left(b+c)
        tree(n-1,d)
        #转回来
        right(c)
    else:
        #画叶子
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)       #画圆，即枝末叶子
        left(90)
        #添加0.3倍的飘落叶子

        if(random()>0.7):
            pu()
            #飘落
            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
            #画叶子
            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            pu()
            #返回
            t=heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()                #抬起画笔
    backward(l)         #退回
    bgcolor(0.5,0.5,0.5)    #背景色
ht()                   #隐藏turtle
speed(0)                #速度 1-10渐进，0 最快
tracer(0)            #屏幕更新速度 最快：0   快：10  正常：6   慢：3   最慢：1
pu()#抬笔
backward(100)
left(90)#左转90度
pu()#抬笔
backward(300)#后退300
tree(10,100)#递归7层
done()          #结束


