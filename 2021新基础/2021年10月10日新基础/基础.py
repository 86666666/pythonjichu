# m=12  #输出一个整数
# print('|%4d|' % m,len('|%4d|' % m))
# print('|%-04d|' % m)
# year,month,day,hour,minute,second=201.5,2,1,8,12,0
# print(year,month,day,hour,minute,second)
# print("现在是北京时间：%04d-%02d-%02d %02d:-%02d:%02d" % (year,month,day,hour,minute,second))
# m=12.57432
# print('|%f|' % m)
# print("|%8.1f|" % m)
# print('|%8.2f|' % m)
# print('|%-8.1f|' % m)
# print('|%-8.0f|' % m)
#
# m='ab'
# print('|%s|' % m)
# print('|%8s|' % m)
# print('|%-8s|' % m)
# if 2==3:
#     print('这是对的')
# else:
#     print('这是错的')
#
# str='123456789'
#
# print(str)
# print(str[0:1])
# print(str[0:2])
# print(str[1:2])
# print(str[-1])
#
# #python中的6个数据类型
#
# #number 数字 string 字符串  list 列表 tuple 元组 dir 字典  set 集合
#
# a,b,c,d=20,5.5,True,4+4
# print(a,b,c,d)
# print(type(a),type(b),type(c),type(d))
# if type(a)==int:
#     print('变量a是整数类型的数据')

# var1=1
# var2=10
# print(var1,var2)
# del var1,var2
# print(var1,var2)

# we='abd'
# print(2*we) #字符串的复制
#
# str='Runoob'
# print(str)
# print(str[0:-1])  #不能切片到最后一位
# print(str[0])
# print(str+'王凯旋是天才')
# print(r'ru\noob')
# print('ru\noob')

# t=['a','b','c','d','e']
# print(t[1:3])
# print(t[:4]) #相当于t[0:4]
# print(t[3:])
# t1=t[:] #全复制
# print(t1)

# list=['abcd',786,2.23,'runoob',70.2]
# tinylist=[123,'runoob']
# print(list[0])
# print(list[1:3])
# print(list[2:])
# print(2*tinylist)
# print(list+tinylist)


# #与字符串不一样的是，列表中的元素是可以改变的
# a=[1,2,3,4,5,6]
# print(a[0])
# print(a)
# a[0]=30
# print(a)
# d=a[2:5]
# print(d)
# for i in d:
#     print(i)
# b=[2,3,'王凯旋',56,8+9,[1,2,3]]
# print(b)
# print(b[5][0])
# b[1:3]=['北京','天津']
# print(b)


#列表和字符串等其他序列一样可以被索引和切片
# 傻逼=['r','u','n','o','o','b']
# print(傻逼)
# print(傻逼[0:-1:2])

#tuple 元组与列表类似，不同之处在于元组的元素不能修改，
# 元组写在小括号（）里面，元素之间用都逗号隔开，元组中的元素类型也可以不相同
tuple=('abcd',786,2.23,'runoob',70.2)
tinytuple=(123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
a=2*tuple
print(a)









