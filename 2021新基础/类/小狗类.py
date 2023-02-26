class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name=name
        self.age=age
        self.log=7889

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print('小狗'+self.name.title()+'正在下蹲')

    def roll_voer(self):
        print('小狗'+self.name.title() +'正在打滚')

my_dog=Dog('666',6)
# print('我的小狗的名字是'+my_dog.name.title())
# print('我的小狗的年龄是'+str(my_dog.age))
# print(my_dog.log)
# my_dog.sit()
print(my_dog.sit())
# my_dog.roll_voer()
# you_dog=Dog('傻逼',90)
# print('你的小狗的名字叫'+you_dog.name)
# print('你的小狗的年龄是'+str(you_dog.age))

