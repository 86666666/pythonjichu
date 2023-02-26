import numpy as np
#a9=np.arange(24).reshape(2,4,3)#csv只能存储一维和二维数组，不能存储三维或者更高维度的数组
a9=np.arange(24).reshape(4,6)
print(a9)
np.savetxt("C:\\Users\86666\Desktop\python文件处理\900.csv",a9,fmt='%d',delimiter=',')
print('写入成功')