select (
select id from lower_backup.employees
limit 7 offset 7) as id;


select * from(
select generate_series(1, 20) as id)
limit 5, 5;

select * from(
select generate_series(1, 20) as id)
offset 10 limit 5;

with recursive cte as (
select id, name, managerid from lower_backup.employees where managerid is null
union all 
select  e.id, c.name, e.managerid  from cte c join lower_backup.employees e on c.id = e.managerid
) select * from cte;




select concat('2020', '01', '01')::date;
select make_date('2020', '01', '01') as begin_date;

select *, 
sum(amount) over(order by sales_date rows between unbounded preceding and current row) as sum_avg
from lower_backup.sales;



select *, 
sum(amount) over(order by sales_date rows between current row and unbounded following) as sum_avg
from lower_backup.sales;


select *, 
sum(amount) over(order by sales_date rows between current row and 1 following) as sum_avg
from lower_backup.sales;


select *, 
sum(amount) over(order by sales_date rows between  current row and 2 preceding) as sum_avg
from lower_backup.sales;


select * from lower_backup.cumulative_sum_reset;

with cte as (
select created_at, to_char(created_at, 'YYYYMM') as yearMonth, count(*) as user_count from lower_backup.cumulative_sum_reset
group by 1)  select * from cte order by created_at;
select created_at, yearmonth, 
sum(user_count) over(partition by yearmonth order by created_at rows between unbounded preceding and current row) as cum_sum
from cte order by created_at;



select date_part('year', current_date);




select  id, (id::numeric/2) as flr, floor(id::numeric/2), 
ceil(id::numeric/2)
from lower_backup.employees where id = 121

select * from lower_backup.employees;

(cnt + 1)/2 or (cnt + 2)/2.

with cte as (
select *, 
count(*) over() as cnt,
row_number() over(order by id) as rnum from lower_backup.employees )
select avg(salary) from cte where 
case when cnt %2 != 0 then rnum in (((cnt::numeric+1)/2), ((cnt::numeric+2)/2))  --   if total count is odd
else rnum in (floor((cnt::numeric+1)/2), (ceil(cnt::numeric+2)/2)) end;		-- if total count is even




select key as key_id from(
select A.key, A.str_forward, B.str_backward, 
case when str_forward = str_backward then 'Y' else 'N' end as flag
from(
select string_agg(value, '') as str_forward, key from lower_backup.palindrome
group by key) A join (
select string_agg(value, '') as str_backward, key as bk_key from(
select * from lower_backup.palindrome
order by key, seq desc)sb1 
group by key) B on A.key = B.bk_key)
where flag = 'Y';



select * from lower_backup.reset_cummulative;

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



WITH ordered AS (
  SELECT
    user_id,
    create_date::date AS dt,
    amount,
    LAG(create_date::date) OVER (PARTITION BY user_id ORDER BY create_date::date) AS prev_dt
  FROM lower_backup.reset_cummulative
)
select * from ordered;
,
flagged AS (
  SELECT
    user_id,
    dt,
    amount,
    prev_dt,
    CASE
      WHEN prev_dt IS NULL OR (dt - prev_dt) >= 3 THEN 1
      ELSE 0
    END AS is_reset
  FROM ordered
), 
streaked AS (
  SELECT
    user_id,
    dt,
    amount,
    prev_dt,
    is_reset,
    SUM(is_reset) OVER (PARTITION BY user_id ORDER BY dt rows between UNBOUNDED preceding and current row) AS streak_id
  FROM flagged
)
select * from streaked;



select * from  lower_backup.logged_user;

with users_logins as (
select user_id as logged_user_id, count(*) from lower_backup.logged_user
where extract('year' from login_time) = '2025'
group by 1 having count(*)>=2)
select ul.logged_user_id,  --lag(login_time::date) over(partition by ) 
(max(login_time::date) - min(login_time::date)) as days_between
from users_logins ul join lower_backup.logged_user u
on ul.logged_user_id = u.user_id
group by 1 order by logged_user_id



with users_logins as (
select user_id as logged_user_id, count(*) from logged_user
where extract('year' from login_time) = '2025'
group by 1 having count(*)>=2)
select ul.logged_user_id,  --lag(login_time::date) over(partition by ) 
(max(login_time::date) - min(login_time::date)) as days_between
from users_logins ul join logged_user u
on ul.logged_user_id = u.user_id
group by 1 order by logged_user_id;



select * from lower_backup.transactions_new;

with cte as (
select customer_id, dte_month, count(*) from(
select distinct customer_id, product_category, to_char(transaction_date, 'yyyymm') as dte_month from lower_backup.transactions_new)
group by 1, 2 having count(*)>=3)
select 
t.customer_id, concat(to_char(t.transaction_date, 'yyyy-mm'), '-01')  as transaction, sum(revenue) as revenue
from cte c join lower_backup.transactions_new t on 
c.customer_id = t.customer_id and 
c.dte_month =  to_char(t.transaction_date, 'yyyymm') 
group by 1,2 order by t.customer_id




with cte as (
select customer_id, dte_month, count(*) from(
select distinct customer_id, product_category, to_char(transaction_date, 'yyyymm') as dte_month from transactions_new)
group by 1, 2 having count(*)>=3)
select 
t.customer_id, concat(to_char(t.transaction_date, 'yyyy-mm'), '-01')  as transaction, sum(revenue) as revenue
from cte c join transactions_new t on 
c.customer_id = t.customer_id and 
c.dte_month =  to_char(t.transaction_date, 'yyyymm') 
group by 1,2 order by t.customer_id;



select key as key_id from(
select A.key, A.str_forward, B.str_backward, 
case when str_forward = str_backward then 'Y' else 'N' end as flag
from(
select string_agg(value, '') as str_forward, key from palindrome
group by key) A join (
select string_agg(value, '') as str_backward, key as bk_key from(
select * from palindrome
order by key, seq desc)sb1 
group by key) B on A.key = B.bk_key)
where flag = 'Y';


select * from lower_backup.call_log;

select * from lower_backup.call_log c1 join 
lower_backup.call_log c2 on 
c1.from_id =c2.to_id and c1.to_id = c2.from_id;


select substring(pair, 1, position('-' in pair)-1) as person1,
substring(pair, position('-' in pair)+1) as person2 
, total_duration
from(
select  
concat(least(from_id, to_id) , '-', greatest(from_id, to_id)) as pair, 
sum(duration) as total_duration
from lower_backup.call_log
group by 1) order by pair;
