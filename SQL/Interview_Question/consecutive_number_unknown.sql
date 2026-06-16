The goal here is to identify consecutive numbers, but the sequence length isn’t fixed.
In some problems, ask is to find three or more consecutive values. In this case, “consecutive” is unknown in length.
If consecutive number length is fixed ("least three consecutive") then using self-join this can be solved.
self-join approach like id1 + 1 = id2 and id2 + 1 = id3, it will only return sequences of exactly three consecutive numbers. 
If there are more than three in a row, that approach won’t return the full set of values, so it’s not a good option.
A better approach is the one below, which works when the consecutive sequence length is not fixed. 
This is a strong option for all scenarios.


with cte as (
select * from Stadium 
where people >= 100), 
cte2 as (
select *, row_number() over(order by id) as rnum, 
(id - row_number() over(order by id)) as diff_num
from cte), 
cte3 as (
select diff_num, count(*) from cte2
group by 1 having count(*)>2)
select id, visit_date, people from cte2 where diff_num in 
(select diff_num from cte3)
order by visit_date;


Input data:
id | visit_date | people |
| -- | ---------- | ------ |
| 1  | 2017-01-01 | 10     |
| 2  | 2017-01-02 | 109    |
| 3  | 2017-01-03 | 150    |
| 4  | 2017-01-04 | 99     |
| 5  | 2017-01-05 | 145    |
| 6  | 2017-01-06 | 1455


select * from cte2;
| id | visit_date | people | rnum | diff_num |
| -- | ---------- | ------ | ---- | -------- |
| 2  | 2017-01-02 | 109    | 1    | 1        |
| 3  | 2017-01-03 | 150    | 2    | 1        |
| 5  | 2017-01-05 | 145    | 3    | 2        |
| 6  | 2017-01-06 | 1455   | 4    | 2        |
| 7  | 2017-01-07 | 199    | 5    | 2        |
| 8  | 2017-01-09 | 188    | 6    | 2        |


grouping all the diff_num if count(*)>=3 then all those diff_num will be pulled.
then again using inclause to get all the data.


select id, visit_date, people from cte2 where diff_num in 
(select diff_num from cte3)
order by visit_date;