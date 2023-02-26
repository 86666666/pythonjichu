# import pandas  as pd
# from sqlalchemy import create_engine
# a={'c':89,'b':89}
# a=pd.DataFrame(a,index=[0])
#
# engine=create_engine("mysql+mysqlconnector://root:123.COMd@192.168.10.4:3306/power?charset=utf8")
# con=engine.connect()
# a.to_sql(name='ceshi',con=con,if_exists='append')
# con.close()
# print('写入数据库成功')

#continue 用法
# import numpy as np
# a=list(np.arange(100))
# for i in a:
#     if i==12:
#         continue
#     print(i)

import tushare as ts

ts.set_token('e4b96d472ce94a6fd8763c1deac5058ed3c365bd574b9ff24403ba67')#设置token
pro=ts.pro_api() #初始化api
# a=pro.moneyflow(ts_code='002149.SZ',trade_date='20190315',fields='buy_sm_amount,buy_md_amount,buy_lg_amount,buy_elg_amount')
# #print(a)
# b=a['buy_sm_amount'].loc[0] / a[['buy_md_amount','buy_lg_amount','buy_elg_amount']].loc[0].sum() #先选取三列数据返回的dataframe对象，然后取出第一行，求和
# #d=a[['buy_md_amount','buy_lg_amount','buy_elg_amount']]
# print(b)
#
# def xiaodan(i,time100):
#     '''计算小单占比函数'''
#     #使用个股资金流向接口获取 每只股票的 buy_sm_amount小单买入金额  2，中单买入金额
#     a = pro.moneyflow(ts_code=i, trade_date=time100[0],fields='buy_sm_amount,buy_md_amount,buy_lg_amount,buy_elg_amount')
#     # 先选取三列数据返回的dataframe对象，然后取出第一行，求和
#     b = a['buy_sm_amount'].loc[0] / a[['buy_md_amount', 'buy_lg_amount', 'buy_elg_amount']].loc[0].sum()
#     b='%.2f' % b
#     return b

a=pro.bak_basic(exchange='SSE;SZSE')
print(a)