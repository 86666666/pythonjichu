'''
在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从Python解释器
退出再进入，那么你定义的所有的方法和变量就都消失了。为此 Python 提供了一个办法，
把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块.
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，
以使用该模块中的函数等功能。这也是使用 python 标准库的方法。

'''
# 判断两个数谁大
'''
def max(a,b):
    c=a
    if a<b:
        c=b
    return(c)


def min(a,b):
    c=a
    if a>b:
        c=b
    return(c)


import sys
y=sys.path
for i in y:   # python的for循环可以遍历任何序列的项目
   print(i)


for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print('当前字母 :', letter)
'''
i=26
c=34
f=34
print(str(i)+':'+str(c)+':'+str(f))
