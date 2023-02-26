import tushare as ts
import numpy as np
import time
import pandas as pd
import datetime
from numba import njit
from threading import Thread#导入多线程模块
from threading import Lock #导入线程锁
# from multiprocessing import Process
# from multiprocessing import Lock


from sqlalchemy import create_engine #写入mysql库
ts.set_token('e4b96d472ce94a6fd8763c1deac5058ed3c365bd574b9ff24403ba67')#设置token
pro=ts.pro_api() #初始化api

#筛选出来沪深两市的票 是dataframe对象
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date',market='主板')
#取出每个票的股票代码放到np的ndarray数组中
data=np.array(data['ts_code'].tolist())  #花费时间 0.024003982543945312
#data=data['ts_code'].tolist()#花费时间 0.0340266227722168
#data=data['ts_code']   #花费时间 0.03227543830871582
#data=data[0:100]
#del data[52]
print(len(data))

#获取2022年交易日历
jiao_rili=pro.trade_cal(exchange='', start_date='20220101', end_date='20221231')
jiao_rili=jiao_rili[jiao_rili['is_open']==1]#1 代表交易日 过滤出每个交易日
jiao_rilia=jiao_rili['cal_date'].tolist()
jiao_rili2=np.array(jiao_rilia) #2022年交易日历

#获取今天日期
day=time.strftime("%Y%m%d") #获取当天时间
#获取昨天日期
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yes_time_nyr = yes_time.strftime('%Y%m%d')#昨天日期格式化输出

#获取60天前日期
yes_60=now_time+datetime.timedelta(days=-60)
yes_60_nyr=yes_60.strftime('%Y%m%d')#昨天日期格式化输出


def datea(a=4):
    '''获取上一个交易日 和上一个交易日之前的 若干个交易日'''
    for i in range(1, 11):
        # 获取上一个交易日日期
        if datetime.datetime.now().strftime('%H:%M:%S') < '18:00:00':
            print('当天还没有收盘,使用昨天数据')
            now_time = datetime.datetime.now()
            yes_time = now_time + datetime.timedelta(days=-i)
        else:
            yes_time=datetime.datetime.now()
            print('已经收盘了，使用今天的数据')
            if yes_time.strftime('%Y%m%d')  in jiao_rili2:
                break
            else:
                print('已经到了收盘时间，但是今天不是交易日，使用上一个交易日数据')
                now_time = datetime.datetime.now()
                yes_time = now_time + datetime.timedelta(days=-i)
        yes_time_nyr = yes_time.strftime('%Y%m%d')  # 昨天日期格式化输出
        if yes_time_nyr in jiao_rili2:
            date1 = yes_time_nyr
            break
    print(f'上一个交易日是{date1}')

    for j in range(1, 11):
        # 获取上一个交易日前若干天日期
        yes_10 = yes_time + datetime.timedelta(days=-a)
        yes_10_nyr = yes_10.strftime('%Y%m%d')  # 昨天日期格式化输出
        if yes_10_nyr in jiao_rili2:  # 判断日期是否在交易日列表中
            date2 = yes_10_nyr
            break
        a = a + j
    print(f'{a}天前的交易日是{date2}')
    return [date1, date2]  # 返回上一个交易日a 以及a之前若干天的交易日c


def dateb(b=10,c=30,d=70,e=100):
    '''获取特定交易日的函数列表'''
    d1=datea()[0] #1天前的交易日
    d5=datea()[1] #5天前的交易日
    d10=datea(b)[1] #10天前的交易日
    d30=datea(c)[1] #30天前的交易日
    d70=datea(d)[1] #70天前的交易日
    d100=datea(e)[1] #100天前的交易日
    return [d1,d5,d10,d30,d70,d100]

#涨幅计算
@njit()
def zhangfu(x,y):
    '''涨幅计算函数'''
    if y<x:
        c=(x-y)/y
    else:
        c=-((y-x)/y)
    return c

#小单占比函数
def xiaodan(i,time100):
    '''计算小单占总买入资金的占比'''
    #使用个股资金流向接口获取 每只股票的 buy_sm_amount小单买入金额  2，中单买入金额
    a = pro.moneyflow(ts_code=i, trade_date=time100[0],fields='buy_sm_amount,buy_md_amount,buy_lg_amount,buy_elg_amount')
    # 先选取三列数据返回的dataframe对象，然后取出第一行，求和
    b = a['buy_sm_amount'].loc[0] / a[['buy_sm_amount','buy_md_amount', 'buy_lg_amount', 'buy_elg_amount']].loc[0].sum()
    b='%.2f' % b
    return b


