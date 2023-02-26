f=open('嫩模联系方式.txt','at+',encoding='utf-8')#rt+ at+ wt+可读可写
f.write('wangkaixuna\n')
print(f.tell())
f.write('王凯旋是天才')
print(f.read())
f.close()