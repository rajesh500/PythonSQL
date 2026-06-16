---- median problem solving for even count and odd. This approach has to follow.
with cte as (
select *, 
count(*) over() as cnt,
row_number() over(order by id) as rnum from lower_backup.employees )
select avg(salary) from cte where 
case when cnt %2 != 0 then rnum in (((cnt::numeric+1)/2), ((cnt::numeric+2)/2))  --   if total count is odd
else rnum in (floor((cnt::numeric+1)/2), (ceil(cnt::numeric+2)/2)) end;		-- if total count is even
