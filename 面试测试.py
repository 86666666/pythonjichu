import os
import sys
import re

#path 文件前缀
#打印出所有在该目录path下，含有文件前缀的文件路径  /var/log

# 第一步  将path路径传入到os库的获取指定目录所有文件路径的函数
# 第二步 将第一步返回的数据转化为列表
# 第三步 通过re库的正则表达式 将/var/log 转化为 查询字符串 然后去匹配第二步返回的数据类型

path=r'C:\Users\86666'
zheng=re.compile(r'tk')
def walk(path):
  if not os.path.exists(path):
    return -1
  list=[]
  for root,dirs,names in os.walk(path):
    for filename in names:7
      c=(os.path.join(root,filename)) #路径和文件名连接构成完整路径
      jieguo = zheng.match(c)
      list.append(jieguo)

ui=walk(path)
print(ui)
