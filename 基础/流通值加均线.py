# 导入函数库
from jqdata import *


def initialize(context):
    # 设定沪深三百作为收益的基准
    set_benchmark('000300.XSHG')
    # 开启动态复权来设置真实的价格
    set_option('use_real_price', True)
    # 设置佣金和印花税
    set_order_cost(
        OrderCost(open_tax=0, close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5),
        type='stock')
    g.security = (get_index_stocks('399002.XSHE')) + (get_index_stocks('000001.XSHG'))  # 设置一个全局变量保存要操作的股票
    # print(str(len(g.security)),g.security)上证指数成分股加上深证指数成分股构成的列表

    # 从上证指数成分股加上深证指数成分股构成的列表中，获取筛选后总市值小于100亿大于20亿，流通值大于20亿的股票
    g.q = query(valuation).filter(valuation.code.in_(g.security), valuation.market_cap > 20, valuation.market_cap < 75,
                                  valuation.circulating_market_cap < 45)  # 查询条件过滤后所有股票的市值
    g.p1 = 5
    g.p2 = 10
    g.p3 = 60
    g.p4 = 120
    run_daily(handle, '9:45')
    # run_weekly(handle,-1)


def handle(context):
    to_sell = []
    to_tuy = []
    df = get_fundamentals(g.q)[['market_cap', 'code', 'circulating_market_cap']]  # 获取筛选后总市值小于100亿，流通值大于20亿
    # print(len(df))
    df = df.sort_values('market_cap')
    # print(df)
    list1 = df['code'].values  # 股票列表
    list1 = list(list1)
    # print(list1)

    for stock in list1:
        # print(stock)
        df = attribute_history(stock, g.p4, fields=['close', 'open'])
        # 金叉 五日均线大于10日均线并且持仓股票
        # 死叉 五日均线小于10日均线并且不持仓股票
        ma5 = df['open'][-5:].mean()
        ma10 = df['open'][-10:].mean()
        ma30 = df['open'][-30:].mean()
        ma60 = df['open'][-60:].mean()
        ma120 = df['open'].mean()

        # 死叉并且持仓就卖出
        if ma10 > ma5 and (stock in context.portfolio.positions):
            to_sell.append(stock)  # 要卖的股票列表
            # order_target(stock,0)  #卖出全部
        # 金叉但是没有持仓就买入
        if ma10 < ma5 and ma5 > ma30 and stock not in context.portfolio.positions:
            to_tuy.append(stock)  # 要买的股票列表
            # order_value(stock,context.portfolio.available_cash*0) #按照可用资金的80%买入
    print('买', len(to_tuy))
    # print(to_tuy)
    print('卖', len(to_sell))
    # print(to_sell)

    # #卖出
    # #卖出

    # if len(to_sell)>0:
    #     for stock in to_sell:
    #         order_target(stock,0)#卖出全部

    # #买入
    # mai=context.portfolio.available_cash/len(to_tuy)
    # if len(to_tuy)>0:
    #     for stock in to_tuy:
    #         order_value(stock,mai)#按剩余钱的平均买入
    # print(to_tuy)

