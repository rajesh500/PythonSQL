-- Write your PostgreSQL query statement below

with recursive cte as (
select *,  1 as level from Employees  where manager_id is null
union all  
select e.*,  level + 1 from cte c join  Employees e on  c.employee_id = e.manager_id
) ,  cte2 as 
(select employee_id, employee_id as emp_hier_id, salary from cte
union all 
select c2.employee_id, c.employee_id, c.salary from cte2 c2 join cte c on  c2.emp_hier_id = c.manager_id
) , 
cte3 as 
(select employee_id, (count(*)-1) as team_size, sum(salary) as budget from cte2  group by 1 order by employee_id)
, cte4 as (
select c.employee_id, c.employee_name, c.level, c3.team_size, c3.budget
from cte3 c3 join cte c on c3.employee_id = c.employee_id)
select * from cte4 order by level, budget desc, employee_name 


input:
| employee_id | employee_name | manager_id | salary | department  |
| ----------- | ------------- | ---------- | ------ | ----------- |
| 1           | Alice         | null       | 12000  | Executive   |
| 2           | Bob           | 1          | 10000  | Sales       |
| 3           | Charlie       | 1          | 10000  | Engineering |
| 4           | David         | 2          | 7500   | Sales       |
| 5           | Eva           | 2          | 7500   | Sales       |
| 6           | Frank         | 3          | 9000   | Engineering |
| 7           | Grace         | 3          | 8500   | Engineering |
| 8           | Hank          | 4          | 6000   | Sales       |
| 9           | Ivy           | 6          | 7000   | Engineering |
| 10          | Judy          | 6          | 7000   | Engineering |


output:
| employee_id | employee_name | level | team_size | budget |
| ----------- | ------------- | ----- | --------- | ------ |
| 1           | Alice         | 1     | 9         | 84500  |
| 3           | Charlie       | 2     | 4         | 41500  |
| 2           | Bob           | 2     | 3         | 31000  |
| 6           | Frank         | 3     | 2         | 23000  |
| 4           | David         | 3     | 1         | 13500  |
| 7           | Grace         | 3     | 0         | 8500   |
| 5           | Eva           | 3     | 0         | 7500   |
| 9           | Ivy           | 4     | 0         | 7000   |
| 10          | Judy          | 4     | 0         | 7000   |
| 8           | Hank          | 4     | 0         | 6000   |