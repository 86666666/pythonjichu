class Dog():
    def __init__(self,name,age=90):
        self.name=name
        self.age=age
        self.gj='中国'

    def sit(self):
        print('小狗蹲下')

    def up(self):
        print('小狗站起来')

a=Dog('luc')
print(a.age,a.gj)
print(f'狗的年龄是{a.age}岁,国籍是{a.gj}')
a.sit()
a.up()
print()

dog1=Dog('美国',90)
dog2=Dog('日本',7999)
print(dog1.age,dog1.gj)
print(dog2.age,dog2.gj)
print('-----------下面是汽车类-------------')

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.xj='地球'
        self.odometer_reading=0

    def get_descriptive_name(self):
        longname=f"{self.year} {self.make} {self.model}"
        return longname.title()

    #通过方法来修改属性的值 设置为全新的值
    def update_odometer(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('你不能将里程表往回调')

    #通过方法来修改属性的值 设置为递增的值
    def increment_odometer(self,miles):
        self.odometer_reading +=miles


    def read_odoscriptive_name(self):
        '''打印一条指出汽车里程的消息'''
        print(f"这辆车行驶了{self.odometer_reading}公里")


my_new_car=Car('jf','x5',2022)
my_new_car2=Car('hu','x7',2030)

print(my_new_car.get_descriptive_name())
#修改属性的值
my_new_car.read_odoscriptive_name()
my_new_car.odometer_reading=70  #通过实例直接修改
my_new_car.read_odoscriptive_name()
my_new_car2.read_odoscriptive_name()
my_new_car2.update_odometer(200) #通过方法来修改属性的值
my_new_car2.update_odometer(100)
my_new_car2.read_odoscriptive_name()
my_new_car2.increment_odometer(900)
my_new_car2.read_odoscriptive_name()

print('类的继承')
#类的继承

class ElectricCar(Car):
    '''电动汽车的独到之处'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print(f'这辆车的电量为{self.battery_size}w')


my_tesla=ElectricCar('ty','x90',2040)

print(my_tesla.model)

my_tesla.update_odometer(9000)
my_tesla.read_odoscriptive_name()
my_tesla.increment_odometer(800)
my_tesla.read_odoscriptive_name()
my_tesla.describe_battery()   #使用子类自己的方法





