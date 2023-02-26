'''
class Person():
    def __init__(self,name,gerder,age):
        self.name=name
        self.gerder=gerder
        self.age=age
        
    def show(self,):
        print(self.name,self.gerder,self.age ,end=' ')#end=''关闭自动换行

    def display(self):
        print(self.name,self.gerder,self.age,end=' ')
        
class Student(Person):
    def __init__(self,name,gerder,age,major,dept):
        Person.__init__(self,name,gerder,age)
        
        self.major=major
        self.dept=dept
        
    def show(self):
        Person.show(self)
        print(self.major,self.dept)

    def setname(self,name):
        self.name= name

    
s=Student('james','male','20','software','computer')
s.show()
s.setname('robert')


class Person():
    def __init__(self,name,gerder,age):
        self.name=name
        self.gerder=gerder
        self.age=age
        
    def show(self,end='\n'):
        print(self.name,self.gerder,self.age ,end=end)#end=''关闭自动换行

    def display(self,end='\n'):
        print(self.name,self.gerder,self.age,end=end)
        
class Student(Person):
    def __init__(self,name,gerder,age,major,dept):
        Person.__init__(self,name,gerder,age)
        self.major=major
        self.dept=dept
        
    def show(self):
        Person.show(self,' ')
        print(self.major,self.dept)

    def setname(self,name):
         self.name= name

    
s=Student('james','male','20','software','computer')
s.show()
print(s.setname('robert'))



n=int(input('请输入今天的天气'))
if n>=26:
    print('请穿t桖')
elif n>=20 and n<26:
    print('请穿衬衣')
elif n>=10 and n<20:
    print('请穿毛衣')
else:
    print('请穿羽绒服')





n=int(input('请输入你的体温'))
print('你好你的体温是:'+str(n))
if n>38:
    print('请送医院隔离')
elif n<=38 and n>=36:
    print('正常体温不用担心')
else:
    print('体温不合理，请重新测体温')






#输入七个人的体温并统计医院隔离的人数，居家隔离的人数，自由活动的人数

i =float(input('请输一号人的体温'))
h=float(input('请输二号人的体温'))
o=float(input('请输三号人的体温'))
y=float(input('请输四号人的体温'))
p=float(input('请输五号人的体温'))
j6=float(input('请输六号人的体温'))
j7=float(input('请输七号人的体温'))
j8=float(input('请输八号人的体温'))

ui =[i,h,o,y,p,j6,j7,j8]
(q,w,e)=(0,0,0)
for k in ui:
    if k>38:
        q=q+1
    elif k<=38 and k>=36.8:
        w=w+1
    else:
        e=e+1
print("医院隔离人"+str(q)+' '+'居家隔离人数'+str(w)+ ' '+'自由活动人数'+str(e))


op=8989
print('王凯旋是世界上少数几个天才了'+str(op)+'!!!!!!!')
a=('5656')
b=('jfajagjoijwangkaixuan')
print(a+'   '+b)
  
        
import math
i=int(input('请输入一个数'))
if i>=0:
    i=math.sqrt(i)
    print(i)
else:
    print('负数不能开平方')
print('程序结束')

s='王凯旋是天才'
s='王凯旋真的是天才'
print(s)

io=('jiyua职业技术学院')
print(io.title())
print(('zhongguo').title())
print(('zhongguo').upper())  # .upper()全部大写
print(('wangkaixuan').lower())# .lower()全部小写
print('\t王凯旋是天才啊')#制表符 
print('\tjfaojfj')#制表符
print('王凯旋是天才\n\t啊啊啊啊')#制表符和换行符

#.strip() lstrip() rstrip()
w=' ophihih '#有空白的时候不能直接用 stripa()lstrip()rstrip()去除参数字符
            #要先去除空白再去除参数字符
w=(w.lstrip())# .lstrip()去除左边空白)
print(w.lstrip('o'))

w=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
xiao='abcdefghijlmnopqrstuvwxyz'
for i in range(len(w)):
    print(w[i],ord(w[i]))

w=' jiyuang'
w=(w.lstrip( ))
print(w.lstrip('j'))





wer=('王凯旋是天才')
print(wer.split('是')) 


ui=[5,8,89,1,24,2,96,897,45]
ui.sort()
print(ui)

class Person():
    name='wangkaixuan'
    age=45

    def show(self):
        print(self.name,self.age)
ui=Person()        
print(Person.name,Person.age)
print(ui.name,ui.age)

#创建汽车类

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_read=0

    def get_descriptive_name(self):
        longname=self.make+self.model+str(self.year)
        return longname.title()

    def read_odometer(self):
        """打印区汽车的里程信息"""
        print('这辆车有'+str(self.odometer_read)+'里程行驶距离')

    def update_odometer(self,mileage):
        if mileage>=self.odometer_read:
            self.odometer_read=mileage#方法修改属性的值
            self.odometer_read+=mileage#通过方法进行递增
        else:
            print('增加的值不能低于初始值')

ui=Car('红旗汽车厂','越野车','89')
print(ui.get_descriptive_name())
ui.read_odometer()
ui.update_odometer(90)
ui.read_odometer()

    
#类属性的建立与访问
class Person():
    name='王凯旋'
    age=12

    def show(self):
        return (self.name,self.age)

p=Person()
q=Person()
print(Person.name,Person.age)#用类名称访问类属性
print(p.name,p.age)#用实例对象访问类属性
print(q.name,q.age)#用实例对象访问类属性
Person.name='robert'
p.age=15
print(Person.name,Person.age)
print(p.name,p.age)
print(q.name,q.age)
print (q.show())

class Personn():
    __name='王凯旋'
    __age=90

    def show(self):
        return (self.__name)

    def show2(self):
       long_name=(self.__name,self.__age)
       return long_name
ui=Personn()
print(ui.show2())

class Person():
    name='王凯旋'
    gerder='男'
    age=89

p=Person()
print(p.name,p.gerder,p.age)
print(Person.name,Person.gerder,Person.age)
p.name='A'
p.gerder='Male'
p.age=20
Person.name='B'
Person.gerder='Female'
Person.age=21
print(p.name,p.gerder,p.age)
print(Person.name,Person.gerder,Person.age)

class Person():
    __name='王凯旋'
    __age=78

    def showname(self):
        return self.__name

    def showage(self):
        return self.__age
    
p=Person()
print(p.showname(),p.showage())

class Person1():
    __name='王凯旋'
    __age=89

    def shili(self):#实例方法
        print(self.__name,self.__age)

    
    @classmethod#类方法
    def show(cls):
        print(cls.__name,10,cls.__age)
        #print(cls.__name,"\nstr(cls.__age)")

    @staticmethod#静态方法
    def show1():
        print(Person1.__name,Person1.__age)

ui=Person1()
ui.show()#实例对象调用类方法
Person1.show()#类对象调用类方法
ui.shili()#实例对象调用实例方法
Person1.shili(ui)#类对象调用实例方法


Person1.show1()#类对象调用静态方法
ui.show1()#实例对象调用静态方法
7

#实例对象的初始化
class Person():
    def __init__(self,n,g,a):
        self.name=n
        self.gerder=g
        self.age=a

    def show(self):
        print(self.name,self.gerder,self.age)
p=Person('james','male',21)
p.show()

#在__init__中设置默认参数
class Person():
    def __init__(self,n='',g='male',a=0):
        self.name=n
        self.gerder=g
        self.age=a

    def show(self):
        print(self.name,self.gerder,self.age)
a=Person('james')
b=Person('james','female')
c=Person('james','male',20)
a.show()
b.show()
c.show()

#类的派生与继承
class Person():
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def sho(self,):
        print(self.name,self.gender,self.age,end='')

    def display(self):
        print(self.name,self.gender,self.age)


class Student(Person):
    def __init__(self,name,gender,age,major,dept):
        Person .__init__(self,name,gender,age)
        self.major=major
        self.dept=dept

    def show(self):
        Person.sho(self)
        print(self.major,self.dept)

a=Student('王凯旋','男',20,'计算机应用技术','信息工程系')
a.show()
a.sho()
a.display()

try:
    f=open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','rt',encoding='UTF-8')
    f=f.read()
    print(f)
except:
    print('文件打开异常')

f=f.read()#读取文件保存到变量里
f.close()关闭文件
f.write('王凯旋是天才')读写文件不需要保存到变量里
#读取模式
rt只读
wt只写会清空源文件
at续写源文件

f=open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','rt',encoding='UTF-8')
绝对路径 加文件名 读写模式 编码格式打开文件保存到变量f里面去


try:
    f=open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','wt',encoding='UTF-8')
    f.write('你好天上人间\nihoama\n我还好\nn')
    f.write('nihoama\n')
    f.write('我还好\n')
    f.close()
except:
    print('文件打开失败')


f=open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','rt',encoding='UTF-8')
c=f.read(5)
print(c)
f.close()

f=('C:\\Users\86666\Desktop\自己编写的Python程序\93.txt')
with open(f,'rt',encoding='UTF-8') as ui:
    ui=ui.readlines()
    print(type(ui))
io=''
for i in ui:
    io+=i.rstrip()
print(io)
print(len(io))


with open('C:\\Users\86666\Desktop\自己编写的Python程序\91.txt','rt',encoding='UTF-8') as ui:
    ui=ui.read()
    for i in ui:
        print(i.strip(),end='')#关闭换行，去掉空格，横行显示

def writefile():
    ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','wt+')
    print(ui.tell())
    ui.write('123')
    print(ui.tell())
    ui.seek(2,0)
    print(ui.tell())
    ui.write('abc')
    print(ui.tell())
    ui.close()

def readfile():
    ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','rt+')
    ui.write('我们')
    ui.seek(0,0)#从零开始移动零个位置
    u=ui.read()
    print(u)
    ui.close()

try:
    writefile()
    readfile()
except Exception as err:
    print(err)


def writefile():
    ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','wb')
    ui.write('abc我们'.encod=('gbk'))
    ui.close()

def readfile():
    ui=open('C:\\Users\86666\Desktop\自己编写的Python程序\94文件指针.txt','rb')
    u=ui.read()
    for i in u:
        print(i,end='')
    ui.close()

try:
    writefile()
    readfile()
except Exception as err:
    print(err)

，import math
s=int(input("请输入一个你想输入的数字"))
if s>=0:
    print(math.sqrt(s))
else:
    print('负数不能开平方')
'''
import math
s=int(input('请输入你想输入的数字'))
if s>=0:
    print('开平方后的结果是',math.sqrt(s))
else:
    print('负数不能开平方')

print('程序运行结束')












