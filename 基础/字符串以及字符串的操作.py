
#字符串  ''引号或者""引号括起来的是字符串
print('falfkalfj,"52855"+89')
print('256944966')

#字符串的拼接用+号
a=('85555')
b=('555')
print(a+b)

op=8989
print('王凯旋是世界上少数几个天才了'+str(op)+'!!!!!!!')

a=('5656')
b=('jfajagjoijwangkaixuan')
print(a+'   '+b)

#python可以随时可以修改变量的值，而pyhton始终将记住变量的最新值

s='王凯旋是天才'
s='王凯旋真的是天才'
print(s)

#方法是pyhton可对数据进行的操作 方法就是函数要带括号（）
#字符串的首字母大写   变量.title()  字符串.title()

print(('fjkajf jgs').title())#字符串的首字母大写 用.title()

name=("wang kai xuan")
print(name.title())#字符串的首字母大写

print(('wang yun hui').upper()) #字符串全部大写 用upper

print(('WANG KAI XUAN').lower())#字符串全部小写 用lower

name_1=('wang kai xuan')
name_2=('WANG KAI XUAN')
print(name_1.upper())#upper用于全部大写
print(name_2.lower())#lower用于全部小写
io=('jiyua职业技术学院')
print(io.title())
print(('zhongguo').title())  #首字母大写
print(('zhongguo').upper())  # .upper()全部大写
print(('wangkaixuan').lower())# .lower()全部小写


#制表符\t 和 换行符\n
print('\twang \n\tkai \nxuan')
io=('jiyua职业技术学院')
print(io.title())
print(('zhongguo').title()) #首字母大写
print(('zhongguo').upper())  # .upper()全部大写
print(('wangkaixuan').lower())# .lower()全部小写
print('\t王凯旋是天才啊')#制表符 
print('\tjfaojfj')#制表符
print('王凯旋是天才\n\t啊啊啊啊')#制表符和换行符



#制表符的写法是\t，作用是对齐表格的各列。
print("学号\t姓名\t语文\t数学\t英语")
print("2017001\t曹操\t99\t88\t0")
print("2017002\t周瑜\t92\t45\t93")
print("2017008\t黄盖\t77\t82\t100")

#strip 脱光扒光剥除  剥除函数
#.lstrip 去除左边空白
#.rstrip 去除右边空白
#.strip 去除左右空白
w=' ophihih '#有空白的时候不能直接用 stripa()lstrip()rstrip()去除参数字符
            #要先去除空白再去除参数字符
w=(w.lstrip())# .lstrip()去除左边空白)
print(w.lstrip('o'))

ui=('gjajf')
print(ui.lstrip('g'))
print(ui.strip('g'))
o=('   jifjajffk\nfaj\n\tfffj\nakf')
print(o.strip('i'))
o4=('ijifjajffkfajfffjakfi')
print(o4.strip('i'))#在首尾移出'i'
#import this#python之禅


#字符串是程序中最常见的一种数据类型，在内存中用Unicode编码储存，
#在磁盘中用GBK或者UTF-8d等别的编码形式

#1 获取字符串的长度函数   len函数         len(字符串或者变量名)
print(len('王凯旋是天才'))
s=('王凯旋是天才')
print(len(s))

#2 读取字符串的字符用  变量名[索引]  字符串[索引]
qwerqwer=('小王是天才')
print(qwerqwer[3])#字符串[索引]
print(('小王是天才')[3])# 变量名[索引]

we=('王凯旋是天才')
for i in range(len(we)):
    print(we[i])

we=('王凯旋是天才')#for循环可以遍历任何序列的项目
for i in we:
    print(i)

#3  字符串在内存中的编码 ord()函数 ord(字符)函数只能返回一个字符的内存编码
print(ord('p'))

w='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
xiao='abcdefghijlmnopqrstuvwxyz'
for i in range(len(w)):
    print(w[i],ord(w[i]))

for i in range(len(xiao)):
    print(xiao[i],ord(xiao[i]))

# 4 编码转化为字符函数 chr(编码,参数) 用一个整数做参数返回对应的字符
# 参数可以是十进制也可以是十六进制
print(chr(89),chr(8989))
#实际应用中可以直接用关系运算符来比较字符串的关系

if 'fj'>'jfif':
    c='fj'
else:
    c='jfif'
    print(c)

# 5 输入一个字符串统计字符串里的大小写字母的数量
ui=input('请输入你的字符串')
ji=0
for i in range(len(ui)):
    if ui[i]>='a' and ui[i]<='z': #可以直接用关系运算符来比较字符的关系
        ji=ji+1

print('ji'*8)#字符串的重复输出
        
# 字符串的函数
#字符串的切片（子串）str[stsrt:stop:step]
w=('王凯旋是天才吗王凯旋真的是天才')
print(w[0:15:2])
print(w[0:4])
print(w[0:-2])


#字符串的查找函数 字符串 .('字符串') s.find('')
#查找的是字符串的第一个出现的字符的索引
#若字符串中不存在这个子串则返回 -1
wer=('王凯旋是天才大家说对还是不对')
wer1=('wang 凯 选是 天才')
print(wer.find('王凯旋'))
print(wer.find('天才'))
print(wer.find('大说'))
print(wer[13:14]) #截去最后一个字符

#返回字符串崽子附中最后一次出现的位置索引（下标）s.rfind('')
print(wer.rfind('对还'))
print(wer.index('王凯')) #s.index('')功能和s.find('')一样
                        # 不存在返回-1    不存在返回异常

# s.startswith('a')              s.endswith('a')
#字符a是否为字符串的开始字符  字符a是否为字符串结束字符
print(wer.startswith('王凯'))
print(wer.endswith('不对'))

#字符串的分裂返回列表 s.split(sep)
print(wer.split('天才'))
print(wer1.split(' '))




















