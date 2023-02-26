class Car():
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0 #添加一个属性用于读取汽车的里程表

    def get_desc_name(self):
        '''返回整洁的描述信息'''
        long_name=(str(self.year)+' '+self.make+' '+self.model)
        return long_name

    def read_odometer(self):
        '''添加一个方法打印汽车里程'''
        print('这辆车行驶里程'+str(self.odometer_reading)+'公里')


    def update_odometer(self,mileage):
        '''创建一个方法来修改属性的值'''
        if mileage > self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('你不能回调里程表')

    def increment_odometer(self,miles):
        '''通过方法对属性的值进行递增'''
        self.odometer_reading+=miles

    def fill_gas_tank(self):
        print('这辆车没有邮箱')

# my_car=Car('宝马','宝马x6',2021)
# print('我的汽车是'+my_car.get_desc_name(),my_car.age)
# my_car2=Car('奔驰','奔驰x',89)
# my_car2.read_odometer()
# my_car2.odometer_reading=23  #句点表示法实例直接访问并设置属性的值 修改的值只对该实例有效，不影响类中属性的值
# my_car2.read_odometer()
# my_car2.update_odometer(30) #用方法修改属性的值
# my_car2.read_odometer()
# my_car2.update_odometer(10)
# my_car2.read_odometer()
#
# my_car3=Car('红旗','红旗x',2008)
# my_car3.read_odometer()
# my_car3.increment_odometer(900)
# my_car3.read_odometer()
# my_car3.increment_odometer(300)
# my_car3.read_odometer()


#将一个类的实例用作另一个类的属性
class Battery():
    '''创建一个电瓶类'''
    def __init__(self,battery_size=71):
        '''初始化属性'''
        self.battery_size=battery_size

    def describe_battery(self):
        '''打印一条描述电瓶容量的消息'''
        print('这辆电动车的电池容量是'+str(self.battery_size)+'千瓦时')








            #类的继承---创建一个子类
class Electricar(Car):
    def __init__(self,make,model,year):
        '''初始化父类的属性'''
        super().__init__(make,model,year)
        self.battery_size=70 #为子类添加电瓶容量这个型属性
        self.battery=Battery() #将Battery类的实例当做Electricar类的属性
      #新方法
    def describe_battery(self):
        '''打印一条描述电瓶容量的方法'''
        print('这辆车的电瓶容量'+str(self.battery_size)+'千瓦时')

    #重写父类的方法
    def fill_gas_tank(self):
        print('这是一个电动车所以没有电瓶')

my_car4=Electricar('特斯拉','modelx',2021)
# print(my_car4.get_desc_name())
# print(my_car4.battery_size)
# my_car4.describe_battery()
#my_car4.fill_gas_tank()
my_car4.battery.describe_battery()