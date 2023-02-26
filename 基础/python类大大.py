
class Dog():
    '''模拟小狗的类'''
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        '''模拟小狗下蹲的方法'''
        return(self.name.title()+'正在下蹲')

    def roll_over(self):
        '''模拟小狗打滚的方法'''
        print(self.name.title()+'正在打滚')

my_dog=Dog('while',12)
print('我的小狗的名字是'+my_dog.name)
print('我的小狗的年龄是'+str(my_dog.age))
ui=my_dog.sit()
print(ui)
#创建多个Dog类实例
my_dog2=Dog('姚明',42)
your_dog=Dog('李白',89)
print()


