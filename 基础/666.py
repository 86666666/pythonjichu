for i in range(1,10):  #---第一层循环用于确定行
    for j in range(1,i+1):# ---第二层循环用于确定一行打印多少公式
        print(str(j)+"x"+str(i)+"="+str(i*j),'  ',end='王凯旋的乘法表  ')
        if i==j:
            print('\n')


print('那你说王凯旋是不是一个天才呢，要是我的话我就说是的')
print('凯旋还是一个大天才呢！！！\n你可千万不哟啊不相信啊')

