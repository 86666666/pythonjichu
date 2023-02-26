#n=float(input('请输入一个数字'))
# a=['google','baidu','runoob','toaboa',90]
# print(type(a))
# for i in range(len(a)):
#     print(i,a[i])
#
name=2
name2=name
name=7
name2=name
print(name2)
print(name)
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,'   ',end='')
    print('\n')