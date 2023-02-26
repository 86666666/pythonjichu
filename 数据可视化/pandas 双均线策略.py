import pandas as pd  #导入需要用到的包
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts
#pro=ts.pro_api('e4b96d472ce94a6fd8763c1deac5058ed3c365bd574b9ff24403ba67')
ts.set_token('e4b96d472ce94a6fd8763c1deac5058ed3c365bd574b9ff24403ba67')#设置token

#通用行情接口获取股票的数据
#pro=ts.pro_api('7240fde9e07a9cc82db49161b8f85769186c321ca754a13ded7722f0')
dfa=ts.pro_bar(ts_code='002199.SZ',asset='E',freq='D',ma=[5,30,80,255])#未复权
dfa['trade_date']=pd.to_datetime(dfa['trade_date'],format='%Y%m%d')#将trade_date转化为时间序列对象
dfa=dfa.set_index('trade_date')#将trade_date列设置为行索引
dfa=dfa.dropna()#删除所有包含缺失值的行
dfa=dfa.drop('ma_v_5',axis=1)
dfa=dfa.drop('ma_v_30',axis=1)
dfa=dfa.drop('ma_v_80',axis=1)
dfa=dfa.drop('ma_v_255',axis=1)
# 用循环找出金叉和死叉
jincha = []
shicha = []
for i in range(1, len(dfa)):
    if dfa['ma5'][i] >= dfa['ma30'][i] and dfa['ma5'][i - 1] < dfa['ma30'][i - 1]:
        jincha.append(str(dfa.index[i]))
    if dfa['ma5'][i] <= dfa['ma30'][i] and dfa['ma5'][i - 1] > dfa['ma30'][i - 1]:
        shicha.append(str(dfa.index[i]))

print(jincha)
print(shicha)
# 不用循环找出金叉和死叉
sr1=dfa['ma5']<dfa['ma30']
sr2=dfa['ma5']>=dfa['ma30']
shicha=dfa[sr1 & sr2.shift(1)]#死叉
jincha=dfa[-(sr1 | sr2.shift(1))]#金叉
jingchalist=dfa[-(sr1|sr2.shift(1))].index
shichalist=dfa[sr1 & sr2.shift(1)].index
print('--------------死叉----------')
print(shichalist)
print('--------------金叉----------')
print(jingchalist)


first_money=100000
money=first_money
hold=0  #持有的股数
sr1=pd.Series(1,index=jingchalist)#用金叉日期来构造series
sr2=pd.Series(0,index=shichalist)
sr=sr1.append(sr2).sort_index()#将两个series合并成一个series并按照索引进行排序

for i in range(0, len(sr)):
    # p=dfa['open'][sr.index[i]]
    if sr.iloc[i] == 1:
        # print(sr.iloc[i])
        p = dfa['open'][sr.index[i]]
        # 金叉买入
        buy = (money // (p * 100))  # 可以买多少手股
        hold = hold + (buy * 100)  # 持有的股票数
        money = money - (buy * 100 * p)  # 买完后剩下的钱
    else:
        # 死叉卖出
        money = money + (hold * p)
        hold = 0

# 最后一天交易日的价格
p = dfa['open'][-1]
now_money = hold * p + money
print(now_money - first_money)

