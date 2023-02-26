# list1=[1,23,46,12,4,5,2]
# list2=['xyz','北京市','天津市']
# list2[2]='潢川县'
# print(list2)
# list2[2:]=['广州市','东北']
# print(list2)
# del list2[-1]
# print(list2)
# list3=list1+list2
# print(list3)
# list4=[4,5]
# for i in list4:
#     list3.insert(0,i)
#
# print(list3)
# print(list3.count(4))
#

import os
#print(os.getcwd())
i1=os.listdir(r'E:\pycharm工程目录\Python网络编程')
for i in i1:
    i=os.path.abspath(i)
    if os.path.isfile(i):
        print(i,'是文件')
def li(mylist1,m,s):
    mylist1.append(1)
    m=2+m
    s='wang'
    s=s+''
#输入省份查找城市

sf=['广东','四川','贵州']
ct=[['广州','深圳','惠州','珠海'],['成都','内江','乐山'],['贵阳','六盘水','遵义']]
p=input('请输入你的省份')
a=False
for i in range(len(sf)):
    if sf[i]==p:
        print(sf[i],':')
        for j in range(len(ct[i])):
            print(ct[i][j],end='')
    else:
        print(p,'不存在')
        break

