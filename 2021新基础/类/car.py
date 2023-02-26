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