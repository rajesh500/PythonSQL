concurent task means A concurrent task is a piece of work that can run overlapping in time with other work, 
rather than waiting for the other work to fully finish first.

Example: task1 is start at 1:00 clock and going to complete at 3:00 clock.
Now task2 is start at 1:20 before the task1 is completed. task2 is going to end at 2:00 clock
task3 is start at 2:30 and end at 3:30, task3 is started before task1 and task2.
task4 is start at 3:00 clock ends at 4:00 clock.
task5 starts at 4:00 clock and ends at 5:00 clock.

Now, task1, task2, task3 are concurrent because 1 clock to 3 clock windows 
three tasks are running these are max concurrent task for that window.

task3 and task4 are one window, here two max concurrent tasks.


concurrent task calculate:
WITH jobs(job_id, started_at, ended_at) AS (
  VALUES
    (1, CAST('2026-03-31 10:00:00' AS TIMESTAMP), CAST('2026-03-31 10:30:00' AS TIMESTAMP)),
    (2, CAST('2026-03-31 10:10:00' AS TIMESTAMP), CAST('2026-03-31 10:40:00' AS TIMESTAMP)),
    (3, CAST('2026-03-31 10:20:00' AS TIMESTAMP), CAST('2026-03-31 10:25:00' AS TIMESTAMP)),
    (4, CAST('2026-03-31 10:50:00' AS TIMESTAMP), CAST('2026-03-31 11:10:00' AS TIMESTAMP))
),
events AS (
  SELECT started_at AS t, +1 AS delta FROM jobs
  UNION ALL
  SELECT ended_at   AS t, -1 AS delta FROM jobs
) ,
scan AS (
  SELECT
    t,
    SUM(delta) OVER (ORDER BY t, delta) AS concurrent_running
  FROM events
)
select  MAX(concurrent_running) AS peak_concurrency  FROM scan;


calculating total hours:
calculate the concurrent tasks and use lead to pull date. (combine the start_time and end_time data)
calcualte the difference between previous and current time stamp in hours.
if concurrent task is 0 those difference time doesnt required.
sum all the diff time 

1) Peak concurrent jobs (overlapping time windows)
Question: Given job intervals, compute the maximum number of jobs running at the same time.


with cte as (
select employee_id, start_time as t, 1 as delta from Tasks 
union all 
select employee_id, end_time as t, -1 as delta from Tasks), 
cte2 as (
select employee_id, t as segment_start_time, sum(delta) over(partition by employee_id order by t, delta) as concur, 
lead(t)  over(partition by employee_id order by t) as segment_end_time
from cte)
select employee_id, floor(sum(case when concur > 0 then extract('epoch' from (segment_end_time - segment_start_time))/3600.0
else 0 end)) as total_task_hours , max(concur) as max_concurrent_tasks 
from cte2 group by 1
order by 1




2. Concurrency at each job start
Question: For each job, how many other jobs were already running when it started?

WITH jobs(job_id, started_at, ended_at) AS (
  VALUES
    (1, CAST('2026-03-31 10:00:00' AS TIMESTAMP), CAST('2026-03-31 10:30:00' AS TIMESTAMP)),
    (2, CAST('2026-03-31 10:10:00' AS TIMESTAMP), CAST('2026-03-31 10:40:00' AS TIMESTAMP)),
    (3, CAST('2026-03-31 10:20:00' AS TIMESTAMP), CAST('2026-03-31 10:25:00' AS TIMESTAMP))
), cte2 as (
select *, lag(started_at) over(order by started_at) as previous_run_time, 
lag(job_id) over(order by started_at) as previous_job_id
from jobs)
select *, case when  previous_run_time > started_at then previous_job_id else 0 end as flag
from cte2 where previous_job_id is not null;


3. Find overlapping pairs (duplicate processing / collisions)
Question: Find all pairs of jobs on the same resource whose run windows overlap, and return the overlap interval.

WITH jobs(job_id, resource_id, started_at, ended_at) AS (
  VALUES
    (1, 'R1', CAST('2026-03-31 10:00:00' AS TIMESTAMP), CAST('2026-03-31 10:30:00' AS TIMESTAMP)),
    (2, 'R1', CAST('2026-03-31 10:20:00' AS TIMESTAMP), CAST('2026-03-31 10:40:00' AS TIMESTAMP)),
    (3, 'R2', CAST('2026-03-31 10:10:00' AS TIMESTAMP), CAST('2026-03-31 10:15:00' AS TIMESTAMP))
)
select * /*
  a.resource_id,
  a.job_id AS job_id_1,
  b.job_id AS job_id_2,
  CASE WHEN a.started_at > b.started_at THEN a.started_at ELSE b.started_at END AS overlap_start,
  CASE WHEN a.ended_at   < b.ended_at   THEN a.ended_at   ELSE b.ended_at   END AS overlap_end
*/ FROM jobs a
cross JOIN jobs b
  where a.resource_id = b.resource_id
 AND a.job_id < b.job_id
 AND a.started_at < b.ended_at
 --AND b.started_at < a.ended_at
ORDER BY a.resource_id, a.job_id, b.job_id;