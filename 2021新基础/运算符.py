p=int(input('请输入一个你喜欢的数字'))
while True:
    if p%2==0:#判断p是否为偶数
        print(str(p)+'是偶数')
        break#是偶数就退出循环
    else:
        for i in range(3):#循环打印三次奇数
            print(str(p)+'是奇数')
        break#循环三次后退出循环



#判断一个字母是否为小写
n=input('请输入一个字符')
if n>='a' and n<='z':
    print(n+'是小写字母')
else:
    print(n+'不是小写字母')



#计算学生平均成绩
shuxue=float(input('请输入你的数学成绩'))
yingyu=float(input('请输入你的英语成绩'))
yuwen=float(input('请输入你的语文成绩'))
zonghe=(shuxue+yingyu+yuwen)//3
print('你好你的各科的平均成绩是'+str(zonghe))