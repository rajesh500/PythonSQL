Input data:
 order_id	cust_id	order_dt	order_amt
    1	        C1	2025-01-01	200
    2	        C1	2025-01-01	150
    3	        C2	2025-01-01	300
    4	        C3	2025-01-02	250
    5	        C1	2025-01-02	100
    6	        C1	2025-01-03	180
    7	        C2	2025-01-03	220

Find the repeat and new customers

out data:
order_dt	new_cust	repeat_cust
2025-01-01  	2	        0
2025-01-02	    1       	1
2025-01-03	    0	        2


query:
with cte as (
select cust_id, min(order_dt) as cust_min_order_dt from lower_backup.repeat_customer
group by 1), 
cte3 as (
select  u.order_id, u.cust_id, u.order_dt, c.cust_min_order_dt
from lower_backup.repeat_customer u join cte c on 
u.Cust_id = c.cust_id)
select
order_dt, sum(case when order_dt = cust_min_order_dt then 1 else 0 end) as new_cust, 
sum(case when order_dt > cust_min_order_dt then 1 else 0 end) as repeat_cust
 from(
select distinct cust_id, order_dt, cust_min_order_dt
from cte3) group by 1 order by order_dt;



Explain:
Find the every customer min date, is the first time visit to the store.
Then join with main table one column as original date and another column as min date.
If the original date = min date then 1      first date = min date 
if original date > min date then 1          If he visited again other than min date which mean repeat customer.
sum the counts.

note: if duplicate date is their use the distinct.

