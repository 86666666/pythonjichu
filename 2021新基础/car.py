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