global dateframe5
# 综合pandas
def zong_dateframe():
    # 前一天收盘价
    time100 = dateb()  # 获取日期列表a=10,b=30,c=70,d=100
    global dateframe5
    dateframe5 = pd.DataFrame({'ts_code':[1], 'day1':4, 'day1-price':5, 'day5':4, 'day5-price':5, 'day10':8, 'day10-price':9,
                               'day30':90, 'day30-price':8, 'day70':8, 'day70-price':9,'day100':8, 'day100-price':9,
                               '5天涨幅':90,'10天涨幅':90,'30天涨幅':90,'70天涨幅':90,'100天涨幅':90,'小单买入占比':0})
    j=1
    for i in data:
        try:
            t=Thread(target=max_xianchen,args=(j,i,time100,))
            t.start()
            t.join()
        except:
            print('出现错误')
            continue
        j=j+1
    dateframe5=dateframe5.drop(labels=[0],axis=0)# 删除第一行
    print('pandas开始将dataframe 写入mysql中')
    from sqlalchemy import create_engine
    engine = create_engine("mysql+mysqlconnector://root:123.COMd@192.168.10.5:3306/power?charset=utf8")
    con = engine.connect()
    dateframe5.to_sql(name='ceshi', con=con, if_exists='append')
    con.close()
    print('写入数据库成功')
    return dateframe5

def max_xianchen(j,i,time100):
    '''多线程函数'''
    print(f'第{j}个{i}开始')
    d1 = pro.daily(ts_code=i, trade_date=time100[0], fields='ts_code,trade_date,close')  # 上一个交易日价格
    d5 = pro.daily(ts_code=i, trade_date=time100[1], fields='ts_code,trade_date,close')  # 5天之前价格
    d10 = pro.daily(ts_code=i, trade_date=time100[2], fields='ts_code,trade_date,close')  # 10天之前价格
    d30 = pro.daily(ts_code=i, trade_date=time100[3], fields='ts_code,trade_date,close')  # 30天前价格
    d70 = pro.daily(ts_code=i, trade_date=time100[4], fields='ts_code,trade_date,close')  # 70天前价格
    d100 = pro.daily(ts_code=i, trade_date=time100[5], fields='ts_code,trade_date,close')  # 70天前价格
    dateframe = pd.merge(d1, d5, left_on='ts_code', right_on='ts_code', how='left')
    dateframe1 = pd.merge(dateframe, d10, left_on='ts_code', right_on='ts_code', how='left')
    dateframe2 = pd.merge(dateframe1, d30, left_on='ts_code', right_on='ts_code', how='left')
    dateframe3 = pd.merge(dateframe2, d70, left_on='ts_code', right_on='ts_code', how='left')
    dateframe4 = pd.merge(dateframe3, d100, left_on='ts_code', right_on='ts_code', how='left')
    dateframe4 = dateframe4.set_axis(
        ['ts_code', 'day1', 'day1-price', 'day5', 'day5-price', 'day10', 'day10-price', 'day30', 'day30-price', 'day70',
         'day70-price',
         'day100', 'day100-price'], axis=1)
    dateframe4['5天涨幅'] = 0
    dateframe4['5天涨幅'] = '%.2f' % zhangfu(float(dateframe4['day1-price']), float(dateframe4['day5-price']))
    dateframe4['10天涨幅'] = 0
    dateframe4['10天涨幅'] = '%.2f' % zhangfu(float(dateframe4['day1-price']), float(dateframe4['day10-price']))
    dateframe4['30天涨幅'] = 0
    dateframe4['30天涨幅'] = '%.2f' % zhangfu(float(dateframe4['day1-price']), float(dateframe4['day30-price']))
    dateframe4['70天涨幅'] = 0
    dateframe4['70天涨幅'] = '%.2f' % zhangfu(float(dateframe4['day1-price']), float(dateframe4['day70-price']))
    dateframe4['100天涨幅'] = 0
    dateframe4['100天涨幅'] = '%.2f' % zhangfu(float(dateframe4['day1-price']), float(dateframe4['day100-price']))
    dateframe4['小单买入占比'] = xiaodan(i, time100)
    with lock:
        global dateframe5
        dateframe5=dateframe5.append(dateframe4, ignore_index=True)
    return 0


if __name__=='__main__':
    pass
    start_time=time.time()
    #设置锁对象
    # lock=threading.Lock()
    lock=Lock()
    bbc = zong_dateframe()

    end_time=time.time()
    zui_time=end_time-start_time
    print(bbc)
    print(zui_time)

