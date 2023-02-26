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
list1=[]
for i in q:
    os.path.isfile(i)
    list1.append(i)
print(list1)

# os.remove('2021年3月28日.py')
# print('删除成功')
