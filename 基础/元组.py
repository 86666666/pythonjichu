'''
# for 循环计算任意个数的最大值
def max(*args):
    print(args)
    m=args[0]
    for i in range(len(args)):
        if m<args[i]:
            m=args[i]
    return m
print(max(4,5,8,87,324,53,6,5,45,67))
'''
# 元组和列表的转化
lis=['王','凯','旋',90,89,78,545,]
t=(3,45,35,5)
lis=tuple(lis)#列表转化为元祖
print(lis)
w=list(t) #将元祖转化为列表
print(w)

#字符串转化为列表或元组
ui9=('wangkaixuan')#将字符串转化为列表
ui9=list(ui9)
print(ui9)

ui8=('王凯旋')
ui8=tuple(ui8)#将字符串转化为元祖
print(ui8)

ui3=(2,5,55,89,'wang','王')
ui3=ui3[:2]+('wangkaixuan',)+ui3[2:]#元组的拼接要加括号和逗号
print(ui3)

ui4=('wagn',)#元祖中只有一个元素要添加逗号
print(type(ui4))
ui1=(4,5,8,87,324,53,6,5,45,67)
print(max(ui1))#最大值
print(min(ui1))#最小值



