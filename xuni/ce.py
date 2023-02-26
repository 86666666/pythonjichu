#查询数据库的语句
#1 每个服务人员处理中工单数量 [已完成]
sql1='''
select t2.E_MAIL 处理人, count(t1.TICKET_ID) sl
from 
VAPP_ITEM t1 join ORG_CONTACT t2 ON t1.assigned_to_contact_id=t2.ROW_ID
where t1.TICKET_STATUS IN ('Active','New','Queued')
group by  t2.E_MAIL
'''

#2, 查询队列（services ai中的支持组）中的正在开着工单数量top10 [已完成]
#目前没有10个组，所以不能用limit 10
sql2='''
select assigned_to_group_name 支持组,COUNT(TICKET_ID) value1 
from VAPP_ITEM
where TICKET_STATUS in ('Active','Complete','Escalated','New','Pending','Queued','Resolved','Resolved-Validation')
GROUP BY assigned_to_group_name 
order by value1 desc
'''

#3 所有开着工单的详细信息 [已完成]
sql3='''
 SELECT
vi.ROW_ID '系统ID',
(SELECT TOP 1 metric_value from VSLA_METRIC_CALCULATIONS as sla WHERE sla.ticket_id=vi.ROW_ID) as 'SLA所用时间(Min)',
sla_compliance_status_indicator as 'SLA状态',
ticket_identifier as '工单号',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=561) as '内部工单号',
TICKET_STATUS as '状态',
person1_org_name as '门店编号',
closed_by_group_name as '关闭组',
(closed_by_name+'.'+closed_by_last_name) as '关闭人',
ticket_description as '问题描述',
last_worklog as '最后工作日志',
DATEADD(SECOND, last_worklog_date, '1970/1/1 08:00:00') as '最后工作日志时间',
(SELECT top 1 [LVL1_CAT] +' - '+ [LVL2_CAT] FROM [VIC_HIERARCHICAL_TREE_DATA] where CHT_ID = (SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=557)) as '解决分类',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=578) as '解决办法',
(created_by_name+'.'+created_by_last_name) as '创建人',
DATEADD(SECOND, CREATED_DATE, '1970/1/1 08:00:00') as '创建时间',
(closed_by_name+'.'+closed_by_last_name) as '关单人',
DATEADD(SECOND, resolved_date, '1970/1/1 08:00:00') as '解决时间',
DATEADD(SECOND, closed_date, '1970/1/1 08:00:00') as '关闭时间',
CCTI_CLASS as '类',
CCTI_CATEGORY as '类别',
CCTI_TYPE as '类型',
CCTI_ITEM as '项目',
sla_target_name as 'SLA',
(SELECT top 1 DATEADD(SECOND, [status_created_date], '1970/1/1 08:00:00') FROM VAPP_HISTORY vh where vh.row_id = vi.ROW_ID and status='Active' order by status_created_date) as '首次响应时间',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=549) as '联系人',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=550) as '联系电话',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=552) as '上门人',
(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=553) as '上门时间',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=554) as '第二次上门人',
(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=555) as '第二次上门时间',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=556) as '第三次上门人',
(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=558) as '第三次上门时间',
person1_hierarchical_path as '组织',
person1_last_name as '城市',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=559) as 'CSS',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=560) as '反馈意见',
(SELECT TOP 1 ATTR_VALUE FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=548) as '客户单号'
from VAPP_ITEM as vi WHERE TICKET_STATUS in ('Active','New','Queued');
'''

#4 近七日新建和关闭工单数量 [已完成]
sql4='''
select a.cr_time 时间, a.asl 新建数量,b.bsl 关闭数量
from (select CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120) cr_time, COUNT(*) asl
from VAPP_ITEM
where datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120),GETDATE())<=7
group by CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120)) a
join 
(select CONVERT(VARCHAR(10),(DATEADD(S,CLOSED_DATE+8*3600,'1970-01-01 00:00:00')),120) cl_time, COUNT(*) bsl
from VAPP_ITEM
where datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CLOSED_DATE+8*3600,'1970-01-01 00:00:00')),120),GETDATE())<=7
group by CONVERT(VARCHAR(10),(DATEADD(S,CLOSED_DATE+8*3600,'1970-01-01 00:00:00')),120)) b 
on a.cr_time=b.cl_time;
'''
#5 每小时创建工单数量  [已完成]
sql5='''
select  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00'))) 时间,COUNT(*) sl
from VAPP_ITEM 
where CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')),120)=convert(VARCHAR(10),getdate(),120)
group by  DATEPART(hh, (DATEADD(S,CREATED_DATE+8*3600,'1970-01-01 00:00:00')))
'''



