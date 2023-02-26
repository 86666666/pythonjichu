#类的方法
class Person():
    __name='wangkaixuan'
    __age=67
    def getname(self):
        return(selfl.__name)
    
    def getage(self):
        return(self.__age)

wh=Person()
print(wh.getage)
    
