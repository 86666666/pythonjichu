import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

#导入模板
from django.shortcuts import render

#作图和连接数据的的模块
import pyecharts
from pyecharts.charts import Bar   #导入柱形图
from pyecharts import options as opts #导入配置
import pymysql
import pandas as pd
from pyecharts.globals import ThemeType #导入主题
from pyecharts.charts import Pie,Line, Grid #导入饼图 折线图
from pyecharts.commons.utils import JsCode

#做表格需要模块
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
#------------------------------------------------------


#查询数据的类
class Sql_chaxun():
    '''封装一个查询数据库的类'''
    def __init__(self,sql):
        self.host1 = '主机'
        self.user1 = '用户名'
        self.passwd1 = '密码'
        self.database1 = '数据库名称'
        self.sql=sql
        self.sqlj=''

    def sql_select(self):
        try:
            con=pymysql.connect(host=self.host1,port=3306,user=self.user1,passwd=self.passwd1,db=self.database1,charset='utf8')
            print('数据库连接成功')
            #global sqljg #定义全局对象
            self.sqlj = pd.read_sql(self.sql, con)  # 1查询74队列每个服务人员手中正在处理的工单数量
            con.commit()  # 提交所有对数据库的操作，把更新写入数据库
            con.close()
            print('成功写入并关闭')
        except Exception as err:
            print(err)
        return self.sqlj


#查询数据库的语句
#1查询74队列每个服务人员手中正在处理的工单数量
sql1='''
select users.login,COUNT(ticket.id)
from ticket left join users on ticket.user_id=users.id
where ticket.queue_id=74 and ticket.ticket_state_id in (1,4) 
GROUP BY users.login
ORDER BY COUNT(ticket.id) DESC;
'''
#2查询队列中正在开着的工单数量TOP10
sql2='''
select t1.`name` 所属队列 ,COUNT(t2.tn) 
from queue t1 join ticket t2 on t1.id=t2.queue_id
where t2.ticket_state_id in (1,4)
group by t1.`name`
order by COUNT(t2.tn) desc 
limit 10;
'''

#3所有开着工单的详细信息
sql3='''
select  t2.customer_id 客户名称,t2.tn 工单id ,t2.title 工单标题,t2.create_time 工单创建时间, t1.`name` 工单即时状态,t3.`name` 所属队列, t4.login 工单负责人
from  ticket_state t1 join ticket t2 on t1.id=t2.ticket_state_id join queue t3 on t2.queue_id=t3.id join users t4 on t2.user_id=t4.id
where t2.ticket_state_id in (1,4);
'''

#4近七日新建和关闭工单数量
sql4='''
select  A.cr_time 时间,A.`新建数量`,B1.`关闭数量`
from (
select DATE_FORMAT(create_time, '%m-%d') cr_time,count(id) 新建数量
from ticket
where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_time)
GROUP BY cr_time) A
join 
(
SELECT date,count(ticket_id) 关闭数量
FROM (
SELECT DATE_FORMAT(max( CREATE_TIME),'%m-%d' ) AS date,ticket_id
FROM ticket_history 
WHERE state_id IN ( 2, 3, 10 ) and  DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(create_time)
GROUP BY ticket_id ) B
group by date) B1
ON A.cr_time=B1.date;
'''
#5每小时创建工单数量
sql5='''
select hour(t2.create_time) as h1,count(*)
from customer_company t1 left join  ticket t2 on t1.customer_id=t2.customer_id
where date(t2.create_time) =curdate()
group by h1;
'''



#6每个小时内将要超时的工单信息   customer_id not in ('RRG')
sql6='''
SELECT  t1.customer_id 客户名称,
        t1.tn 工单id,
        t1.title 工单标题,
        t1.create_time 工单创建时间,
				t2.login 工单所有者
FROM
        ticket t1 join users t2 on t1.user_id=t2.id
WHERE
        t1.ticket_state_id IN ( 1, 4 ) 
        AND t1.escalation_time not in ('0')
        AND TIMEDIFF( from_unixtime( t1.escalation_time, '%Y-%m-%d %H:%i:%s' ), t1.create_time )<= '05:00:00'
'''
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



def bar1():
    #1查询74队列每个服务人员手中正在处理的工单数量
    w=Sql_chaxun(sql1) #使用查询数据库的类
    sql1j=w.sql_select()
    c1=(
    Bar(init_opts=opts.InitOpts( width='400px',height='400px'))
    .add_yaxis('WTCCN-VEISW服务人员工单数量',list(sql1j['COUNT(ticket.id)']))
    .add_xaxis((list(sql1j['login'])))
    #bar.reversal_axis()  #将柱状图反转过来作为横着条形图
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False),
                     title_opts=opts.TitleOpts(title='SW工程师实时处理工单数量', pos_left=130,
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
    # 2查询队列中正在开着的工单数量TOP10
    w2=Sql_chaxun(sql2)
    sql2j=w2.sql_select()
    c2 = (
        Bar()
        .add_xaxis(list(sql2j['所属队列']))
        .add_yaxis('队列处理中工单数量TOP10', (list(sql2j['COUNT(t2.tn)'])),label_opts=opts.LabelOpts(position='top',color='lightcyan', font_size=20))
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
    w3=Sql_chaxun(sql3)
    sql3j=w3.sql_select()
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
    w4=Sql_chaxun(sql4)
    sql4j=w4.sql_select()
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
    w5=Sql_chaxun(sql5)
    sql5j=w5.sql_select()
    x_data = list(sql5j['h1'])
    y_data = list(sql5j['count(*)'])
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
    w6=Sql_chaxun(sql6)
    sql6j=w6.sql_select()
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

#有放大效果
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')
        #return HttpResponse(content=open("./templates/index.html").read())

#毛玻璃
class IndexView2(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'bindex.html')

#没有放大效果
class IndexView3(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'cindex.html')