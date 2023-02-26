#    字符串的类型

# 1 获取字符串长度函数 len() len('fkajf') len(s) s为变量
print(len('4555'))
s="wpmemg我们788"
print(len(s))


# 2 读取序列的项目（读取字符串的各个字符） 字符串[索引] 使用for循环遍历
s='王凯旋是天才'
print(s[5])

# 3 字符串编码函数  ord(字符)
s='wangkaixuan王凯旋是大天才'  #直接用for 循环的遍历功能
for i in s:
    print(i,ord(i))
    
s='wangkaixuan王凯旋是大天才'  #for循环
for i in range(len(s)):
    print(s[i],ord(s[i]))
    
