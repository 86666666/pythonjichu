'''
class Person():
    name='james'
    age=12
    #实例方法
    def lishow(self):
        print(self.name,self.age)

    #类方法
    @classmethod
    def leishow(cls):
        print(cls.name)

    #定义静态方法
    @staticmethod
    def show():
        print('类属性的名称是',Person.name)

p=Person()
#静态方法的调用
p.show()
Person.show()
#实例方法的调用
p.lishow()
Person.lishow(p)
#类方法的调用
p.leishow()
Person.leishow()
'''
class Person():
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def show(self):
        print(self.name,self.gender,self.age,end=' ')

    def display(self):
        print(self.name,self.gender,self.age)

class Student(Person):
    def __init__(self,name,gender,age,major,dept):
        Person.__init__(self,name,gender,age)
        self.major=major
        self.dept=dept


    def show(self):
        Person.show(self)
        print(self.major)

    def setname(self,name):
        '''修改name的属性'''
        self.name=name

s=Student('james','male','20','software','computer')
s.show()

