'''
#列表类型
#列表的数据项不需要有相同的类型 每个元素分配一个索引（下标）
#序列都可以进行的操作：索引，切片，加，乘，检查成员

my_list=['wangkaixuan','iop','是天才啊',45,5,6]
my_list2=[2,45,34,89]
ui=my_list+my_list2
print(my_list+my_list2)\
print(ui)
for i in ui:
    print(i)
ui[0]=89090
print(ui)

#删除列表 del 语句
del ui[0:3] #通过列表的截取来删除元素
print(ui)
del ui[1]  #删除后列表的结果会自动保存在原有列表里
print(ui)
wang='12335899666'
print(wang[2:])
yu=['iop',89545,5,4,3]

if 'iop' in yu:
    print('王凯旋是天才')
print(5 not in yu) #in 和 not in返回的是True 或False的逻辑值

# 列表的常用操作函数
# 1 list.append()在末尾添加新的对象
my_list4=['wangkaixuan',3,2,5,78,90,'iop',3,3,2,2,'iop']
my_list4.append('啥时候开学啊')
print(my_list4)

# 2 list.count()统计元素出现的次数
print(my_list4.count(3))

# 3 list.extend()在末尾增加啊另一个序列的多个值
a=[8,78,56,34,'op']
b=[890,67,23]
a.extend(b)
print(a)
# 4 list.index()在列表找出一个元素第一次出现位置的下标
print(a.index(78))

# 5 list.insert(index,obj)将元素按照索引的方式插入列表
a.insert(0,89)
print(a)

# 6 list.remove(obj)移除某一个元素在列表中的第一个匹配项
a.remove(56)
print(a)

# 7 list.reverse()将列表中的元素反向，反向后顺序也更改了
we9=[1,23,13,4,0.5,6,17,8,29,10]
we9.reverse()#被更改没有返回值
print(we9)

# 8 list.sort()将列表内的元素进行排序
y=sorted(we9)
print(y)
print(we9)

# 9 list (列表与函数)
def fun():
    list=[]
    for i in range(10):
        list.append(i)
    return list
    
list=fun()
print(list)

#10 列表的应用
#输入省份查找城市
s=['广东','四川','贵州']
c=[['广州','深圳','惠州','珠海'],['成都','内江','乐山'],['贵阳','六盘水','遵义']]
n=input('请输入你的省份：')
found=False
for i in range(len(s)):
    if s[i]==n:
        print(s[i])
        for j in range(len(c[i])):
            print(c[i][j],end='')
            found=True
            break
if not found:
    print('没有这个省份')

#输入城市查找省份
s=['广东','四川','贵州']
c=[['广州','深圳','惠州','珠海'],['成都','内江','乐山'],['贵阳','六盘水','遵义']]
d=input('请输入你的城市')
def search(d):
    for i in range(len(c)):
        for x in c[i]:
            if x==d:
                print(d+'在'+s[i]+'省')
                return
    print('没有这个省')
search(d)

'''
io=(9,4,7,'reuir',(5,56,23,0))#嵌套元组的访问
print(io[4][1])

ui=[90,54,'王凯旋','ji',(90,78,45,90,)]#嵌套列表的访问
print(ui[4][3])


    


    

            
        




