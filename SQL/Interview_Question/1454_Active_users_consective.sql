
Accounts table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Winston  |
| 7  | Jonathan |
+----+----------+
Logins table:
+----+------------+
| id | login_date |
+----+------------+
| 7  | 2020-05-30 |
| 1  | 2020-05-30 |
| 7  | 2020-05-31 |
| 7  | 2020-06-01 |
| 7  | 2020-06-02 |
| 7  | 2020-06-02 |
| 7  | 2020-06-03 |
| 1  | 2020-06-07 |
| 7  | 2020-06-10 |
+----+------------+


Active users are those who logged in to their accounts for five or more consecutive days.

Write a solution to find the id and the name of active users.

Return the result table ordered by id.

The result format is in the following example.



out: 
| id | name     |
| -- | -------- |
| 7  | Jonathan |


solve using cummulative sum:
with cte as (
select distinct id, login_date from Logins order by id, login_date), cte2 as (
select *, case when (login_date - prev_date) = 1 then 0 else 1 end as diff from(
select *, lag(login_date, 1) over(partition by id order by id, login_date) as prev_date from cte)
), cte3 as (
select id, grp, count(*) from(
select *, sum(diff) over(partition by id order by login_date) as grp from cte2)
group by 1, 2 having count(*)>=5)
select distinct c3.id, a.name from cte3 c3 join accounts a on c3.id = a.id
order by c3.id
