
'''
try:
    import math
    i=float(input('请输入一个要开平方的数字'))
    if i<0:
        print('负数不能开平方')
    else:
        print(math.sqrt(i))
except Exception as err:
    print(err)

while True:
    try:
        import math
        m=float(input('请输入一个数'))
        if m<0:
            raise Exception('您输入的数为负数')
        break
    except Exception as err:
        print('输入错误：',err,'请重新输入')
print(math.sqrt(m))

print('程序结束')
while True:
    try:
        import math
        m=float(input('请输入一个数字以便用来开平方'))
        m=math.sqrt(m)
        print(m)
        break
    except:
        print('你出错了，要重新输入')
print('程序结束')

def a(a,b,c):
    print(a,b,c)
a(4,5,7)
def ui(i):
    if i<0:
        return ('王凯旋是天才')


ui(-9)

def u():
    print('王凯旋是天才')
    return('王凯旋是天才')
1
ui=u()
print(ui)
def sum():
    global pr
    global ci
    pr=input('请输入你的省份')
    ci=input('请输入你的城市')
sum()
print(pr,ci)

def show():
    print('你在'+pr+ci+'境内')
show()

def max(a,b=1,c=2):
    print(a,b,c)

max(1)
max(1,2)
max(1,2,3)

print('王凯旋是天才','不知道',sep='6666')


import sys
print(sys.path[0])


def time():
    shi=int(input('请输入当前时间'))
    feng=int(input('请输入当前分钟'))
    miao=int(input('请输入当前是多少秒'))
    if shi<0 or shi>24:
        raise Exception('输入的时间不正确')
    if feng<0 or feng>59:
        raise Exception('输入的分钟不正确')
    if miao<0 or miao>59:
        raise Exception('输入的秒数不正确')
    print('%02d:%02d:%02d'%(shi,feng,miao))

time()

import bijiao
print(bijiao.max1(3,5))

ui='wangkaixuan'
print(len(ui))
for i in ui:
    print(i)

ui=('wangkaixuan')

for i in range(len(ui)):
    print(ui[i])

name=('wangkaixuan')
print(name.title())
print(name)
print(name.upper())
print(name.lower())

name2=(' wangkaixuan')
print(name2.strip())
print(name2)
o4=('ijifjajffkfajfffjakfi')
print(o4.strip('i'))#在首尾移出'i'

s='wangkaixuan'
print(s.find('n'))#返回子串的第一次出现的位置的下标，没有就返回负一
print(s.find('nk'))
print(s.rfind('uaa'))
if s.startswith('w'):
    print('王凯旋是天才')

wang=('i am learning python')
p=wang.split(' ')
print(type(p),p)
print(s.split('gk'))

ui=[2,3,5,'北京市','天津市',90]

ui[2]=(4+9)
print(ui)
ui[1:4]=(85,45,67)#通过切片来更改列表的值
print(ui)
del ui[0]
print(ui)
for i in range(10):#通过append在列表的末尾添加值
    ui.append(i)

print(ui)

jiyuan=[2019,10,10,2,4,5,5,5,2]
print(jiyuan.count(10))#通过list.count()方法来统计列表中的某一个元素出现的次数
#list.extend()#在末尾一次增加另一个序列的值
qi=(3,5,6)
jiyuan.extend(qi)
print(jiyuan)
#list从列表中找出某一个值得第一次出现的索引
print(jiyuan.index(10))

#list .insert(索引,值)将元素按照索引的方式插入列表
list1=[2,5,6,2]
list1.insert(2,'wangkaixuan')
print(liyu

wang='5254525452452633524'
q=wang.count('5')
print(q)

print(ui)
print(ui.count('机'))

tuple1=(23,45,'王凯旋','faf','qw')
str1=('abc王凯旋123')
list1=[2,4,'list','52','王凯旋']
print(type(tuple1),type(str1),type(list1))
print(list(str1),'/n',list(tuple1))
def max1(*args):
    e=args[0]
    for i in range(len(args)):
        if e<args[i]:
            e=args[i]
    print(e)

max1(8,3,5,2,62,25,)

tuple12=(3,4,5,2)
uiii=tuple12[0:2]+('王凯旋',)+tuple12[2:]
print(uiii)

zidian={2:45,'北京':'顺义','河南':'信阳',34:'上海'}
print(len(zidian))


print(zidian[2])
zidian['tianjing']=989

iui=zidian.keys()
print(type(iui))
print(zidian.get('中国','对不起没有保存'))

st=[]
def chazhao():
    global st
    st.append({'name':'张三','性别':'男','年龄':'20'})
    st.append({'name':'李四','性别':'男','年龄':'21'})
    st.append({'name':'王五','性别':'女','年龄':'56'})

def cha(na):
    for i in st:
        if i['name']==na:
            print(na+'的性别是'+i['性别']+'年龄是'+i['年龄'])
            return
    print('没有找到')


chazhao()
cha('王五')

print(abs(-89))
a=int(input('输入一个数'))
b=int(input('输入一个数来判断它的值是否正确'))
if all((a+b==78,89)):
    print('输入的值正确')
print(round(70.896,2))

ji=[3,4,6]
jii=[4,5,24,3]
for i in ji:
    if i in jii:
        print('添加'+str(i))
    else:
        print('没有'+str(i))




alien={'速度':0,'距离':25,'状态':'慢'}
if alien['状态']=='慢':
    x=3
elif alien['状态']=='快':
    x=2
else:
    x=1
alien['速度']=alien['速度']+x
print(alien['速度'])
q=alien.items()
q=list(q)
print(q)
print(q[0])
for j,i in alien.items():
    print(j,i)
'''
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
friends=['jen','phil']
'''
for name,language in favorite_languages.items():
    print(name.title()+'最喜欢的计算机语言是'+language.title())
'''
for name in favorite_languages.keys():
    print(name)
    if name in friends:
        print('你好'+name.title()+'我知道你最喜欢的计算机语言是'+favorite_languages[name])














