
Input: 
Tasks table:
+---------+----------------+
| task_id | subtasks_count |
+---------+----------------+
| 1       | 3              |
| 2       | 2              |
| 3       | 4              |
+---------+----------------+
Executed table:
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 2          |
| 3       | 1          |
| 3       | 2          |
| 3       | 3          |
| 3       | 4          |
+---------+------------+
Output: 
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 1          |
| 1       | 3          |
| 2       | 1          |
| 2       | 2          |
+---------+------------+


with cte as (
select task_id, max(subtasks_count) as subtask_max_id from Tasks
group by 1), cte2 as (
select task_id, generate_series(1, subtask_max_id) as subtask_id from cte)
select task_id, subtask_id from(
select  c2.*, e.task_id as e_task_id, e.subtask_id as e_subtask_id from cte2 c2 left join Executed e on 
c2.task_id = e.task_id and c2.subtask_id = e.subtask_id)
where (e_task_id is null and e_subtask_id is null)

with cte as (
select task_id, max(subtasks_count) as subtask_max_id from Tasks
group by 1), cte2 as (
select task_id, generate_series(1, subtask_max_id) as subtask_id from cte)
select * from cte2 
where (task_id, subtask_id) not in 
(select task_id, subtask_id from Executed)
order by task_id, subtask_id


with recursive cte as (
    select 1 as user_id
    union all 
    select user_id+1 from cte 
    where user_id < (select max(task_id) from Tasks)
    ), 
    cte2 as (
    select user_id, 1 as subtask_id from cte
    union all 
    select user_id, subtask_id + 1 from cte2 c2 join 
    Tasks t on c2.user_id = t.task_id and 
    c2.subtask_id < t.subtasks_count
    )
    select user_id as task_id, subtask_id from cte2 
    where (user_id, subtask_id) not in 
    (select task_id, subtask_id  from Executed )
    order by user_id, subtask_id