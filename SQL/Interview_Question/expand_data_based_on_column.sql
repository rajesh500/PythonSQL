Input:
searches    num_users
1           2
2           2
3           3
4           1

WITH RECURSIVE CTE AS (select searches, num_users, 1 as level from TABLES
union all 
select searches, num_users, level + 1 from cte 
where level < num_users
)select * from cte;

1     2     1
1     2     2
2     2     1
2     2     2
3     3     1
3     3     2
3     3     3
4     1     1