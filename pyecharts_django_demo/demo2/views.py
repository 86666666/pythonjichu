from django.shortcuts import render

import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

#导入模板
from django.shortcuts import render
from django.template.defaulttags import register #首先在view.py里导入register模块，这是干嘛的呢？他是Django自定义函数的
#作图和连接数据的的模块
import pyecharts
from pyecharts.charts import Bar   #导入柱形图
from pyecharts import options as opts #导入配置
import pymssql #连接sqlserver数据库的包
import pandas as pd
from pyecharts.globals import ThemeType #导入主题
from pyecharts.charts import Pie,Line, Grid #导入饼图 折线图
from pyecharts.commons.utils import JsCode
from .sql import * #导入sql语句中的变量
from pyecharts.charts import Liquid
#做表格需要模块
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
#------------------------------------------------------
# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error

#定义数据库查询类
class Sql_chaxun2():
    '''初始化sqlserver 连接属性'''
    def __init__(self,sql):
        self.servername='' #服务器名称
        self.username='用户名'  #账户
        self.port='端口号' #端口号
        self.password='密码' #密码
        self.dabasename='数据库名称'
        self.sql=sql
        self.sqlj=''

    def chaxun(self):
        con=pymssql.connect(server=self.servername,user=self.username,password=self.password,database=self.dabasename,port=self.port,charset='utf8')
        print('sqlserver 连接成功')
        self.sqlj=pd.read_sql(self.sql,con)
        con.commit() #提交对数据库的操作
        con.close() #关闭数据库
        print('关闭数据库成功')
        return self.sqlj



def bar1():
    #1每个服务人员处理中工单数量 [已完成]
    w=Sql_chaxun2(sql1) #使用查询数据库的类
    sql1j=w.chaxun()
    c1=(
    Bar(init_opts=opts.InitOpts( width='400px',height='400px'))
    .add_yaxis('WTCCN-VEISW服务人员工单数量',list(sql1j['sl']))
    .add_xaxis((list(sql1j['处理人'])))
    #bar.reversal_axis()  #将柱状图反转过来作为横着条形图
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                     title_opts=opts.TitleOpts(title='工程师处理中工单数量', pos_left=130,
                                               title_textstyle_opts=opts.TextStyleOpts(color='white', font_size=18)),
                     xaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='springgreen', width='3')),
                         axislabel_opts=opts.LabelOpts(font_size=12,position='top',rotate=45)),
                     yaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='springgreen', width='4')))
                     )
    .set_series_opts(
        itemstyle_opts={
            "normal": {
                "color": JsCode(
                    """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,color: 'rgba(0, 244, 255, 1)'}
                        ,{offset: 1,color: 'rgba(0, 77, 167, 1)'}], false)
                    """
                ),  # 调整柱子颜色渐变
                'shadowBlur': 15,  # 光影大小
                "barBorderRadius": [100, 100, 100, 100],  # 调整柱子圆角弧度
                "shadowColor": "#0EEEF9",  # 调整阴影颜色
                'shadowOffsetY': 2,
                'shadowOffsetX': 2,  # 偏移量
            }
        }

    )
    .dump_options_with_quotes() #设置对象
    )
    return c1

