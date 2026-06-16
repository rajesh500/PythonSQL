max_parallel_workers
max_parallel_workers_per_gather
max_worker_processes 

max_worker_processes = 20 is moderate in these 20 workers
it includes 
parallel query workers 
logical replication workers 
Extension/background job workers 
other general background tasks. 



How to Answer: Optimization with Execution Plans & Workers in PostgreSQL
1. Start with Execution Plans

Definition:
Explain that an execution plan is PostgreSQL’s internal roadmap for how a query will be processed—what indexes to use, join order, whether to use sequential or parallel scans, and so on.
How to View:
Mention the use of EXPLAIN or EXPLAIN ANALYZE to see the query plan, costs, actual times, and the utilization of workers (if parallelism is chosen).


2. Optimization Steps Based on Execution Plan

Identify Bottlenecks:
Look for steps in the plan with high cost or time. Calls like Seq Scan, Hash Join, or Sort might surface as bottlenecks.
Check for Parallelism:
If you see lines like Gather or Parallel Seq Scan, the query is using parallel workers. Otherwise, it’s running sequentially.


3. Role of Workers (Parallel Execution)

How Workers Help:
Parallel workers split work (e.g., scanning big tables or performing joins) across multiple CPU cores, reducing query runtime for large datasets.
Execution Plan Clues:
Look for Workers Launched in the execution plan. This shows the number of parallel worker processes used for the query.


4. Practical Optimization Actions
a. When the Execution Plan is Not Parallelized:

Increase parallel-friendly configuration parameters:

max_parallel_workers_per_gather
max_parallel_workers


Check table eligibility:
Large tables and non-volatile functions work best with parallel queries.

b. When Parallelism Is Present but Insufficient:

Tune number of workers in the config.
Monitor system resource utilization to make sure increasing workers doesn’t overcommit CPU/RAM.

c. When Parallelism Doesn’t Help or Hurts:

Analyze the plan to see if the overhead of coordination outweighs the benefit. For small queries, parallel execution can actually be slower.
Adjust back down or restrict parallelism for OLTP workloads where simplicity and low latency are more important.


5. Sample Interview-Ready Statement

"When optimizing queries in PostgreSQL, I start by analyzing the execution plan to identify costly steps—using EXPLAIN ANALYZE to see both chosen steps and actual runtimes. For large analytics queries, I look for opportunities to enable or tune parallel execution. If the plan isn’t already parallel, I verify that system and table settings allow it (max_parallel_workers, max_parallel_workers_per_gather) and adjust these upward for bigger servers. When parallel workers are being used, I check that the number is optimal and resources (CPU, RAM) aren’t saturated. These tuning steps, informed by the execution plan, help significantly reduce query times for the right workloads."


6. Extra Points: Show Awareness of Limits and Context

Not all queries benefit from parallelism (e.g., small OLTP queries).
Monitoring and testing are crucial after changes.
Autovacuum and replication workers are also worker-related performance factors for overall database health.


Summary Table: Key Steps in Optimization via Execution Plan & Workers



Step
What to Do
Tool / Setting




Analyze query
Find bottlenecks, see parallel usage
EXPLAIN, EXPLAIN ANALYZE


Enable parallelism
Increase parallel worker settings
max_parallel_workers, max_parallel_workers_per_gather


Assess impact
Monitor performance, adjust based on workload
System monitoring tools