#6sla状态数量 [已完成]
sql6='''
select sla_compliance_status_indicator sla状态,COUNT(TICKET_ID) 数量
from 
VAPP_ITEM
GROUP BY 
sla_compliance_status_indicator
'''

sql7='''
/*
@kehu 定义查询的客户
@tianshu 定义查询的天数
@sla_target_name 定义查询工单的优先级
@CCTI_CLASS 定义ccti的类型
*/
declare @kehu VARCHAR(20)
set @kehu ='WTC';

declare @tianshu int
set @tianshu=30

declare @sla_target_name varchar(20)
set @sla_target_name='WTC - P2'

declare @CCTI_CLASS varchar(20)
set @CCTI_CLASS='HW'

select 
	t1.cr_date 日期,
	t2.Total_call,
	t3.Unclosed,
	t4.Scheduled,
	t5.P1_call,
	t6.Over_SLA,
	/*datename(day,t1.cr_date) 日期,*/
	t7.SLA_Met,
	t8.Worst_TAT,
	t9.Avg_onsite_time,
	t10.No_onsite_time,
	t11.Onsite_1,
	t12.Remote_Fixed
from
	(select convert(varchar(10),dateadd(dd,number,(getdate()-@tianshu)),120) cr_date
	from master..spt_values 
	where type = 'P'
	and number < @tianshu) 
	as t1 
left join 
/*Total Call，最近30天每日创建工单数量 不统计删除工单*/
	(select 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date, 
		COUNT(TICKET_ID) Total_call
	from 
		VAPP_ITEM
	where 
		datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		and person1_root_org_name = @kehu
		and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
	group by 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
	)
	as t2 
	on t1.cr_date=t2.cr_date
left join 
/*Unclosed 最近30天状态为开着的未关单数量，已创建时间排序*/
	(
	select 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date, 
		COUNT(TICKET_ID) Unclosed
	from 
		VAPP_ITEM
	where 
		datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30 and TICKET_STATUS IN ('Active','Complete','Escalated','New','Pending','Queued','Resolved','Resolved-Validation') and person1_root_org_name = @kehu
	group by 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
	)
	as t3 
	on t1.cr_date=t3.cr_date 
left join 
/* Scheduled  最近30天每天sla应到期工单数量且  工单状态为未关 （按照到期时间排序）   
确认工单状态
*/
	(
	SELECT
		a.cr_date,
		COUNT ( TICKET_ID ) Scheduled
	from
			(Select CONVERT (VARCHAR ( 10 ),
			DATEADD(SECOND, (select top 1 sla_due_by from VSLA_AGREEMENT_COMPLIANCE_LIST_UX as vc where vc.item_id=vi.ROW_ID order by threshold_sort_order desc), 	'1970/1/1 08:00:00') ,120) as 'cr_date',
		vi.TICKET_ID
		from VAPP_ITEM as vi where  person1_root_org_name = @kehu and TICKET_STATUS not in ('Closed','Archive','Request - Delete','Approved','Submitted') and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,vi.CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30) as a
	GROUP BY 
		a.cr_date
	)
	as t4  
	on t1.cr_date=t4.cr_date
left join 
/* P1_call 最近30天工单优先级最高的数量（按照创建时间排序）*/
	(select 
	CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
	count(TICKET_ID) P1_call
from
	VAPP_ITEM
where 
	datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30 and sla_target_name=@sla_target_name
	and person1_root_org_name = @kehu
	and TICKET_STATUS not in ('Request - Delete','Approved','Submitted')
GROUP BY 
	CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
	)
	as t5
	on t1.cr_date=t5.cr_date
left join
/*Over_SLA 最近30天工单状态已超时工单数量 按照创建时间排序 */
	(
	select 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
		count(TICKET_ID) Over_SLA
	from
		VAPP_ITEM
	where 
		sla_compliance_status_indicator='Breached SLA' and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30 and person1_root_org_name = @kehu
		and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
	GROUP by 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
	)
 as t6
 on t1.cr_date=t6.cr_date
left join
/*SLA_Met 最近30天达成率 按照创建时间排序 公式（totalcall - uniclosed - oversla）/(totalcall - uniclosed ) */
	(
	select 
		a.cr_date,
		/*(a.xjsl/b.gdsl) SLA_Met*/
		CAST(CAST(a.xjsl*1.0*100 / b.gdsl AS decimal(10,2)) AS varchar(50)) +'%' SLA_Met
	from
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date, 
			COUNT(TICKET_ID) xjsl
		from 
			VAPP_ITEM
		where 
			datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		 AND TICKET_STATUS NOT IN ('Active','Complete','Escalated','New','Pending','Queued','Resolved','Resolved-Validation','Request - Delete','Approved','Submitted')
		 AND sla_compliance_status_indicator NOT IN ('Breached SLA','SLA Not Applied')
		 and person1_root_org_name = @kehu
		group by 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		) as a 
	join 
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date, 
			COUNT(TICKET_ID) gdsl
		from 
			VAPP_ITEM
		where 
			datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		 and TICKET_STATUS NOT IN ('Active','Complete','Escalated','New','Pending','Queued','Resolved','Resolved-Validation','Request - Delete','Approved','Submitted')
		 and person1_root_org_name = @kehu
		 AND sla_compliance_status_indicator NOT IN ('SLA Not Applied')
		group by 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		) as b 
	on a.cr_date=b.cr_date
	)
	as t7
	on t1.cr_date=t7.cr_date
left join
/* Worst_TAT 最近30天每天工单处理花费最大时间 【已完成】
#原理 1，以创建时间排序 2，关单时间- 创建时间 3，工单状态为关闭 4，当天最大值*/
		(
		select 
		b.cr_date,
		max(b.zd) Worst_TAT
	from 
		(select CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
		convert(varchar(10),(DATEADD(S,CLOSED_DATE,'1970/1/1 08:00:00') -DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),108) zd
		from
		VAPP_ITEM
		where TICKET_STATUS='Closed' and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		and person1_root_org_name = @kehu
		and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
		) b
	group by 
		b.cr_date
		)
	as t8
	on t1.cr_date=t8.cr_date
left join
/* Avg_onsite_time 最近30天平均上门时间  只计算有第一次上门时间的工单 【已完成】
#单位是小时
把删除状态去除统计 */
		(
			select t.cr_date,
			/*avg(t.avg_onsitetime) Avg_onsite_time*/
			(
        SELECT
            CONVERT(VARCHAR(12), avg(t.avg_onsitetime) /60/60 % 24) + ':'
            + CONVERT(VARCHAR(2),  avg(t.avg_onsitetime) /60 % 60) + ':'
            + CONVERT(VARCHAR(2),  avg(t.avg_onsitetime) % 60)
        ) Avg_onsite_time
		from
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
			DATEDIFF(ss,DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00'),(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=553)) avg_onsitetime
		from
			VAPP_ITEM as vi
		where 
			(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=553) is not null 
			and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
			and person1_root_org_name = @kehu
			and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
            and TICKET_ID NOT IN ('472')
		) as t
		group by t.cr_date
			)
	as t9
	on t1.cr_date=t9.cr_date
left join
/*No_onsite_time 最近30天没有上门时间的工单数量且ccti=hw 按照创建时间排序 */
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
			COUNT(TICKET_ID) No_onsite_time
		from
			VAPP_ITEM as vi
		where 
			(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.		ROW_ID and va.ATTR_ID=553) is null 
			and CCTI_CLASS=@CCTI_CLASS and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
			and person1_root_org_name = @kehu
			and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
		GROUP BY 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)
	as t10
	on t1.cr_date=t10.cr_date
left join
/*Onsite_1 最近30天 重复上门工单数量 统计有第二次和第三次上门时间的工单 按照创建时间分组 */
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
			COUNT(TICKET_ID) Onsite_1
		from
			VAPP_ITEM as vi
		where 
			(SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=row_id and va.ATTR_ID=555) is not null 
			and (SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=row_id and va.ATTR_ID=558) is not null 
			and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
			and person1_root_org_name = @kehu
			and TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
		GROUP BY 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)
	as t11
	on t1.cr_date=t11.cr_date
left join 
	(
	select 
		a.cr_date,
		CAST(CAST(a.fengzi*1.0*100 / b.fengmu AS decimal(10,2)) AS varchar(50)) +'%' Remote_Fixed
	from
		(
		select 
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
			COUNT(TICKET_ID)  fengzi
		from
			VAPP_ITEM as vi
		WHERE 
		TICKET_STATUS  IN ('Closed','Archive')
		AND  (SELECT TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00') FROM VAPP_ITEM_ATTRIBUTES as va WHERE va.ITEM_ID=vi.ROW_ID and va.ATTR_ID=553) IS  NULL
		and person1_root_org_name = @kehu
		and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		group by 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)as a 
	join 
		(
		select CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
		COUNT(TICKET_ID) fengmu
		from
		VAPP_ITEM
		WHERE 
		TICKET_STATUS  IN ('Closed','Archive')
		and person1_root_org_name = @kehu
		and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=30
		GROUP BY 
		CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)as b
	on a.cr_date=b.cr_date
	) as t12
on t1.cr_date=t12.cr_date
'''
def a():
    ui=6
    return 6