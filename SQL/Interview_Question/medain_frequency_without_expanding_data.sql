 
 Input:
val freq
10	2
20	1
30	3
40	1
35	2
32	0

out:
30
 
 
 with cte as (
 select *, sum(freq) over() as total_freq, 
 sum(freq) over(order by val rows between unbounded preceding and current row) as cumm_sum, 
 1 as position
 from lower_backup.median
 ), cte2 as (
 select *, 
 case when freq > 0 then coalesce((lag(cumm_sum) over(order by val))+position, 1) else 
 lag(cumm_sum) over(order by val) 
 end as start_position, 
 cumm_sum as end_position, 
 (total_freq + 1)/2 as m, (total_freq+2)/2 as n
 from cte)
 select avg(val) from cte2 where m between start_position and end_position 
 or  (n between start_position  and end_position) ;


 Note in this kind of problem even and odd position doesn't matter both will return correct.
 Only this kind of problems.