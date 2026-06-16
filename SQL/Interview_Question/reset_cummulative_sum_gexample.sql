data:
user_id create_date amount
1	    2024-01-01	100
1	    2024-01-02	200
1	    2024-01-05	50
1	    2024-01-06	100


out:
user_id create_date     amount reset_amount
1	    2024-01-01	    100	    100
1	    2024-01-02	    200	    300
1	    2024-01-05	    50	    50
1	    2024-01-06	    100	    150


query:
complexity in the query is how group first two records and last two records.
First pull down the  create_date then find the difference between dates.
First record previos_date is null and third record as diff_days as 3 which means we can assign 1 
and sum it using rows between unbounded preceding and current row 
it will add 1, 1+0 = 1, 1+0+1 = 2, 1+0+1+0 = 2.
Now first two records has 1 and last two records 2.

with cte as (
select *, 
lag(create_date) over(order by create_date) as previous_date
from lower_backup.reset_cummulative), cte2 as (
select *, (create_date - previous_date) as diff_days
from cte), cte3 as (
select *, 
case when previous_date is null or diff_days >= 3 then 1 else 0 end as reset_id
from cte2), 
cte4 as (
select *, sum(reset_id) over(partition by user_id order by create_date rows between unbounded preceding and current row) as reset_group
from cte3)
select *,
sum(amount) over(partition by user_id, reset_group order by create_date rows between unbounded preceding and current row) as reset_amount
from cte4;