def bar2():
    # 查询队列（services ai中的支持组）中的正在开着工单数量top10
    w2=Sql_chaxun2(sql2)
    sql2j=w2.chaxun()
    c2 = (
        Bar()
        .add_xaxis(list(sql2j['支持组']))
        .add_yaxis('支持组中工单数量TOP10', (list(sql2j['value1'])),label_opts=opts.LabelOpts(position='top',color='lightcyan', font_size=20))
        #.reversal_axis()  # 将柱状图反转过来作为横着条形图
        .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                         title_opts=opts.TitleOpts(title='队列处理中工单数量TOP10', pos_left=130,
                                                   title_textstyle_opts=opts.TextStyleOpts(color='white',
                                                                                           font_size=18)),
                         xaxis_opts=opts.AxisOpts(
                             axisline_opts=opts.AxisLineOpts(
                                 linestyle_opts=opts.LineStyleOpts(color='lightcyan', width='3')),
                             axislabel_opts=opts.LabelOpts(font_size=8,position='top',rotate=20)),
                         yaxis_opts=opts.AxisOpts(
                             axisline_opts=opts.AxisLineOpts(
                                 linestyle_opts=opts.LineStyleOpts(color='lightcyan', width='4')),
                         axislabel_opts=opts.LabelOpts(font_size=9,position='top'))

                         )
        .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode(
                        """new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,color: 'rgba(0, 244, 255, 1)'}
                            ,{offset: 1,color: 'rgba(0, 77, 167, 1)'}], false)
                        """
                    ),  # 调整柱子颜色渐变
                    'shadowBlur': 5,  # 光影大小
                    "barBorderRadius": [100, 100, 100, 100],  # 调整柱子圆角弧度
                    "shadowColor": "#0EEEF9",  # 调整阴影颜色
                    'shadowOffsetY': 2,
                    'shadowOffsetX': 2,  # 偏移量
                }
            }
        )
        .dump_options_with_quotes()  # 设置对象
        )
    return c2

def pie1():
    # 3所有开着工单的详细信息  饼图--饼图相比其他图形 要求数据是一对一对的
    w3=Sql_chaxun2(sql3)
    sql3j=w3.chaxun()
    c1 = pd.DataFrame(sql3j.groupby('客户名称').size().sort_values(ascending=False).head(10).index)
    c2 = pd.DataFrame(sql3j.groupby('客户名称').size().sort_values(ascending=False).head(10).values)
    c3 = (
        Pie()
            .add("", [list(z) for z in zip(c1['客户名称'], c2[0])])
            .set_colors(["aqua", "greenyellow", "lightcyan", "red", "pink", "orange", "purple",'deeppink','darkred','darkslategray'])
            .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                         title_opts=opts.TitleOpts(title='处理中工单数量', pos_left=300,pos_top=1,
                                                   title_textstyle_opts=opts.TextStyleOpts(color='white',
                                                                                           font_size=18)),
                         xaxis_opts=opts.AxisOpts(
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='red', width='3')),
                             axislabel_opts=opts.LabelOpts(font_size=17)),
                         yaxis_opts=opts.AxisOpts(
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='red', width='4')))
                         )
            # .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .dump_options_with_quotes()
    )
    return c3

def line1():
    # 4近七日新建和关闭工单数量
    w4=Sql_chaxun2(sql4)
    sql4j=w4.chaxun()
    c4 = (
    Line()
    .add_xaxis(list(sql4j['时间']))
    .add_yaxis('新建数量', list(sql4j['新建数量']), label_opts=opts.LabelOpts(position='top', color='mediumspringgreen', font_size=20, ),
               linestyle_opts=opts.LineStyleOpts(is_show=False, width=3, color='mediumspringgreen'))
    .add_yaxis("关闭数量", list(sql4j['关闭数量']), label_opts=opts.LabelOpts(position='bottom', color='blueviolet', font_size=20),
               linestyle_opts=opts.LineStyleOpts(is_show=False, width=3, color='blueviolet'))
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=True,pos_top=20,textstyle_opts=opts.TextStyleOpts(color='Brown',font_size=15)),
                     title_opts=opts.TitleOpts(title='近七日新建和关闭工单数量', pos_left=130,
                                               title_textstyle_opts=opts.TextStyleOpts(color='white',
                                                                                       font_size=18)),
                     xaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(
                             linestyle_opts=opts.LineStyleOpts(color='lime', width='4')),
                         axislabel_opts=opts.LabelOpts(font_size=12)),
                     yaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(
                             linestyle_opts=opts.LineStyleOpts(color='lime', width='4')))
                     )
    .dump_options_with_quotes()
    )
    return c4


