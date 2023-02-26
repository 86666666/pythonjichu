'''
class Dog():
    '''一次模拟小狗的简单尝试'''
    def __init__(self,name,age):  #方法__init__设置属性
        '''初始化属性name和age'''
        self.name=name  #创建属性的句点表示法
        self.age=age    #创建属性的句点表示法
        self.gg=78*89 
    def sit(self):
        '''模拟小狗被命令蹲下来'''
        print(self.name.title()+'is now sitting')

    def roll_over(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title()+'蹲下了')
        
        
my_dog=Dog("wang",8)  #
print(my_dog.age) #访问属性用句点表示法
k=my_dog.sit()
print(k)
'''
