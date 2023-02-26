from django.shortcuts import render
import numpy as np
import pymysql
import pandas as pd
import datetime

#定义查询mysql数据库的类

sql1='''
select * from ceshi where day1='20220923';
'''

#查询数据的类
class Sql_chaxun():
    '''封装一个查询数据库的类'''
    def __init__(self,sql):
        self.host1 = '192.168.10.2'
        self.user1 = 'root'
        self.passwd1 = '123.COMd'
        self.database1 = 'power'
        self.sql=sql
        self.sqlj=''

    def sql_select(self):
        try:
            con=pymysql.connect(host=self.host1,port=3306,user=self.user1,passwd=self.passwd1,db=self.database1,charset='utf8')
            print('数据库连接成功')
            #global sqljg #定义全局对象
            r4=[]
            self.sqlj = pd.read_sql(self.sql, con)  #
            columns_index=list(self.sqlj.columns.values) #获取dataframe的索引
            print(columns_index)
            print(self.sqlj)
            for ii2 in range(len(self.sqlj)):
                G_daima=self.sqlj.loc[ii2].tolist()[1]#G_daima 代表股票代码
                G_daima=G_daima.split('.')[0]
                print(G_daima)
                lista=self.sqlj.loc[ii2].tolist()
                lista.append(G_daima)
                r4.append(lista)
            con.commit()  # 提交所有对数据库的操作，把更新写入数据库
            con.close()
            print('成功写入并关闭')
        except Exception as err:
            print(err)
        return locals()  #将结果返回


#定义查询数据库的类
def index(request):
    import datetime
    dt=datetime.datetime.now()
    dt2=f"{dt.year}年{dt.month}月{dt.day}日  {dt.hour}时{dt.minute}分"
    a = Sql_chaxun(sql1)
    c = a.sql_select()
    c2=c['r4']
    index=c['columns_index']
    print(index)
    name = '第一个tushare项目'  # 表名称
    return render(request,'index/index.html',locals())
# Create your views here.
