


'''
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




class Person:
    name='james'
    age=12

p=Person()
q=Person()
print(p.name,p.age) #使用实例对象和（句点表示法）来访问类属性
print(Person.name,Person.age) #使用类名称和（句点表示法）来访问类属性

#私有属性的访问权限
class Person():
    name='xxx'
    age=2         #没有用双下划线开头的是公有属性
    gender='女'
    __name='wangkaixuan'
    __age=4       #用双下划线开头的是私有属性
    __denger='男'



#类的实例方法
class Person():
    __name='wangkaixuan'  #定义私有属性
    __age=67
    def getname(self):   # 定义方法（实例方法）
        return(self.__name)
    
    def getage(self):
        return(self.__age)
wh=Person()
print(wh.getage(),wh.getname())  #方法是函数调用的时候要带上括号
'''
#类的类方法（属于类的方法,不是实例方法）用 @classmethod来修饰
class Person():
    __name = 'wangkaixuan'  #定义私有属性
    __age = 34

    @classmethod   #定义类的方法（不同于实例对象的方法）
    def show(cls):
        print(cls.__name,cls.__age)
        #print(cls.__name.cls.__age)报错是因为pirnt中的逗号用成了点号

Person.show()
'''
#为这个对象实例赋值，那么如果这个对象有这个属性，这个属性的值就会被改变，
#如果没有这个属性就会自动为该对象实例创建一个这样的属性

# 类方法
class Wang():
    name='wangkaixuan'
    age=45
    @classmethod #类属性 
    def show(self):        #一次用一个函数打印两个属性会带括号
        a=self.name+' '+str(self.age)#return(self.name,self.age)打印出来的结果带括号
        return a

ui=Wang()
print(ui.show())
   
print(Wang.show())


# 静态方法
class Person():
    __name='iames' #创建私有属性
    __age=12

    def wang(self):  # 实例方法 可以用类对象名称或者类名称传递实例对象给函数self
        print(self.__name,self.__age)

    @staticmethod  # 静态方法  类名称和实例对象名称调用
    def display():
        print(Person.__name,Person.__age)
    @classmethod  # 类方法实例对象和类名称调用
    def show(cls):
        print(cls.__name,cls.__age)

    
ui=Person
Person.display()
Person.show()
Person.wang(ui)#实例方法用类名称调用需要给函数传递实例对象给self参数

# 对象初始化（面向对象）构造方法__init__(self) 析构方法__del__(self)
class Person():
    def __init__(self,n):  #构造函数
        print('__init__',self,n,end='')
        self.name=n
        
    def __del__(self):  #析构函数
        print('__del__',self)
        
        
    def show(self):
        print(self.name)
p=Person('wangkaixuan')
p.show()
print (id(p)
print('\n\twangkaixuan')  # python换行符与制表符

#对象初始化 构造函数__init__初始化实例的属性
# 构造函数__init__时间里对象的时候自动调用的函数

class Person():
    def __init__(self,n='',g='male',a=0):
        self.name=n   #创建实例对象自己的属性
        self.gerder=g   #三句话创造的是实例属性而不是类属性
        self.age=a

    def show(self):
        print(self.name,self.gerder,self.age)

a=Person('james')
b=Person('james','female')
c=Person('james','male',20)
a.show()
b.show()
c.show()

#类的继承（派生与继承）
#面向对象一个很大的特点是类可以被扩展和继承

class Person(): #基类
    def __init__(self,name,gerder,age):#构造函数 初始化实例对象的属性
        self.name=name
        self.gerder=gerder
        self.age=age

    def show(self):#关闭换行也可以用def show(self,end='\n')
        print(self.name,self.gerder,self.age,end=' ')#关闭自动换行并增加空白键隔
                                                    #也可以增加数据例如字符串
                                                    
class Student(Person):  #派生类（继承类）
    def __init__(self,name,gerder,age,major,dept):
        Person.__init__(self,name,gerder,age)#继承调用并显示基类的构造函数
        self.major=major  #初始化新增加的继承类属性
        self.dept=dept

    def show(self):
        Person.show(self)
        print(self.major,self.dept)

    def setname(self,name):
        self.name= name
        
s=Student('wagnkaixuan','男',78,'计算机','信息工程系',)
s.show()
s.setname('jiyaunhsi')
s.show()
'''

























