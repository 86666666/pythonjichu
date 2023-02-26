#版本1
import pymssql
servername='192.168.139.21' #服务器名称
username='veii' #账户
password='ValueExch@2022'
con=pymssql.connect(server=servername,user=username,password=password,database='VEII',port='23350',charset='utf8')
print('连接成功')
cur=con.cursor() #获取游标对象
print('获取游标对象成功')
sql1='''
select  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00'))) 时间,COUNT(*)
from VAPP_ITEM
where CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120)=convert(VARCHAR(10),getdate(),120)
group by  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')))
'''
cur.execute(sql1) #执行sql语句
a2=cur.fetchall() #获取结果
con.commit() #提交对数据库的操作
con.close() #关闭数据库
print('关闭数据库成功')
print(a2)
print(type(a2))


#版本2 构造一个类来方便查询
sql1='''
select  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00'))) 时间,COUNT(*)
from VAPP_ITEM
where CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120)=convert(VARCHAR(10),getdate(),120)
group by  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')))
'''
import pymssql
class Sql_chaxun2():
    '''初始化sqlserver 连接属性'''
    def __init__(self,sql):
        self.servername='192.168.139.21' #服务器名称
        self.username='veii'  #账户
        self.port='23350' #端口号
        self.password='ValueExch@2022' #密码
        self.dabasename='VEII'
        self.sql=sql
        self.sqlj=''

    def chaxun(self):
        con=pymssql.connect(server=self.servername,user=self.username,password=self.password,database=self.dabasename,port=self.port,charset='utf8')
        print('sqlserver 连接成功')
        cur=con.cursor() #获取游标对象
        cur.execute(sql1) #执行sql语句
        self.sqlj=cur.fetchall() #获取结果
        con.commit() #提交对数据库的操作
        con.close() #关闭数据库
        print('关闭数据库成功')
        return self.sqlj

a=Sql_chaxun2(sql1)
c=a.chaxun()
print(c)


#版本3 类中使用pandas 来读取sql
sql1='''
select  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00'))) 时间,COUNT(*)
from VAPP_ITEM
where CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120)=convert(VARCHAR(10),getdate(),120)
group by  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')))
'''
import pymssql
import pandas as pd
class Sql_chaxun2():
    '''初始化sqlserver 连接属性'''
    def __init__(self,sql):
        self.servername='192.168.139.21' #服务器名称
        self.username='veii'  #账户
        self.port='23350' #端口号
        self.password='ValueExch@2022' #密码
        self.dabasename='VEII'
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

a=Sql_chaxun2(sql1)
c=a.chaxun()
print(c)
print(type(c))