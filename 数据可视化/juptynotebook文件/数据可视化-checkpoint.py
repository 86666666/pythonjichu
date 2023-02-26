#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np#导入numpy库
date=[2,3,5,6]
date2=[5,7,8,4]
date3=[34,54,23,65]
date1=np.array(date)#函数np.array()创建数组
print(date1)
date4=np.array([date1,date2,date3])#创建多维数组时子元素的数据个数必须相同
print(date4)


# In[6]:


print(type(date1))#查看数组的数据类型


# In[25]:


c=[1,2,3,4]
d=[1,2,3,4]
d1=np.array(d)#用array函数创建数组
print(c*2)#列表的乘法是复制
print(d1*2)#数组的乘法是每个元素相乘相乘


# In[14]:


#创建多维数组
date6=np.array([np.arange(2),np.arange(2)])
print(date6)


# In[17]:


print(date6.shape)#shape属性数组的形状
print(date6.dtype)#数组的类型


# In[19]:


ww=np.arange(1,9,0.5)#创建一维数组
print(ww)
print(ww.shape)
w2=np.ones((3,2,6))#创建全1数组
print(w2)
print(w2.shape)
w3=np.zeros((2,4,5))#创建全零数组
print(w3)
w4=np.eye(5)#创建正方形对角线全为1的数组
print(w4)


# In[23]:


#数组的索引与切片
a=np.array([9,8,7,6,5])
b=[9,8,7,6,5]
ui=a[1]#数组的索引
print(ui)
uii=a[1:4:2]#一维数组的切片
print(uii)
j=b[1:4:2]#列表的切片
print(j)


# In[24]:


arr=np.arange(15).reshape(3,5)
print(arr)


# In[57]:


print(arr[0])
print(len(arr))#获取数组的长度
print(arr[0][2])#获取具体的数组的元素
print(arr[0,2])#两种方法等价


# In[43]:


#一维数组的切片
shuzu=np.arange(24)#创建一个一维数组
print(shuzu)
print(shuzu[1:5])#一维数组的切片


# In[47]:


#修改数组的形状
shuzu=shuzu.reshape(4,6)#改变之前一维数组的形状成为一个三行五列的数组
print(shuzu)
#多维数组的切片
print(shuzu[:,:])#切片所有行所有列
print(shuzu[0:2,0:2])


# In[49]:


#再次改变数组的形状
shuzu=shuzu.reshape(2,3,4)
print(shuzu)


# In[52]:


#高纬度数组的切片
print(shuzu[:,1,1])
print(shuzu[:,:,0:2])


# In[59]:


x=np.array([[2,3,4,],[2,4,5,5]])
print(x)
x.shape#济源职业技术学院济源职业技术学院


# In[65]:


print(shuzu.ndim)
print(shuzu.dtype)
uii=np.full((2,3,4),90)
print(uii)
print(uii.shape)


# In[76]:


zhu=np.arange(24).reshape(2,3,4)
print(zhu)
zhu.resize(4,6)#变量.resize(shape)改变原数组
print(zhu)
print(zhu.flatten())#对数组进行降维


# In[84]:


# .astype()复制拷贝数组
xin=zhu.astype(dtype=np.int32)
new_a=xin.tolist()#数组转化为列表
print(new_a)
print(type(new_a))#查看数组的类型


# In[ ]:


# 数组与数的运算
zhu
print(zhu+6)


# In[103]:


xin1=np.arange(12).reshape(3,4)
print(xin1)
#u=xin1.mean()#计算数组的平均值
#u
r=np.square(xin1)#计算数组各元素的平方
print(r)
print(xin1==r)#比较两个数组


# In[121]:


#csv文件的保存和读取(csv文件只能有效存储一维和二维数组)
# np.savetxt()和 np.loadtxt()只能有效存储一维和二维数组
#保存文件函数np.savetxt
np.savetxt('C:\\Users\86666\Desktop\自己编写的Python程序\jia.csv',r,fmt='%d',delimiter=',')
print('保存成功')
print(csv)

#读取文件函数np.loadtxt
csvduqu=np.loadtxt('C:\\Users\86666\Desktop\自己编写的Python程序\jian.csv',dtype=np.int32,delimiter=',')
print(csvduqu)
print(type(csvduqu))


# In[127]:


#多维数组的存取
shuzu23=np.arange(24).reshape(2,3,4)
shuzu23.tofile('C:\\Users\86666\Desktop\自己编写的Python程序\zhuzu23.dat',sep=',',format='%d')
print('保存成功')

#多维数组的读取
shuzu_du=np.fromfile('C:\\Users\86666\Desktop\自己编写的Python程序\zhuzu23.dat',dtype=np.int,sep=',').reshape(shuzu23.shape)#还原数组的形状
print(shuzu_du)


# In[134]:


#numpy的便捷文件存取

np.save('a.npy',shuzu23)
print('保存成功')
bianjie_du=np.load('a.npy')
print(bianjie_du)


# In[143]:


# numpy随机数函数
np.random.randint(1,10,(2,3,4))# 返回shape形状的整数数组，取值在  (low,high] 之间左闭右开不包含high


# In[151]:


#numpy随机数函数
#numpy.random.rand(d0,d1,d2,...,dn)返回一个shape形状的数组，随机数均匀分布，分布范围为[0,1)即不包含1
xin=np.random.rand(2,3,4)
xin


# In[181]:


#numpy随机数函数
sin=np.random.randn(2,10)
print(sin)


# In[168]:


np.random.choice(a,shape,)根据指定的数组a返回shape形状的数组


# In[220]:


#ui=np.random.randint(1,11,(2,5))
ui2=np.arange(10).reshape(2,5)
print(ui2)
print(np.sum(ui))#求数组所有元素的和
print(np.min(ui2))#求数组的最小值
print(np.max(ui2))#求数组的最大值
print(np.ptp(ui2))#求数组最大值和最小值的差
print(np.median(a))#求数组的中位数
print(np.mean(a))#求数组的平均数


# In[224]:


#numpy的梯度（变化率）函数np.gradient(a)计算数组a中的元素，当a为多维数组的时候，返回每个维度的梯度
a=np.array([[1,3,4,5],[1,6,8,4]])
print(a)
np.gradient(a)

