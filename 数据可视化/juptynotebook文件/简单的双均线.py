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
    g.security = ['601318.XSHG']  # 设置一个全局变量保存要操作的股票
    g.p1 = 5
    g.p2 = 10

    # run_weekly(handle,1,time='9:31')设置每周一运行

    # df=attribute_history(g.security,g.p2)
    # log.info(df)
    # m5=df['open']
    # print(m5)
    # print(m5[-5:])


def handle_data(context, data):
    for stock in g.security:
        df = attribute_history(stock, g.p2)
        # 金叉 五日均线大于10日均线并且持仓股票
        # 死叉 五日均线小于10日均线并且不持仓股票
        ma5 = df['open'][-5:].mean()
        ma10 = df['open'].mean()

        # 死叉卖出
        # #判断持仓的一种方法
        # print(g.security)
        # if ma10>ma5 and context.portfolio.positions[stock].total_amount >0:
        if ma10 > ma5 and stock in context.portfolio.positions:
            order_target(stock, 0)  # 卖出全部
        # 金叉买入
        if ma10 < ma5 and stock not in context.portfolio.positions:
            order_value(stock, context.portfolio.available_cash * 0.8)  # 按照可用资金的80%买入


## 开盘前运行函数
def before_market_open(context):
    pass


## 开盘时运行函数
def market_open(context):
    pass


## 收盘后运行函数
def after_market_close(context):
    pass