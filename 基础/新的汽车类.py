class Car():
    def __init__(self,make,model,year):
        '''初始化实例属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_xiangxi(self):
        '''返回汽车的详细信息1'''
        print('汽车制造商是'+self.make+'汽车型号是'+self.model+'汽车制造年份是'+str(self.year)+' 年')

    def read_odometer(self):
        '''打印一条汽车行驶里程的信息'''
        print('这辆车目前行驶了'+str(self.odometer_reading)+'公里')

    def update(self):
        while True:
            zengzhi=int(input('请输入增值'))
            if zengzhi>self.odometer_reading:
                self.odometer_reading=zengzhi
                break
            else:
                print('输入的值不正确，请您重新输入')

class Elecar(Car):
    def __init__(self,make,model,year,dianchi):
        Car.__init__(self,make,model,year)
        self.dianchi=dianchi


    def show(self):
        '''打印电动车电池的详细信息'''
        print(self.dianchi,'毫安')

my_dian=Elecar('美国制造','奔驰',1997,52)

print('电动车汽车制造商'+my_dian.make)
my_dian.get_xiangxi()









