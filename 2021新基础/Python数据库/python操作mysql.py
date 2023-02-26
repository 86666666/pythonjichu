import pymysql
import pandas as pd
try:
    con=pymysql.connect(host='192.168.43.225',port=3306,user='root',passwd='123.COMd',db='student',charset='utf8')
    print('连接成功')
    cur=con.cursor(pymysql.cursors.DictCursor)#获取游标对象
    #sql='create table ad(so varchar(100),name varchar(20),age int(1));'
    #cur.execute(sql)
    cur.execute('select version()')#查看mysql数据库版本
    data=cur.fetchone()
    print(data)#输出mysql数据库版本
    sql="insert into ad values('19910947','sui',2);"
    cur.execute(sql)
    con.commit()#提交所有对数据库的操作，把更新写入数据库
    con.close()
    print('成功写入并关闭')
except Exception as err:
    print(err)



try:
    pass
except Exception as err:
    pass
finally:
    pass


#封装查询sql类
class Sql_chaxun():
    '''封装一个查询数据库的类'''
    def __init__(self,sql):
        self.host1 = 'pc-uf6a1v5f4adl90846.mysql.polardb.rds.aliyuncs.com'
        self.user1 = 'veirds'
        self.passwd1 = 'z0eR41PajDH33qmq'
        self.database1 = 'otrs'
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