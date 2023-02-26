m=float(input('请输入学生的成绩'))
if m<0 or m>100:
    print('不可能的，你输错了')#if语句只执行一个条件
elif m>=90:
    print('a')
elif m>=80:
    print('b')
elif m>=70:
    print('c')
elif m>=60:
    print('d')
else:
    print('你太垃圾了')
