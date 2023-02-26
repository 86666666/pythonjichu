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


sql8='''
/*
本报表统计屈臣氏客户在30天内的KPI值：
Total Call  工单总数
Unclosed    未关单总数
Scheduled   预计解决数量
P1 call#    P1紧急工单数量
Over SLA#   超SLA数量
SLA Met%    SLA达成率
Worst TAT   当天完成跨度最长的工单所花的时间
Remote Fixed    远程解决率
Max late close  系统操作关闭时间-实际关闭时间之间的差值，该栏位列出最大的差值所花的时间，ServiceAI没有实际关单时间，可不统计。
Repeat Call#    重复Call数量，ServiceAI没有该计算值，暂不统计。
Avg onsite time 平均上门时间
No Onsite time  没有上门时间的数量
Onsite# > 1 上门次数大于1次的数量
*/

/*@kehu 定义报表统计的客户*/
declare @kehu VARCHAR(20)
set @kehu ='WTC'

/*@天数 定义报表统计的的天数*/
declare @tianshu int
set @tianshu=30
declare @tianshu2 int
set @tianshu2=@tianshu-1

/*@sla_target_name 定义查询工单的优先级*/
declare @sla_target_name varchar(20)
set @sla_target_name='WTC-P1'

/*@group 定义No Onsite time中硬件组的名称*/
--declare @group varchar(20)
--set @group=''L1-HW-SH','L1-HW-BJ','L1-HW-GZ','L1-HW-SZ''

/*@CCTI_CLASS 定义No Onsite time中ccti为硬件的类型*/
declare @CCTI_CLASS varchar(20)
set @CCTI_CLASS='HW'

/*Total Call  30天内的每天创建的工单数量(不统计已删除工单)*/
SELECT
    '—',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'Total Call' KPI,
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t1.c AS Total_Call,
        case when datediff(dd, t1.cr_date, getdate()) =1 then t1.c else '' end as D1,
        case when datediff(dd, t1.cr_date, getdate()) =2 then t1.c else '' end as D2,
        case when datediff(dd, t1.cr_date, getdate()) =3 then t1.c else '' end as D3,
        case when datediff(dd, t1.cr_date, getdate()) =4 then t1.c else '' end as D4,
        case when datediff(dd, t1.cr_date, getdate()) =5 then t1.c else '' end as D5,
        case when datediff(dd, t1.cr_date, getdate()) =6 then t1.c else '' end as D6,
        case when datediff(dd, t1.cr_date, getdate()) =7 then t1.c else '' end as D7,
        case when datediff(dd, t1.cr_date, getdate()) =8 then t1.c else '' end as D8,
        case when datediff(dd, t1.cr_date, getdate()) =9 then t1.c else '' end as D9,
        case when datediff(dd, t1.cr_date, getdate()) =10 then t1.c else '' end as D10,
        case when datediff(dd, t1.cr_date, getdate()) =11 then t1.c else '' end as D11,
        case when datediff(dd, t1.cr_date, getdate()) =12 then t1.c else '' end as D12,
        case when datediff(dd, t1.cr_date, getdate()) =13 then t1.c else '' end as D13,
        case when datediff(dd, t1.cr_date, getdate()) =14 then t1.c else '' end as D14,
        case when datediff(dd, t1.cr_date, getdate()) =15 then t1.c else '' end as D15,
        case when datediff(dd, t1.cr_date, getdate()) =16 then t1.c else '' end as D16,
        case when datediff(dd, t1.cr_date, getdate()) =17 then t1.c else '' end as D17,
        case when datediff(dd, t1.cr_date, getdate()) =18 then t1.c else '' end as D18,
        case when datediff(dd, t1.cr_date, getdate()) =19 then t1.c else '' end as D19,
        case when datediff(dd, t1.cr_date, getdate()) =20 then t1.c else '' end as D20,
        case when datediff(dd, t1.cr_date, getdate()) =21 then t1.c else '' end as D21,
        case when datediff(dd, t1.cr_date, getdate()) =22 then t1.c else '' end as D22,
        case when datediff(dd, t1.cr_date, getdate()) =23 then t1.c else '' end as D23,
        case when datediff(dd, t1.cr_date, getdate()) =24 then t1.c else '' end as D24,
        case when datediff(dd, t1.cr_date, getdate()) =25 then t1.c else '' end as D25,
        case when datediff(dd, t1.cr_date, getdate()) =26 then t1.c else '' end as D26,
        case when datediff(dd, t1.cr_date, getdate()) =27 then t1.c else '' end as D27,
        case when datediff(dd, t1.cr_date, getdate()) =28 then t1.c else '' end as D28,
        case when datediff(dd, t1.cr_date, getdate()) =29 then t1.c else '' end as D29,
        case when datediff(dd, t1.cr_date, getdate()) =30 then t1.c else '' end as D30
    FROM (
        SELECT
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
                COUNT(TICKET_ID) c
            FROM
                VAPP_ITEM
            WHERE
                datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
                AND person1_root_org_name = @kehu
                AND TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
            GROUP BY
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
        ) AS t1
    ) AS A
UNION ALL
/*Unclosed 30天内的每天创建后，状态未关闭的工单数量(不统计已删除工单)*/
SELECT
    '—',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'Unclosed',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t2.c AS Unclosed,
        case when datediff(dd, t2.cr_date, getdate()) =1 then t2.c else '' end as D1,
        case when datediff(dd, t2.cr_date, getdate()) =2 then t2.c else '' end as D2,
        case when datediff(dd, t2.cr_date, getdate()) =3 then t2.c else '' end as D3,
        case when datediff(dd, t2.cr_date, getdate()) =4 then t2.c else '' end as D4,
        case when datediff(dd, t2.cr_date, getdate()) =5 then t2.c else '' end as D5,
        case when datediff(dd, t2.cr_date, getdate()) =6 then t2.c else '' end as D6,
        case when datediff(dd, t2.cr_date, getdate()) =7 then t2.c else '' end as D7,
        case when datediff(dd, t2.cr_date, getdate()) =8 then t2.c else '' end as D8,
        case when datediff(dd, t2.cr_date, getdate()) =9 then t2.c else '' end as D9,
        case when datediff(dd, t2.cr_date, getdate()) =10 then t2.c else '' end as D10,
        case when datediff(dd, t2.cr_date, getdate()) =11 then t2.c else '' end as D11,
        case when datediff(dd, t2.cr_date, getdate()) =12 then t2.c else '' end as D12,
        case when datediff(dd, t2.cr_date, getdate()) =13 then t2.c else '' end as D13,
        case when datediff(dd, t2.cr_date, getdate()) =14 then t2.c else '' end as D14,
        case when datediff(dd, t2.cr_date, getdate()) =15 then t2.c else '' end as D15,
        case when datediff(dd, t2.cr_date, getdate()) =16 then t2.c else '' end as D16,
        case when datediff(dd, t2.cr_date, getdate()) =17 then t2.c else '' end as D17,
        case when datediff(dd, t2.cr_date, getdate()) =18 then t2.c else '' end as D18,
        case when datediff(dd, t2.cr_date, getdate()) =19 then t2.c else '' end as D19,
        case when datediff(dd, t2.cr_date, getdate()) =20 then t2.c else '' end as D20,
        case when datediff(dd, t2.cr_date, getdate()) =21 then t2.c else '' end as D21,
        case when datediff(dd, t2.cr_date, getdate()) =22 then t2.c else '' end as D22,
        case when datediff(dd, t2.cr_date, getdate()) =23 then t2.c else '' end as D23,
        case when datediff(dd, t2.cr_date, getdate()) =24 then t2.c else '' end as D24,
        case when datediff(dd, t2.cr_date, getdate()) =25 then t2.c else '' end as D25,
        case when datediff(dd, t2.cr_date, getdate()) =26 then t2.c else '' end as D26,
        case when datediff(dd, t2.cr_date, getdate()) =27 then t2.c else '' end as D27,
        case when datediff(dd, t2.cr_date, getdate()) =28 then t2.c else '' end as D28,
        case when datediff(dd, t2.cr_date, getdate()) =29 then t2.c else '' end as D29,
        case when datediff(dd, t2.cr_date, getdate()) =30 then t2.c else '' end as D30
    FROM (
        SELECT
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            COUNT(TICKET_ID) c
        FROM
            VAPP_ITEM
        WHERE
            datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            AND TICKET_STATUS IN ('Active','Complete','Escalated','New','Pending','Queued','Resolved','Resolved-Validation')
            AND person1_root_org_name = @kehu
        GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
        ) AS t2
    ) AS A
UNION ALL
/*Scheduled  30天内，每天sla应到期工单数量且工单状态为未关*/
SELECT
    '—',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'Scheduled',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t3.c AS Scheduled,
        case when datediff(dd, t3.cr_date, getdate()) =1 then t3.c else '' end as D1,
        case when datediff(dd, t3.cr_date, getdate()) =2 then t3.c else '' end as D2,
        case when datediff(dd, t3.cr_date, getdate()) =3 then t3.c else '' end as D3,
        case when datediff(dd, t3.cr_date, getdate()) =4 then t3.c else '' end as D4,
        case when datediff(dd, t3.cr_date, getdate()) =5 then t3.c else '' end as D5,
        case when datediff(dd, t3.cr_date, getdate()) =6 then t3.c else '' end as D6,
        case when datediff(dd, t3.cr_date, getdate()) =7 then t3.c else '' end as D7,
        case when datediff(dd, t3.cr_date, getdate()) =8 then t3.c else '' end as D8,
        case when datediff(dd, t3.cr_date, getdate()) =9 then t3.c else '' end as D9,
        case when datediff(dd, t3.cr_date, getdate()) =10 then t3.c else '' end as D10,
        case when datediff(dd, t3.cr_date, getdate()) =11 then t3.c else '' end as D11,
        case when datediff(dd, t3.cr_date, getdate()) =12 then t3.c else '' end as D12,
        case when datediff(dd, t3.cr_date, getdate()) =13 then t3.c else '' end as D13,
        case when datediff(dd, t3.cr_date, getdate()) =14 then t3.c else '' end as D14,
        case when datediff(dd, t3.cr_date, getdate()) =15 then t3.c else '' end as D15,
        case when datediff(dd, t3.cr_date, getdate()) =16 then t3.c else '' end as D16,
        case when datediff(dd, t3.cr_date, getdate()) =17 then t3.c else '' end as D17,
        case when datediff(dd, t3.cr_date, getdate()) =18 then t3.c else '' end as D18,
        case when datediff(dd, t3.cr_date, getdate()) =19 then t3.c else '' end as D19,
        case when datediff(dd, t3.cr_date, getdate()) =20 then t3.c else '' end as D20,
        case when datediff(dd, t3.cr_date, getdate()) =21 then t3.c else '' end as D21,
        case when datediff(dd, t3.cr_date, getdate()) =22 then t3.c else '' end as D22,
        case when datediff(dd, t3.cr_date, getdate()) =23 then t3.c else '' end as D23,
        case when datediff(dd, t3.cr_date, getdate()) =24 then t3.c else '' end as D24,
        case when datediff(dd, t3.cr_date, getdate()) =25 then t3.c else '' end as D25,
        case when datediff(dd, t3.cr_date, getdate()) =26 then t3.c else '' end as D26,
        case when datediff(dd, t3.cr_date, getdate()) =27 then t3.c else '' end as D27,
        case when datediff(dd, t3.cr_date, getdate()) =28 then t3.c else '' end as D28,
        case when datediff(dd, t3.cr_date, getdate()) =29 then t3.c else '' end as D29,
        case when datediff(dd, t3.cr_date, getdate()) =30 then t3.c else '' end as D30
    FROM (
        SELECT
            a.cr_date,
            COUNT ( TICKET_ID ) c
        FROM
            (SELECT
                CONVERT (
                    VARCHAR ( 10 ),DATEADD(
                        SECOND,
                        (
                        SELECT
                            top 1 sla_due_by
                        FROM
                            VSLA_AGREEMENT_COMPLIANCE_LIST_UX AS vc
                        WHERE
                            vc.item_id=vi.ROW_ID
                        ORDER BY
                            threshold_sort_order DESC
                        ), '1970/1/1 08:00:00'
                        ),120
                    ) AS 'cr_date',
                vi.TICKET_ID
            FROM
                VAPP_ITEM AS vi
            WHERE
                person1_root_org_name = @kehu
                AND TICKET_STATUS not in ('closed','Request - Delete','archive','Approved','Submitted')
                AND datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,vi.CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            ) AS a
        GROUP BY
            a.cr_date
            ) AS t3
    ) AS A
UNION ALL
/* P1_call 30天内创建的工单，优先级最高的数量(不统计已删除工单)*/
SELECT
    '—',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'P1 call',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t4.c AS P1_call,
        case when datediff(dd, t4.cr_date, getdate()) =1 then t4.c else '' end as D1,
        case when datediff(dd, t4.cr_date, getdate()) =2 then t4.c else '' end as D2,
        case when datediff(dd, t4.cr_date, getdate()) =3 then t4.c else '' end as D3,
        case when datediff(dd, t4.cr_date, getdate()) =4 then t4.c else '' end as D4,
        case when datediff(dd, t4.cr_date, getdate()) =5 then t4.c else '' end as D5,
        case when datediff(dd, t4.cr_date, getdate()) =6 then t4.c else '' end as D6,
        case when datediff(dd, t4.cr_date, getdate()) =7 then t4.c else '' end as D7,
        case when datediff(dd, t4.cr_date, getdate()) =8 then t4.c else '' end as D8,
        case when datediff(dd, t4.cr_date, getdate()) =9 then t4.c else '' end as D9,
        case when datediff(dd, t4.cr_date, getdate()) =10 then t4.c else '' end as D10,
        case when datediff(dd, t4.cr_date, getdate()) =11 then t4.c else '' end as D11,
        case when datediff(dd, t4.cr_date, getdate()) =12 then t4.c else '' end as D12,
        case when datediff(dd, t4.cr_date, getdate()) =13 then t4.c else '' end as D13,
        case when datediff(dd, t4.cr_date, getdate()) =14 then t4.c else '' end as D14,
        case when datediff(dd, t4.cr_date, getdate()) =15 then t4.c else '' end as D15,
        case when datediff(dd, t4.cr_date, getdate()) =16 then t4.c else '' end as D16,
        case when datediff(dd, t4.cr_date, getdate()) =17 then t4.c else '' end as D17,
        case when datediff(dd, t4.cr_date, getdate()) =18 then t4.c else '' end as D18,
        case when datediff(dd, t4.cr_date, getdate()) =19 then t4.c else '' end as D19,
        case when datediff(dd, t4.cr_date, getdate()) =20 then t4.c else '' end as D20,
        case when datediff(dd, t4.cr_date, getdate()) =21 then t4.c else '' end as D21,
        case when datediff(dd, t4.cr_date, getdate()) =22 then t4.c else '' end as D22,
        case when datediff(dd, t4.cr_date, getdate()) =23 then t4.c else '' end as D23,
        case when datediff(dd, t4.cr_date, getdate()) =24 then t4.c else '' end as D24,
        case when datediff(dd, t4.cr_date, getdate()) =25 then t4.c else '' end as D25,
        case when datediff(dd, t4.cr_date, getdate()) =26 then t4.c else '' end as D26,
        case when datediff(dd, t4.cr_date, getdate()) =27 then t4.c else '' end as D27,
        case when datediff(dd, t4.cr_date, getdate()) =28 then t4.c else '' end as D28,
        case when datediff(dd, t4.cr_date, getdate()) =29 then t4.c else '' end as D29,
        case when datediff(dd, t4.cr_date, getdate()) =30 then t4.c else '' end as D30
    FROM (
        SELECT
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            count(TICKET_ID) c
        FROM
            VAPP_ITEM
        WHERE
            datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            AND sla_target_name=@sla_target_name
            AND person1_root_org_name = @kehu
            AND TICKET_STATUS not in ('Request - Delete','Approved','Submitted')
        GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
        ) AS t4
    ) AS A
UNION ALL
/*Over_SLA 30天创建的工单，状态已关闭，SLA已超时工单数量*/
SELECT
    '—',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'Over SLA',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t5.c AS Over_SLA,
        case when datediff(dd, t5.cr_date, getdate()) =1 then t5.c else '' end as D1,
        case when datediff(dd, t5.cr_date, getdate()) =2 then t5.c else '' end as D2,
        case when datediff(dd, t5.cr_date, getdate()) =3 then t5.c else '' end as D3,
        case when datediff(dd, t5.cr_date, getdate()) =4 then t5.c else '' end as D4,
        case when datediff(dd, t5.cr_date, getdate()) =5 then t5.c else '' end as D5,
        case when datediff(dd, t5.cr_date, getdate()) =6 then t5.c else '' end as D6,
        case when datediff(dd, t5.cr_date, getdate()) =7 then t5.c else '' end as D7,
        case when datediff(dd, t5.cr_date, getdate()) =8 then t5.c else '' end as D8,
        case when datediff(dd, t5.cr_date, getdate()) =9 then t5.c else '' end as D9,
        case when datediff(dd, t5.cr_date, getdate()) =10 then t5.c else '' end as D10,
        case when datediff(dd, t5.cr_date, getdate()) =11 then t5.c else '' end as D11,
        case when datediff(dd, t5.cr_date, getdate()) =12 then t5.c else '' end as D12,
        case when datediff(dd, t5.cr_date, getdate()) =13 then t5.c else '' end as D13,
        case when datediff(dd, t5.cr_date, getdate()) =14 then t5.c else '' end as D14,
        case when datediff(dd, t5.cr_date, getdate()) =15 then t5.c else '' end as D15,
        case when datediff(dd, t5.cr_date, getdate()) =16 then t5.c else '' end as D16,
        case when datediff(dd, t5.cr_date, getdate()) =17 then t5.c else '' end as D17,
        case when datediff(dd, t5.cr_date, getdate()) =18 then t5.c else '' end as D18,
        case when datediff(dd, t5.cr_date, getdate()) =19 then t5.c else '' end as D19,
        case when datediff(dd, t5.cr_date, getdate()) =20 then t5.c else '' end as D20,
        case when datediff(dd, t5.cr_date, getdate()) =21 then t5.c else '' end as D21,
        case when datediff(dd, t5.cr_date, getdate()) =22 then t5.c else '' end as D22,
        case when datediff(dd, t5.cr_date, getdate()) =23 then t5.c else '' end as D23,
        case when datediff(dd, t5.cr_date, getdate()) =24 then t5.c else '' end as D24,
        case when datediff(dd, t5.cr_date, getdate()) =25 then t5.c else '' end as D25,
        case when datediff(dd, t5.cr_date, getdate()) =26 then t5.c else '' end as D26,
        case when datediff(dd, t5.cr_date, getdate()) =27 then t5.c else '' end as D27,
        case when datediff(dd, t5.cr_date, getdate()) =28 then t5.c else '' end as D28,
        case when datediff(dd, t5.cr_date, getdate()) =29 then t5.c else '' end as D29,
        case when datediff(dd, t5.cr_date, getdate()) =30 then t5.c else '' end as D30
    FROM (
        SELECT
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            count(TICKET_ID) c
        FROM
            VAPP_ITEM
        WHERE
            sla_compliance_status_indicator='Breached SLA'
            AND datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            AND person1_root_org_name = @kehu
            AND TICKET_STATUS IN ('closed','archive')
        GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
            ) AS t5
    ) AS A
UNION ALL
/*插入日期t6*/
SELECT
    'Target',
    'ALL',
    'KPI',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        case when datediff(dd, t6.cr_date, getdate()) =1 then t6.c else '' end as D1,
        case when datediff(dd, t6.cr_date, getdate()) =2 then t6.c else '' end as D2,
        case when datediff(dd, t6.cr_date, getdate()) =3 then t6.c else '' end as D3,
        case when datediff(dd, t6.cr_date, getdate()) =4 then t6.c else '' end as D4,
        case when datediff(dd, t6.cr_date, getdate()) =5 then t6.c else '' end as D5,
        case when datediff(dd, t6.cr_date, getdate()) =6 then t6.c else '' end as D6,
        case when datediff(dd, t6.cr_date, getdate()) =7 then t6.c else '' end as D7,
        case when datediff(dd, t6.cr_date, getdate()) =8 then t6.c else '' end as D8,
        case when datediff(dd, t6.cr_date, getdate()) =9 then t6.c else '' end as D9,
        case when datediff(dd, t6.cr_date, getdate()) =10 then t6.c else '' end as D10,
        case when datediff(dd, t6.cr_date, getdate()) =11 then t6.c else '' end as D11,
        case when datediff(dd, t6.cr_date, getdate()) =12 then t6.c else '' end as D12,
        case when datediff(dd, t6.cr_date, getdate()) =13 then t6.c else '' end as D13,
        case when datediff(dd, t6.cr_date, getdate()) =14 then t6.c else '' end as D14,
        case when datediff(dd, t6.cr_date, getdate()) =15 then t6.c else '' end as D15,
        case when datediff(dd, t6.cr_date, getdate()) =16 then t6.c else '' end as D16,
        case when datediff(dd, t6.cr_date, getdate()) =17 then t6.c else '' end as D17,
        case when datediff(dd, t6.cr_date, getdate()) =18 then t6.c else '' end as D18,
        case when datediff(dd, t6.cr_date, getdate()) =19 then t6.c else '' end as D19,
        case when datediff(dd, t6.cr_date, getdate()) =20 then t6.c else '' end as D20,
        case when datediff(dd, t6.cr_date, getdate()) =21 then t6.c else '' end as D21,
        case when datediff(dd, t6.cr_date, getdate()) =22 then t6.c else '' end as D22,
        case when datediff(dd, t6.cr_date, getdate()) =23 then t6.c else '' end as D23,
        case when datediff(dd, t6.cr_date, getdate()) =24 then t6.c else '' end as D24,
        case when datediff(dd, t6.cr_date, getdate()) =25 then t6.c else '' end as D25,
        case when datediff(dd, t6.cr_date, getdate()) =26 then t6.c else '' end as D26,
        case when datediff(dd, t6.cr_date, getdate()) =27 then t6.c else '' end as D27,
        case when datediff(dd, t6.cr_date, getdate()) =28 then t6.c else '' end as D28,
        case when datediff(dd, t6.cr_date, getdate()) =29 then t6.c else '' end as D29,
        case when datediff(dd, t6.cr_date, getdate()) =30 then t6.c else '' end as D30
    FROM (
        SELECT
            t.cr_date,
            datename(day,t.cr_date) c
        FROM
            (
            SELECT
                convert(varchar(10),dateadd(dd,number,(getdate()-@tianshu)),120) cr_date
            FROM
                master..spt_values
            WHERE
                type = 'P'
                AND number < @tianshu
            ) AS t
        ) AS t6
    )AS A
UNION ALL
/*SLA_Met 最近30天创建的工单，SLA达成率，只计算关闭的工单。公式（达成SLA工单数量）/(总工单数量) */
SELECT
    '90%',
    CAST(convert(decimal(16,2), CAST(sum(isnull(A.xjsl,0)) AS decimal(10,2)) *1.00*100 / CAST(sum(isnull(A.gdsl,0)) AS decimal(10,2))) AS varchar(50)) +'%',
    'SLA Met',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t7.c AS SLA_Met,
        t7.xjsl,
        t7.gdsl,
        case when datediff(dd, t7.cr_date, getdate()) =1 then t7.c else '' end as D1,
        case when datediff(dd, t7.cr_date, getdate()) =2 then t7.c else '' end as D2,
        case when datediff(dd, t7.cr_date, getdate()) =3 then t7.c else '' end as D3,
        case when datediff(dd, t7.cr_date, getdate()) =4 then t7.c else '' end as D4,
        case when datediff(dd, t7.cr_date, getdate()) =5 then t7.c else '' end as D5,
        case when datediff(dd, t7.cr_date, getdate()) =6 then t7.c else '' end as D6,
        case when datediff(dd, t7.cr_date, getdate()) =7 then t7.c else '' end as D7,
        case when datediff(dd, t7.cr_date, getdate()) =8 then t7.c else '' end as D8,
        case when datediff(dd, t7.cr_date, getdate()) =9 then t7.c else '' end as D9,
        case when datediff(dd, t7.cr_date, getdate()) =10 then t7.c else '' end as D10,
        case when datediff(dd, t7.cr_date, getdate()) =11 then t7.c else '' end as D11,
        case when datediff(dd, t7.cr_date, getdate()) =12 then t7.c else '' end as D12,
        case when datediff(dd, t7.cr_date, getdate()) =13 then t7.c else '' end as D13,
        case when datediff(dd, t7.cr_date, getdate()) =14 then t7.c else '' end as D14,
        case when datediff(dd, t7.cr_date, getdate()) =15 then t7.c else '' end as D15,
        case when datediff(dd, t7.cr_date, getdate()) =16 then t7.c else '' end as D16,
        case when datediff(dd, t7.cr_date, getdate()) =17 then t7.c else '' end as D17,
        case when datediff(dd, t7.cr_date, getdate()) =18 then t7.c else '' end as D18,
        case when datediff(dd, t7.cr_date, getdate()) =19 then t7.c else '' end as D19,
        case when datediff(dd, t7.cr_date, getdate()) =20 then t7.c else '' end as D20,
        case when datediff(dd, t7.cr_date, getdate()) =21 then t7.c else '' end as D21,
        case when datediff(dd, t7.cr_date, getdate()) =22 then t7.c else '' end as D22,
        case when datediff(dd, t7.cr_date, getdate()) =23 then t7.c else '' end as D23,
        case when datediff(dd, t7.cr_date, getdate()) =24 then t7.c else '' end as D24,
        case when datediff(dd, t7.cr_date, getdate()) =25 then t7.c else '' end as D25,
        case when datediff(dd, t7.cr_date, getdate()) =26 then t7.c else '' end as D26,
        case when datediff(dd, t7.cr_date, getdate()) =27 then t7.c else '' end as D27,
        case when datediff(dd, t7.cr_date, getdate()) =28 then t7.c else '' end as D28,
        case when datediff(dd, t7.cr_date, getdate()) =29 then t7.c else '' end as D29,
        case when datediff(dd, t7.cr_date, getdate()) =30 then t7.c else '' end as D30
    FROM (
        SELECT
            a.cr_date,
            a.xjsl,
            b.gdsl,
            CAST(convert(decimal(16,2),CAST(a.xjsl*1.0*100 / b.gdsl AS decimal(10,2))) AS varchar(50)) +'%' c
        FROM
            (
            SELECT
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
                COUNT(TICKET_ID) xjsl
            FROM
                VAPP_ITEM
            WHERE
                datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
                AND TICKET_STATUS IN ('closed','archive')
                AND sla_compliance_status_indicator NOT IN ('Breached SLA','SLA Not Applied')
                AND person1_root_org_name = @kehu
            GROUP BY
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
            )
            AS a
        join
            (
            SELECT
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
                COUNT(TICKET_ID) gdsl
            FROM
                VAPP_ITEM
            WHERE
                datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
                AND TICKET_STATUS IN ('closed','archive')
                AND sla_compliance_status_indicator NOT IN ('SLA Not Applied')
                AND person1_root_org_name = @kehu
            GROUP BY
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
            )
            AS b
            ON a.cr_date=b.cr_date
        ) AS t7
    ) AS A
UNION ALL
/* Worst_TAT 30天内创建的工单，处理工单所花费最长时间时间跨度的工单的时间值，关闭时间-创建时间(只计算关闭的工单)*/
SELECT
    '24:00',
    MAX(A.Worst_TAT),
    'Worst TAT',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t8.c AS Worst_TAT,
        case when datediff(dd, t8.cr_date, getdate()) =1 then t8.c else '' end as D1,
        case when datediff(dd, t8.cr_date, getdate()) =2 then t8.c else '' end as D2,
        case when datediff(dd, t8.cr_date, getdate()) =3 then t8.c else '' end as D3,
        case when datediff(dd, t8.cr_date, getdate()) =4 then t8.c else '' end as D4,
        case when datediff(dd, t8.cr_date, getdate()) =5 then t8.c else '' end as D5,
        case when datediff(dd, t8.cr_date, getdate()) =6 then t8.c else '' end as D6,
        case when datediff(dd, t8.cr_date, getdate()) =7 then t8.c else '' end as D7,
        case when datediff(dd, t8.cr_date, getdate()) =8 then t8.c else '' end as D8,
        case when datediff(dd, t8.cr_date, getdate()) =9 then t8.c else '' end as D9,
        case when datediff(dd, t8.cr_date, getdate()) =10 then t8.c else '' end as D10,
        case when datediff(dd, t8.cr_date, getdate()) =11 then t8.c else '' end as D11,
        case when datediff(dd, t8.cr_date, getdate()) =12 then t8.c else '' end as D12,
        case when datediff(dd, t8.cr_date, getdate()) =13 then t8.c else '' end as D13,
        case when datediff(dd, t8.cr_date, getdate()) =14 then t8.c else '' end as D14,
        case when datediff(dd, t8.cr_date, getdate()) =15 then t8.c else '' end as D15,
        case when datediff(dd, t8.cr_date, getdate()) =16 then t8.c else '' end as D16,
        case when datediff(dd, t8.cr_date, getdate()) =17 then t8.c else '' end as D17,
        case when datediff(dd, t8.cr_date, getdate()) =18 then t8.c else '' end as D18,
        case when datediff(dd, t8.cr_date, getdate()) =19 then t8.c else '' end as D19,
        case when datediff(dd, t8.cr_date, getdate()) =20 then t8.c else '' end as D20,
        case when datediff(dd, t8.cr_date, getdate()) =21 then t8.c else '' end as D21,
        case when datediff(dd, t8.cr_date, getdate()) =22 then t8.c else '' end as D22,
        case when datediff(dd, t8.cr_date, getdate()) =23 then t8.c else '' end as D23,
        case when datediff(dd, t8.cr_date, getdate()) =24 then t8.c else '' end as D24,
        case when datediff(dd, t8.cr_date, getdate()) =25 then t8.c else '' end as D25,
        case when datediff(dd, t8.cr_date, getdate()) =26 then t8.c else '' end as D26,
        case when datediff(dd, t8.cr_date, getdate()) =27 then t8.c else '' end as D27,
        case when datediff(dd, t8.cr_date, getdate()) =28 then t8.c else '' end as D28,
        case when datediff(dd, t8.cr_date, getdate()) =29 then t8.c else '' end as D29,
        case when datediff(dd, t8.cr_date, getdate()) =30 then t8.c else '' end as D30
    FROM (
        SELECT
            b.cr_date,
            max(b.zd) c
        FROM
            (
            SELECT
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
                CONVERT(VARCHAR(10),(DATEADD(S,CLOSED_DATE,'1970/1/1 08:00:00') - DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),108) zd
            FROM
                VAPP_ITEM
            WHERE
                datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
                AND person1_root_org_name = @kehu
                AND TICKET_STATUS IN ('closed','archive')
            ) b
        GROUP BY
                b.cr_date
            ) AS t8
    ) AS A
UNION ALL
/*Remote_Fixed 最近30天创建的工单，远程解决率，只计算关闭的工单。公式（第一次上门时间为空的工单数）/(总工单数量) */
SELECT
    '30%',
    CAST(convert(decimal(16,2), CAST(sum(isnull(A.fengzi,0)) AS decimal(10,2)) *1.00*100 / CAST(sum(isnull(A.fengmu,0)) AS decimal(10,2))) AS varchar(50)) +'%',
    'Remote Fixed',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t9.c AS Remote_Fixed,
        t9.fengzi,
        t9.fengmu,
        case when datediff(dd, t9.cr_date, getdate()) =1 then t9.c else '' end as D1,
        case when datediff(dd, t9.cr_date, getdate()) =2 then t9.c else '' end as D2,
        case when datediff(dd, t9.cr_date, getdate()) =3 then t9.c else '' end as D3,
        case when datediff(dd, t9.cr_date, getdate()) =4 then t9.c else '' end as D4,
        case when datediff(dd, t9.cr_date, getdate()) =5 then t9.c else '' end as D5,
        case when datediff(dd, t9.cr_date, getdate()) =6 then t9.c else '' end as D6,
        case when datediff(dd, t9.cr_date, getdate()) =7 then t9.c else '' end as D7,
        case when datediff(dd, t9.cr_date, getdate()) =8 then t9.c else '' end as D8,
        case when datediff(dd, t9.cr_date, getdate()) =9 then t9.c else '' end as D9,
        case when datediff(dd, t9.cr_date, getdate()) =10 then t9.c else '' end as D10,
        case when datediff(dd, t9.cr_date, getdate()) =11 then t9.c else '' end as D11,
        case when datediff(dd, t9.cr_date, getdate()) =12 then t9.c else '' end as D12,
        case when datediff(dd, t9.cr_date, getdate()) =13 then t9.c else '' end as D13,
        case when datediff(dd, t9.cr_date, getdate()) =14 then t9.c else '' end as D14,
        case when datediff(dd, t9.cr_date, getdate()) =15 then t9.c else '' end as D15,
        case when datediff(dd, t9.cr_date, getdate()) =16 then t9.c else '' end as D16,
        case when datediff(dd, t9.cr_date, getdate()) =17 then t9.c else '' end as D17,
        case when datediff(dd, t9.cr_date, getdate()) =18 then t9.c else '' end as D18,
        case when datediff(dd, t9.cr_date, getdate()) =19 then t9.c else '' end as D19,
        case when datediff(dd, t9.cr_date, getdate()) =20 then t9.c else '' end as D20,
        case when datediff(dd, t9.cr_date, getdate()) =21 then t9.c else '' end as D21,
        case when datediff(dd, t9.cr_date, getdate()) =22 then t9.c else '' end as D22,
        case when datediff(dd, t9.cr_date, getdate()) =23 then t9.c else '' end as D23,
        case when datediff(dd, t9.cr_date, getdate()) =24 then t9.c else '' end as D24,
        case when datediff(dd, t9.cr_date, getdate()) =25 then t9.c else '' end as D25,
        case when datediff(dd, t9.cr_date, getdate()) =26 then t9.c else '' end as D26,
        case when datediff(dd, t9.cr_date, getdate()) =27 then t9.c else '' end as D27,
        case when datediff(dd, t9.cr_date, getdate()) =28 then t9.c else '' end as D28,
        case when datediff(dd, t9.cr_date, getdate()) =29 then t9.c else '' end as D29,
        case when datediff(dd, t9.cr_date, getdate()) =30 then t9.c else '' end as D30
    FROM (
        select
		a.cr_date,
        a.fengzi,
        b.fengmu,
		CAST(convert(decimal(16,2), CAST(a.fengzi*1.00*100 / b.fengmu AS decimal(10,2))) AS varchar(50)) +'%' c
	from
		(
		select
			CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
			COUNT(TICKET_ID)  fengzi
		from
			VAPP_ITEM as vi
		WHERE
            TICKET_STATUS  IN ('Closed','Archive')
            AND  (
                SELECT
                    TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
                FROM
                    VAPP_ITEM_ATTRIBUTES as va
                WHERE
                    va.ITEM_ID=vi.ROW_ID
                    and va.ATTR_ID=553) IS  NULL
            and person1_root_org_name = @kehu
            and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=@tianshu
		group by
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)
        as a
	join
		(
		select
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            COUNT(TICKET_ID) fengmu
		from
            VAPP_ITEM
		WHERE
            TICKET_STATUS  IN ('Closed','Archive')
            and person1_root_org_name = @kehu
            and datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<=@tianshu
		GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
		)
        as b
	on a.cr_date=b.cr_date
        ) AS t9
    ) AS A
UNION ALL
/* Avg_onsite_time 30天内创建的工单，每日平均上门时间  只计算有第一次上门时间的工单。(不统计删除工单) #单位是小时*/
SELECT
    '1:00',
    --将总平均值转换为时间格式
    (SELECT
        CONVERT(VARCHAR(12), avg(A.Avg_onsite_time) /60/60 % 24) + ':'
        + CONVERT(VARCHAR(2),  avg(A.Avg_onsite_time) /60 % 60) + ':'
        + CONVERT(VARCHAR(2),  avg(A.Avg_onsite_time) % 60)
    ),
    'Avg Onsite Time',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t8.d AS Avg_onsite_time,
        case when datediff(dd, t8.cr_date, getdate()) =1 then t8.c else '' end as D1,
        case when datediff(dd, t8.cr_date, getdate()) =2 then t8.c else '' end as D2,
        case when datediff(dd, t8.cr_date, getdate()) =3 then t8.c else '' end as D3,
        case when datediff(dd, t8.cr_date, getdate()) =4 then t8.c else '' end as D4,
        case when datediff(dd, t8.cr_date, getdate()) =5 then t8.c else '' end as D5,
        case when datediff(dd, t8.cr_date, getdate()) =6 then t8.c else '' end as D6,
        case when datediff(dd, t8.cr_date, getdate()) =7 then t8.c else '' end as D7,
        case when datediff(dd, t8.cr_date, getdate()) =8 then t8.c else '' end as D8,
        case when datediff(dd, t8.cr_date, getdate()) =9 then t8.c else '' end as D9,
        case when datediff(dd, t8.cr_date, getdate()) =10 then t8.c else '' end as D10,
        case when datediff(dd, t8.cr_date, getdate()) =11 then t8.c else '' end as D11,
        case when datediff(dd, t8.cr_date, getdate()) =12 then t8.c else '' end as D12,
        case when datediff(dd, t8.cr_date, getdate()) =13 then t8.c else '' end as D13,
        case when datediff(dd, t8.cr_date, getdate()) =14 then t8.c else '' end as D14,
        case when datediff(dd, t8.cr_date, getdate()) =15 then t8.c else '' end as D15,
        case when datediff(dd, t8.cr_date, getdate()) =16 then t8.c else '' end as D16,
        case when datediff(dd, t8.cr_date, getdate()) =17 then t8.c else '' end as D17,
        case when datediff(dd, t8.cr_date, getdate()) =18 then t8.c else '' end as D18,
        case when datediff(dd, t8.cr_date, getdate()) =19 then t8.c else '' end as D19,
        case when datediff(dd, t8.cr_date, getdate()) =20 then t8.c else '' end as D20,
        case when datediff(dd, t8.cr_date, getdate()) =21 then t8.c else '' end as D21,
        case when datediff(dd, t8.cr_date, getdate()) =22 then t8.c else '' end as D22,
        case when datediff(dd, t8.cr_date, getdate()) =23 then t8.c else '' end as D23,
        case when datediff(dd, t8.cr_date, getdate()) =24 then t8.c else '' end as D24,
        case when datediff(dd, t8.cr_date, getdate()) =25 then t8.c else '' end as D25,
        case when datediff(dd, t8.cr_date, getdate()) =26 then t8.c else '' end as D26,
        case when datediff(dd, t8.cr_date, getdate()) =27 then t8.c else '' end as D27,
        case when datediff(dd, t8.cr_date, getdate()) =28 then t8.c else '' end as D28,
        case when datediff(dd, t8.cr_date, getdate()) =29 then t8.c else '' end as D29,
        case when datediff(dd, t8.cr_date, getdate()) =30 then t8.c else '' end as D30
    FROM (
        SELECT
            b.cr_date,
            --计算总平均值
            AVG(b.zd) d,
            --将日平均值转时间格式
            (
            SELECT
                CONVERT(VARCHAR(12), avg(b.zd) /60/60 % 24) + ':'
                + CONVERT(VARCHAR(2),  avg(b.zd) /60 % 60) + ':'
                + CONVERT(VARCHAR(2),  avg(b.zd) % 60)
            ) c
        FROM
            (
            SELECT
                CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
                --如果上门时间早于创建时间，赋NULL。如果晚于创建时间，计算差值
                CASE WHEN(
                    SELECT
                        TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
                    FROM
                        VAPP_ITEM_ATTRIBUTES AS va
                    WHERE va.ITEM_ID=vi.ROW_ID
                    AND va.ATTR_ID=553
                    )  > DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')
				THEN
                    DATEDIFF(
                    ss,DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00'),(
                        SELECT
                            TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
                        FROM
                            VAPP_ITEM_ATTRIBUTES AS va
                        WHERE
                            va.ITEM_ID=vi.ROW_ID
                            AND va.ATTR_ID=553
                        )
                    )
				ELSE
					NULL 
				END AS zd
                --判断到此结束
            FROM
                VAPP_ITEM AS vi
            WHERE
                (
                SELECT
                    TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
                FROM
                    VAPP_ITEM_ATTRIBUTES AS va
                WHERE
                    va.ITEM_ID=vi.ROW_ID
                    AND va.ATTR_ID=553
                ) is not null
                AND datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
                AND person1_root_org_name = @kehu
                AND TICKET_STATUS IN ('closed','archive')
            ) b
            GROUP BY
                b.cr_date
            ) AS t8
    ) AS A
UNION ALL
/*No_onsite_time 30天内创建的工单，统计每天派给了硬件ccti=hw但是没有第一次上门时间的。(不统计删除工单)*/
SELECT
    '0',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'No Onsite Time',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t11.c AS No_onsite_time,
        case when datediff(dd, t11.cr_date, getdate()) =1 then t11.c else '' end as D1,
        case when datediff(dd, t11.cr_date, getdate()) =2 then t11.c else '' end as D2,
        case when datediff(dd, t11.cr_date, getdate()) =3 then t11.c else '' end as D3,
        case when datediff(dd, t11.cr_date, getdate()) =4 then t11.c else '' end as D4,
        case when datediff(dd, t11.cr_date, getdate()) =5 then t11.c else '' end as D5,
        case when datediff(dd, t11.cr_date, getdate()) =6 then t11.c else '' end as D6,
        case when datediff(dd, t11.cr_date, getdate()) =7 then t11.c else '' end as D7,
        case when datediff(dd, t11.cr_date, getdate()) =8 then t11.c else '' end as D8,
        case when datediff(dd, t11.cr_date, getdate()) =9 then t11.c else '' end as D9,
        case when datediff(dd, t11.cr_date, getdate()) =10 then t11.c else '' end as D10,
        case when datediff(dd, t11.cr_date, getdate()) =11 then t11.c else '' end as D11,
        case when datediff(dd, t11.cr_date, getdate()) =12 then t11.c else '' end as D12,
        case when datediff(dd, t11.cr_date, getdate()) =13 then t11.c else '' end as D13,
        case when datediff(dd, t11.cr_date, getdate()) =14 then t11.c else '' end as D14,
        case when datediff(dd, t11.cr_date, getdate()) =15 then t11.c else '' end as D15,
        case when datediff(dd, t11.cr_date, getdate()) =16 then t11.c else '' end as D16,
        case when datediff(dd, t11.cr_date, getdate()) =17 then t11.c else '' end as D17,
        case when datediff(dd, t11.cr_date, getdate()) =18 then t11.c else '' end as D18,
        case when datediff(dd, t11.cr_date, getdate()) =19 then t11.c else '' end as D19,
        case when datediff(dd, t11.cr_date, getdate()) =20 then t11.c else '' end as D20,
        case when datediff(dd, t11.cr_date, getdate()) =21 then t11.c else '' end as D21,
        case when datediff(dd, t11.cr_date, getdate()) =22 then t11.c else '' end as D22,
        case when datediff(dd, t11.cr_date, getdate()) =23 then t11.c else '' end as D23,
        case when datediff(dd, t11.cr_date, getdate()) =24 then t11.c else '' end as D24,
        case when datediff(dd, t11.cr_date, getdate()) =25 then t11.c else '' end as D25,
        case when datediff(dd, t11.cr_date, getdate()) =26 then t11.c else '' end as D26,
        case when datediff(dd, t11.cr_date, getdate()) =27 then t11.c else '' end as D27,
        case when datediff(dd, t11.cr_date, getdate()) =28 then t11.c else '' end as D28,
        case when datediff(dd, t11.cr_date, getdate()) =29 then t11.c else '' end as D29,
        case when datediff(dd, t11.cr_date, getdate()) =30 then t11.c else '' end as D30
    FROM (
        SELECT
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            COUNT(TICKET_ID) c
        FROM
            VAPP_ITEM AS vi
        WHERE
            (
            SELECT
                TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
            FROM
                VAPP_ITEM_ATTRIBUTES AS va
            WHERE
                va.ITEM_ID=vi.ROW_ID
                AND va.ATTR_ID=553
            ) is null
            AND CCTI_CLASS=@CCTI_CLASS
            --AND closed_by_group_name IN ('@group')
            AND datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            AND person1_root_org_name = @kehu
            AND TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
        GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
        ) AS t11
    ) AS A
UNION ALL
SELECT
/*Onsite>1 30天内创建的，统计有第一次和第二次上门时间的工单数量(上门大于一次)(不统计删除工单) */
    '0',
    CAST(MAX(D1) + MAX(D2) + MAX(D3) + MAX(D4) + MAX(D5) + MAX(D6) + MAX(D7) + MAX(D8) + MAX(D9) + MAX(D10) +
    MAX(D11) + MAX(D12) + MAX(D13) + MAX(D14) + MAX(D15) + MAX(D16) + MAX(D17) + MAX(D18) + MAX(D19) + MAX(D20) +
    MAX(D21) + MAX(D22) + MAX(D23) + MAX(D24) + MAX(D25) + MAX(D26) + MAX(D27) + MAX(D28) + MAX(D29) + MAX(D30) as varchar),
    'Onsite>1',
    CAST(MAX(D1) as varchar),CAST(MAX(D2) as varchar),CAST(MAX(D3) as varchar),CAST(MAX(D4) as varchar),CAST(MAX(D5) as varchar),
    CAST(MAX(D6) as varchar),CAST(MAX(D7) as varchar),CAST(MAX(D8) as varchar),CAST(MAX(D9) as varchar),CAST(MAX(D10) as varchar),
    CAST(MAX(D11) as varchar),CAST(MAX(D12) as varchar),CAST(MAX(D13) as varchar),CAST(MAX(D14) as varchar),CAST(MAX(D15) as varchar),
    CAST(MAX(D16) as varchar),CAST(MAX(D17) as varchar),CAST(MAX(D18) as varchar),CAST(MAX(D19) as varchar),CAST(MAX(D20) as varchar),
    CAST(MAX(D21) as varchar),CAST(MAX(D22) as varchar),CAST(MAX(D23) as varchar),CAST(MAX(D24) as varchar),CAST(MAX(D25) as varchar),
    CAST(MAX(D26) as varchar),CAST(MAX(D27) as varchar),CAST(MAX(D28) as varchar),CAST(MAX(D29) as varchar),CAST(MAX(D30) as varchar)
FROM
    (
    SELECT
        t12.c AS Onsite_1,
        case when datediff(dd, t12.cr_date, getdate()) =1 then t12.c else '' end as D1,
        case when datediff(dd, t12.cr_date, getdate()) =2 then t12.c else '' end as D2,
        case when datediff(dd, t12.cr_date, getdate()) =3 then t12.c else '' end as D3,
        case when datediff(dd, t12.cr_date, getdate()) =4 then t12.c else '' end as D4,
        case when datediff(dd, t12.cr_date, getdate()) =5 then t12.c else '' end as D5,
        case when datediff(dd, t12.cr_date, getdate()) =6 then t12.c else '' end as D6,
        case when datediff(dd, t12.cr_date, getdate()) =7 then t12.c else '' end as D7,
        case when datediff(dd, t12.cr_date, getdate()) =8 then t12.c else '' end as D8,
        case when datediff(dd, t12.cr_date, getdate()) =9 then t12.c else '' end as D9,
        case when datediff(dd, t12.cr_date, getdate()) =10 then t12.c else '' end as D10,
        case when datediff(dd, t12.cr_date, getdate()) =11 then t12.c else '' end as D11,
        case when datediff(dd, t12.cr_date, getdate()) =12 then t12.c else '' end as D12,
        case when datediff(dd, t12.cr_date, getdate()) =13 then t12.c else '' end as D13,
        case when datediff(dd, t12.cr_date, getdate()) =14 then t12.c else '' end as D14,
        case when datediff(dd, t12.cr_date, getdate()) =15 then t12.c else '' end as D15,
        case when datediff(dd, t12.cr_date, getdate()) =16 then t12.c else '' end as D16,
        case when datediff(dd, t12.cr_date, getdate()) =17 then t12.c else '' end as D17,
        case when datediff(dd, t12.cr_date, getdate()) =18 then t12.c else '' end as D18,
        case when datediff(dd, t12.cr_date, getdate()) =19 then t12.c else '' end as D19,
        case when datediff(dd, t12.cr_date, getdate()) =20 then t12.c else '' end as D20,
        case when datediff(dd, t12.cr_date, getdate()) =21 then t12.c else '' end as D21,
        case when datediff(dd, t12.cr_date, getdate()) =22 then t12.c else '' end as D22,
        case when datediff(dd, t12.cr_date, getdate()) =23 then t12.c else '' end as D23,
        case when datediff(dd, t12.cr_date, getdate()) =24 then t12.c else '' end as D24,
        case when datediff(dd, t12.cr_date, getdate()) =25 then t12.c else '' end as D25,
        case when datediff(dd, t12.cr_date, getdate()) =26 then t12.c else '' end as D26,
        case when datediff(dd, t12.cr_date, getdate()) =27 then t12.c else '' end as D27,
        case when datediff(dd, t12.cr_date, getdate()) =28 then t12.c else '' end as D28,
        case when datediff(dd, t12.cr_date, getdate()) =29 then t12.c else '' end as D29,
        case when datediff(dd, t12.cr_date, getdate()) =30 then t12.c else '' end as D30
    FROM (
        SELECT
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120) cr_date,
            COUNT(TICKET_ID) c
        FROM
            VAPP_ITEM AS vi
        WHERE
            (
            SELECT
                TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
            FROM
                VAPP_ITEM_ATTRIBUTES AS va
            WHERE
                va.ITEM_ID=row_id
                AND va.ATTR_ID=555
            ) is not null
            AND (
                SELECT
                    TOP 1 DATEADD(SECOND, CONVERT(INT, ATTR_VALUE), '1970/1/1 08:00:00')
                FROM
                    VAPP_ITEM_ATTRIBUTES AS va
                WHERE
                    va.ITEM_ID=row_id
                    AND va.ATTR_ID=558
                ) is not null
            AND datediff(dd,CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120),GETDATE())<= @tianshu
            AND person1_root_org_name = @kehu
            AND TICKET_STATUS NOT IN ('Request - Delete','Approved','Submitted')
        GROUP BY
            CONVERT(VARCHAR(10),(DATEADD(S,CREATED_DATE,'1970/1/1 08:00:00')),120)
        ) AS t12
    ) AS A
'''