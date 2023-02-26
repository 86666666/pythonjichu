 import os
# import sys
# print(sys.path)
# print(os.name)
# print(type(os.getcwd()))
# a=os.listdir(r'E:\\pycharm工程目录')#返回指定的目录下的文件和目录
# print(os.listdir())#返回当前文件所在的目录
# print(a)
# if os.path.isdir('Python网络编程'):#检验给出的路径名是不是目录
#     print('是目录')
# else:
#     print('这不是目录')
#
# print(os.path.isfile('a2mod.py'))#检验给出的路径名是不是文件
q=os.listdir()
print(q)
list1=[]
for i in q:
    os.path.isfile(i)#判断是不是文件，
    list1.append(i)#如果是文件就添加到列表里
list2=[]
for i in list1:
    a1=os.path.abspath(i)#通过文件名字获取文件的绝对路径
    list2.append(a1)

for i in list2:
    print(i)

# os.remove('2021年3月28日.py')
# print('删除成功')

#给文件进行重命名
#os.rename('xin.py','xin2.py')#对文件进行重命名

os.makedirs(r'c\c1\c2')#创建多级目录