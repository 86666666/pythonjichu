# 导入函数库
from jqdata import *


# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)

    # 过滤掉order系列API产生的比error级别低的log
    # log.set_level('order', 'error')

    ### 股票相关设定 ###
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5),
                   type='stock')

    # 变量保存要操作的股票
    g.security = get_index_stocks('000002.XSHG')

    # 用query函数取得query对象并用filter函数按条件过滤
    g.q = query(valuation).filter(valuation.code.in_(g.security))  # 查询沪深三百所有股票的市值
    # ft=get_fundamentals(g.q,date='20200819')#
    # print(ft[['market_cap','code']])
    # 定时运行函数每个月第一个交易日运行
    run_monthly(handle, 1, time='9:35')  #


def handle(context):
    df = get_fundamentals(g.q)[['market_cap', 'code']]
    df = df.sort_values('market_cap')

    # log.info(df)
    df = df['code'][0:20]  # 球的每日市值最小的20只股票
    # log.info(df.values)#返回股票列表

    to_hold = df.values  # 要持有的股票列表
    # log.info(to_hold)

    # 查看手里持仓的股票是否在筛选出来的要购买并持有的列表里,若手中持有的股票不在筛选出来的列表里则全部卖出
    try:
        for stock in context.portfolio.positions:
            if stock not in to_hold:
                order_target(stock, 0)  # 全部卖出
    except:
        print('出现错误')

    # 查看筛选出来的，是否已经购买持仓，没有就筛选出来添加到列表里，再用剩余的钱除以列表里的股票数，平均分下来的钱买入每只股票
    to_buy = []
    for stock in to_hold:
        if stock in context.portfolio.positions:
            to_buy.append(stock)  # 没有持仓的股票添加到列表里

    if len(to_buy) > 0:
        cash = context.portfolio.available_cash / len(to_buy)  # 分配给每只股票的钱
        for stock in to_buy:
            order_value(stock, cash)


## 开盘前运行函数
def before_market_open(context):
    pass


## 开盘时运行函数
def market_open(context):
    pass


## 收盘后运行函数
def after_market_close(context):
    pass