def line2():
    # 5每小时创建工单数量
    """
    参考地址: https://gallery.echartsjs.com/editor.html?c=xEyDk1hwBx
    """
    w5=Sql_chaxun2(sql5)
    sql5j=w5.chaxun()
    x_data = list(sql5j['时间'])
    y_data = list(sql5j['sl'])
    c5 = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis("每小时创建工单数量()", y_data)
        # legend_opts 图例配置项 配置了图例为圆形  最后还是直接关闭了图例配置项，因为图裂旁边的文字搞不定
        # title_opts  配置了标题文字内容  标题文字颜色 标题文字大小

        .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                         title_opts=opts.TitleOpts(title='每小时创建工单数量', pos_left='120',
                                                   title_textstyle_opts=opts.TextStyleOpts(color='white',
                                                                                           font_size=18)),
                         xaxis_opts=opts.AxisOpts(
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='aqua', width=3)),
                             axislabel_opts=opts.LabelOpts(font_size=17),type_='value',split_number=12),
                         yaxis_opts=opts.AxisOpts(
                             is_show=False,
                             axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color='aqua', width=4)))
                         )
        .set_series_opts(
            # 标签配置项 配置了标签颜色为 黄色
            label_opts=opts.LabelOpts(color='yellow', font_size=13),
            # 线样式配置项 配置了线宽 配置了颜色
            linestyle_opts=opts.LineStyleOpts(is_show=False, width=3, color='rgb(128, 128, 128)'),
            # 标记点配置项目 配置了最大值
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", symbol='circle')],
                                              symbol_size=20),

        )
        .dump_options_with_quotes()
    )

    return c5

def bar3():
    w6=Sql_chaxun2(sql6)
    sql6j=w6.chaxun()
    c3 = pd.DataFrame(sql6j.groupby('客户名称').size().sort_values(ascending=False).index)
    c4 = pd.DataFrame(sql6j.groupby('客户名称').size().sort_values(ascending=False).values)
    c6 =(
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_yaxis('将要超时{5H}  & 已超时', list(c4[0]))
    .add_xaxis(list(c3['客户名称']))
    # bar.reversal_axis()  #将柱状图反转过来作为横着条形图
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                     title_opts=opts.TitleOpts(title='将要超时{5H}  & 已超时', pos_left='130',
                                               title_textstyle_opts=opts.TextStyleOpts(color='white',
                                                                                       font_size=18)),
                     xaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(
                             linestyle_opts=opts.LineStyleOpts(color='yellow', width=3)),
                         axislabel_opts=opts.LabelOpts(font_size=12, position='top', rotate=20)),
                     yaxis_opts=opts.AxisOpts(
                         axisline_opts=opts.AxisLineOpts(
                             linestyle_opts=opts.LineStyleOpts(color='yellow', width=4)),

                     )
                     )
    .dump_options_with_quotes()
    )
    return c6

#talbe1 返回报表
def baifeng(a):
    '''专为 Remote_Fixed和SLA_Met 字段求百分比定义的函数 '''
    a = str(a)
    b1 = c[a][c[a] != 0].astype('str')  # 过滤掉为0的行 并将数据类型设置为str
    a2 = []
    for i in b1:
        str(i)
        i2 = i.rstrip('%')  # 去除每个字符串后面的百分号
        a2.append(i2)  # 将循环得到的结果保存到列表中
    a3 = pd.Series(a2).astype('float64')  # 用列表建立serries对象，因为列表无法求和
    a3 = ('%.2f' % a3.mean() + '%')  # 格式化输入浮点数 然后加上%号
    return a3

#模板不支持range函数
@register.filter
def get_range(value):
    return range(len(value))

