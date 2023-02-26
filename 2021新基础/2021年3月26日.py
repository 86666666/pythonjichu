s='wangkaixuan'
a=' WANGKAIXUAN 1'
print(s.title())
print(s.upper())
print(a.lower())
print(a.lstrip('w'))
print(s.strip('w',))

while True:
    try:
        name=input('请输入你的名字')
        name=name.strip()
        if name=='':
            raise Exception('你输入的年龄不对')
        gender=input('请输入你的性别')
        if gender!='男' and gender!='女':
            raise Exception('无效的性别')
        age=float(input('请输入你的年龄'))
        if age>30 or age<18:
            raise Exception('你输入的年龄不对')
        break
    except Exception as err:
        print(err,'请你重新输入')

print('你好你的名字是'+name,'你的年龄是'+str(age))



