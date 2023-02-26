import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
pro=ts.pro_api('7240fde9e07a9cc82db49161b8f85769186c321ca754a13ded7722f0')#初始化pro接口
try:
    df11 = pro.daily(ts_code='002094.SZ')#获取某一只股票的日线行情数据
    #print(df11)
    #print(df11['trade_date'])
    df11['trade_date']=pd.to_datetime(df11['trade_date'])#将字符串转化为时间序列对象
    #print(df11['trade_date'])
#将时间序列转化为index索引
    df12=df11.set_index('trade_date')
except Exception as err:
    print(err)
print(df12)
df12.plot()
plt.show()#显示绘图