#wtc 报表1
def baobiao(request):
    # 第一步：获取数据
    a = Sql_chaxun2(sql7)  # 调用类实例化对象与查询sql语句
    global c
    c = a.chaxun()  # 调用类的chaxun方法执行sql然后返回结果

    # 第二步：数据清洗和列类型转换

    c = c.fillna(0)  # 空值用0填充
    # 修改列的数据类型
    c['Total_call'] = c['Total_call'].astype('int64')  # 将Total_call 的float64类型改为int64
    c['P1_call'] = c['P1_call'].astype('int64')  # 将P1_call 的float64类型改为int64
    # c['SLA_Met']=c['SLA_Met'].astype('int64')       #将SLA_Met 的float64类型改为int64
    c['No_onsite_time'] = c['No_onsite_time'].astype('int64')  # 将No_onsite_time  的float64类型改为int64

    # 第三步：数据整理
    # 将x轴的索引取出放到列表中，然后在将列表转化为series类型，最后合并到dateframe类型中
    i4 = []
    for i in (c.columns):
        i4.append(i)
    del i4[0]  # 删除日期 解决 指标 对接 30天指标汇总错误问题
    i5 = pd.Series(i4)  # 将列表类型转化为Series类型

    c['指标'] = i5  # 新建一个列 列名为指标 并将series类型合并到dataframe类型中

    # 以下下时进行30天指标汇总计算代码

    c['30天指标汇总'] = 0
    c['30天指标汇总'][0] = c['Total_call'].sum()
    c['30天指标汇总'][1] = c['Unclosed'].sum()
    c['30天指标汇总'][2] = c['Scheduled'].sum()
    c['30天指标汇总'][3] = c['P1_call'].sum()
    c['30天指标汇总'][4] = c['Over_SLA'].sum()
    c['30天指标汇总'][5] = baifeng('SLA_Met')  # 使用函数求值
    c['30天指标汇总'][6] = c['Worst_TAT'][c['Worst_TAT'] != 0].astype('str').max()  # 过滤掉时间中不为0的值 将数据类型转化为字符串
    # Avg_onsite_time 求值
    Avg_onsite_time1 = pd.to_datetime(c['Avg_onsite_time'][c['Avg_onsite_time'] != 0],
                                      format='%H:%M:%S')  # 过滤掉值为0的行，然后将数据类型转换为datetime
    Avg_onsite_time2 = str(Avg_onsite_time1.mean()).split(' ')[1]  # 将 平均值05:42:55.090909184  转化为字符串 ，然后以空格分割为列表
    Avg_onsite_time = Avg_onsite_time2.split('.')[0]
    c['30天指标汇总'][7] = Avg_onsite_time
    c['30天指标汇总'][8] = (c['No_onsite_time'].dropna().sum())
    c['30天指标汇总'][9] = (c['Onsite_1'].dropna().sum())
    c['30天指标汇总'][10] = baifeng('Remote_Fixed')  # 使用函数求值

    c = c.fillna(0)  # 空值用0填充
    del c['指标'][12]
    del c['指标'][13]
    r3 = []
    for r2 in range(len(c)):
        r3.append(c.loc[r2].tolist())

    return render(request,'baobiao1.html',locals())

#wtc 报表2 横着过来
def baobiao2(request):
    # 第一步：获取数据
    a = Sql_chaxun2(sql8)  # 调用类实例化对象与查询sql语句
    d = a.chaxun()  # 调用类的chaxun方法执行sql然后返回结果
    # i1 = []
    # for i in (d.columns):
    #     print(i)
    #     i1.append(i)
    d = d.fillna(0)
    r4 = []
    for r2 in range(len(d)):
        r4.append(d.loc[r2].tolist())
    return render(request,'baobiao2.html',locals())

#bar()
class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar1()))

#bar2()
class ChartView2(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar2()))

#pie1()
class ChartView3(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(pie1()))

#line1
class ChartView4(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line1()))

#line2
class ChartView5(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(line2()))


#bar3
class ChartView6(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar3()))

#table1 图7
class ChartView7(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(baobiao()))


#看板首页 版本1
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'2index.html')

#看板首页 版本2
class IndexView3(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'3index.html')


#报表的html
class IndexView2(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'baobiao1.html',locals())
