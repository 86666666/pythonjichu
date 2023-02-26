
'''
定义三个变量math,chinese.english.来存储数学，语文，英语的成绩。
键盘输入的数据本质是字符串，要通过float函数转换为实数，然后才能计算
'''
math=float(input('请输入数学成绩'))
chinese=float(input('请输入语文成绩'))
english=float(input('请输入英语成绩'))
sum=math+chinese+english
print('总分为',sum,'平均成绩',sum/3)
