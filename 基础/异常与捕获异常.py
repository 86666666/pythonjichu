try:
    name=input('姓名')
    if name.strip()=="":
        raise Exception('无效的姓名')
    geder=input('性别')
    if geder!='男'and geder!='女':8
    raise Exception('无效的性别')
    age=input('年龄')
    age=float(age)
    if age<18 or age>30:
        raise Exception('无效的年龄')
    print(name,geder,age)
except Exception as err:
    print(err)

