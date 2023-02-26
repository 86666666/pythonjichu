import pymysql
import pandas as pd
#数据库的连接 先使用测试环境数据库

host1='rm-uf627yg12q052wzb3.mysql.rds.aliyuncs.com'
user1='veirds_uat'
passwd1='I2CN7M1inqM5WA2e'
database1='epsm_uat'

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
select hour(CONVERT_TZ(t2.create_time,'+00:00', '+08:00')) as h1, date(CONVERT_TZ(t2.create_time,'+00:00', '+08:00')) h2,count(*)
from customer_company t1 left join  ticket t2 on t1.customer_id=t2.customer_id 
where date(CONVERT_TZ(t2.create_time,'+00:00', '+08:00')) ='2022-06-15'
group by h1;
'''

#6五小时内将要超时的工单信息
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


# #print(sql1)
# db=pymysql.connect(host=host,user=user,passwd=passwd,database=database,charset='utf8')
# # 使用 cursor() 方法创建一个游标对象 cursor
# curson=db.cursor(pymysql.cursors.DictCursor)
# #使用execute（）方法执行sql查询
# curson.execute(sql1)
# print(curson.fetchone())
# db.commit()
# db.close()


try:
    con=pymysql.connect(host=host1,port=3306,user=user1,passwd=passwd1,db=database1,charset='utf8')
    print('连接成功')
    #cur=con.cursor()#获取游标对象 为元组
    cur=con.cursor(pymysql.cursors.DictCursor)  #获取游标对象 为列表
    cur.execute(sql1)#查看mysql数据库版本
    data=cur.fetchall()
    print(data)#输出mysql数据库版本
    print(type(data))
    print(len(data))
    df = pd.read_sql(sql1, con)
    print(df)
    con.commit()#提交所有对数据库的操作，把更新写入数据库
    con.close()
    print('成功写入并关闭')
except Exception as err:
    print(err)


#print(data)
