import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar
from pyecharts import options as opts
#自己加入
from django.shortcuts import render

#作图和连接数据的的模块
import pyecharts
from pyecharts.charts import Bar   #导入柱形图
from pyecharts import options as opts #导入配置
import pymysql
import pandas as pd
from  pyecharts.globals import ThemeType #导入主题
from pyecharts.charts import Pie,Line, Grid #导入饼图 折线图
from pyecharts.charts import Line   #导入折线图
#import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
#做表格需要模块
from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts
#------------------------------------------------------


#查询数据的类
class Sql_chaxun():
    '''封装一个查询数据库的类'''
    def __init__(self,sql):
        self.host1 = 'pc-uf6a1v5f4adl90846.mysql.polardb.rds.aliyuncs.com'
        self.user1 = 'veirds'
        self.passwd1 = 'z0eR41PajDH33qmq'
        self.database1 = 'otrs'
        self.sql=sql

    def sql_select(self):
        try:
            con=pymysql.connect(host=self.host1,port=3306,user=self.user1,passwd=self.passwd1,db=self.database1,charset='utf8')
            print('数据库连接成功')
            global sql1j #定义全局对象
            sql1j = pd.read_sql(self.sql, con)  # 1查询74队列每个服务人员手中正在处理的工单数量
            con.commit()  # 提交所有对数据库的操作，把更新写入数据库
            con.close()
            print('成功写入并关闭')
        except Exception as err:
            print(err)

#查询数据库的语句
#1查询74队列每个服务人员手中正在处理的工单数量
sql1='''
select users.login,COUNT(ticket.id)
from ticket left join users on ticket.user_id=users.id
where ticket.queue_id=74 and ticket.ticket_state_id in (1,4) 
GROUP BY users.login
ORDER BY COUNT(ticket.id) DESC;
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


# def bar_base():
#     c = (
#         Bar()
#         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#         .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
#         .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
#         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
#         .dump_options_with_quotes()
#     )
#     return c

def bar1():
    #1查询74队列每个服务人员手中正在处理的工单数量
    w=Sql_chaxun(sql1) #使用查询数据库的类
    w.sql_select()
    c1=(
        Bar()
    .add_yaxis('WTCCN-VEISW服务人员工单数量',list(sql1j['COUNT(ticket.id)']))
    .add_xaxis((list(sql1j['login'])))
    #bar.reversal_axis()  #将柱状图反转过来作为横着条形图
    .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True))
    .dump_options_with_quotes() #设置对象
    )
    return c1


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(bar1()))


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')
        #return HttpResponse(content=open("./templates/index.html").read())