'''
import matplotlib .pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'#修改字体必须在第一行就修改
liebaio=[2,4,5,2,7,8]
plt.plot(liebaio)
plt.title('王凯旋的图')#错误示范matplotlib本身不支持中文显示需要函数调试
plt.xlabel('x轴上的数')#修改下轴上的标签
plt.ylabel('y轴上的数')#修改y轴上的标签
plt.show()#打开matplotlib查看器
'''

with open('books.txt','wt',encoding='utf-8')as ui:
    ui.write('pyhton程序设计基础')
print('写入成功')

