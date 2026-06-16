
--- Source Data:
orderid	item	qty
O1	A1	5
O2	A2	1
O3	A3	3

---output data:
orderid	item qty
O1	A1	1	
O1	A1	1	
O1	A1	1	
O1	A1	1	
O1	A1	1	
O2	A2	1	
O3	A3	1	
O3	A3	1	
O3	A3	1	




with  recursive cte as (
select orderid, item, 1 as cond_fail, qty from lower_backup.recursive_exp -- where  orderid = 'O1'
union all 
select orderid, item, cond_fail, qty-1 from cte 
where cond_fail < qty
)select orderid, item, cond_fail, qty from cte order by orderid;
----- using qty and failing the condition is possible, picking another field and failing the condition.


select generate_series(1, qty) as id, orderid as idm, item, 1 as qty from lower_backup.recursive_exp
--- using generate_series could be very easy.