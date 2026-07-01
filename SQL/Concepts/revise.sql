

date_part:
select 
date_part('isodow', createddate), createddate
,* from batchuat.t_sub_pmt_detail
where cast(createddate as date) > '2025-01-01' and idn_detail_pmt_sub  = '104927752';

week  --> date is falling in which week.
doy   --> date is falling in which number from 1 to 365.
dow   --> (day of the week, 0=Sunday to 6=Saturday)
century
decade
year
month
day
hour
minute
second
microseconds
milliseconds
epoch
isodow
isoyear
timezone
timezone_hour
timezone_minute 

** EPOCH time difference in seconds return only between TIMESTAMP fields not on  the date fields.
SELECT EXTRACT(EPOCH FROM NOW());  
In PostgreSQL, "epoch" refers to the Unix epoch, which is the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC
SELECT EXTRACT(EPOCH FROM TIMESTAMP '2023-03-11 17:43:17.436' - '2023-03-10 17:43:17.436');
extract(EPOCH FROM   lastmodifieddate - createddate);


date_difference:
no direct functions use date2 - date1 (direct date fields) return difference in days.
If difference is in seconds and want to convert it into days then 
seconds/86400  -- days
seconds/3600 -- hours (difference in hours)

date_trunc():
select date_trunc('year', createddate)  --> bring year into starting point
ex: 2025-01-01 00:00:00    if date '2025-02-20 20:12:36'

select date_trunc('month', createddate)
ex: 2025-02-01 00:00:00   if date '2025-02-20 20:12:36'

syntax:
date_trunc('year', createddate)   createddate is column no need to define timestamp
if we are defining date then timestamp mandatory.

date_trunc('Year',  timestamp '2025-02-20 20:12:36')
date_trunc('Month',  timestamp '2025-02-20 20:12:36')
date_trunc('day',  timestamp '2025-02-20 20:12:36')


extract:
extract('day' from timestamp '2025-02-20 20:12:36');

SELECT EXTRACT('YEAR' FROM my_date_column) FROM my_table;

select  age('2026-01-01'::date ,'2013-01-01'::date);
out: 13 years

age('2026-02-10'::date ,'2013-01-01'::date);
out: 13 years 1 mon 9 days

SELECT TO_CHAR(DATE '2026-05-26', 'Day'); ---- Returns 'Tuesday  ' (blank-padded)
SELECT TO_CHAR(DATE '2026-05-26', 'dy');  ---- Returns 'tue'

recursive:
With recursive cte_name as (
    select query (non recursive query or base query)
    union / union all
    select query (recursive query using cte_name [with a termination condition])
) select * from cte_name;


queries using recursive concept:
1. sequence generate without using built-in function.
2. hierarchy of employees under a given manager    ---> h.id = emp.managerid
3. hierarchy of managers for a given employee.     ---> h.managerid = emp.id
4. Binary tree   ( tree traversal)


with recursive cte_main as (
select *, 1 as level from lower_backup.Employees where name = 'Bob'
union 
select emp.id,  emp.name, emp.managerid, level + 1 from cte_main c1 
join lower_backup.Employees emp
on c1.id = emp.managerid
)
select * from cte_main;


Cumulative sum:
means adding sum of current and above rows.
id  cum_sum
1    1
2    3
3    6
4    10

select *, 
sum(amount) over(partition by region order by sales_date)
from lower_backup.sales;


Lets say we have 10 rows in a partition only add above two rows from current row then above apporach wont work
we need to use preceding and current row.


select *, 
sum(amount) over(partition by region order by sales_date rows between 2 preceding and current row)
from lower_backup.sales;

preceding means above rows --> current row above rows


1. Running Total  vs Rolling Total:
Running Total:
Aggregate all values from the beginning up to the current point without dropping off older data.

sum(sales) over(order by month rows between unbounded PRECEDING and current row)
unbounded means no limit 
preceding means above rows 

                            Month  sales    SUM
unbounded preceding         Jan     20      20
                            Fev     10      30
                            Mar     30      60
                            Apr     5       65
                            Jun     70      135
                            Jul     40      175

    current row will move from first to last but unbounded preceding will be at first record.


2. Rolling Total:  (rolling sum, moving window, sliding window)
Aggregate all values within a fixed time window (e.g. 30 days)
As new data is added, the oldest data point will be dropped.

sum(sales) over(order by month rows between 2 preceding and current row)
                            month   sales   SUM
2 preceding                 Jan     20      20
                            Fev     10      30
                            Mar     30      60
                            Apr     5       45
                            Jun     70      105
                            Jul     40      105

In both questions first three records sum is same but starting from 4th sum amount start changing.


select *, 
sum(amount) over(order by sales_date rows between 2 preceding and current row) as sum_avg
from lower_backup.sales;

select *, 
sum(amount) over(order by sales_date rows between unbounded preceding and current row) as sum_avg
from lower_backup.sales;

select *, 
sum(amount) over(order by sales_date rows between current row and 1 following) as sum_avg
from lower_backup.sales;

select *, 
sum(amount) over(order by sales_date rows between current row and 2 following) as sum_avg
from lower_backup.sales;

select *, 
sum(amount) over(order by sales_date rows between current row and unbounded following) as sum_avg
from lower_backup.sales;

range between current row and 2 following --> means if any number is missing for the sum it will add 0 the missing number and summit.
7 - 90   - 90  ideally if we yse row between it will sum 90+60+40 which is wrong for this scenario
4 - 60   - 130
3 - 40   - 70
2 - 30   - 30 

val   freq  2pcr    upcr   2FCR     UFCR
10	    2	 2       2      6       9
20	    1	 3       3      4       8
30	    3	 6       6      5       6
32	    0	 4       6      3       6
35	    2	 5       8      3       3
40	    1	 3       9      1       2


overall Total
total per GROUP
running total 
rolling total


3. Moving Average:
sales   MovingAvg
10      10  
20      15
90      40
20      35

avg(sales) over(partition by productid order by order_date) as movingAvg


cumulative sum can be done using self join and correlated sub query.
but these two are slow using window function is very faster.


4. Resetting Cumulative Sum on Condition:
resetting means if it is monthly then cumulative sum should happen with in that month 
and following again should start.   (resetting monthly, yearly or daily)

with cte as (
select created_at, to_char(created_at, 'YYYYMM') as yearMonth, count(*) as user_count from lower_backup.cumulative_sum_reset
group by 1)
select created_at, yearmonth, 
sum(user_count) over(partition by yearmonth order by created_at rows between unbounded preceding and current row) as cum_sum
from cte;


5. cumulative sum total:
6. cumulative sum with in the group:
7. reverse cumulative sum --> cumulative sum displayed 

to_char();

to_char(value, format_mask)
to_char(sales_date, 'yyyymmdd') as sales_dt
to_char(sales_date, 'yyyy-mm-dd') as sales_dt
to_char(sales_date, 'yyyy/mm/dd') as sales_dt
to_char(sales_date, 'dd/mm/yyyy')


to_date();
to_date(sales_dt, 'YYYYMMDD')   --> sales_dt = 20250101

percentage:
(COUNT(*) * 100.0) / SUM(COUNT(*)) OVER() AS percentage_of_total

previous row compare or previous day/month/year.
(94-84/84) * 100 



string_agg():
string(column, 'separator')
combine (concatenate) the values from multiple rows into a single string, often with a separator of your choice

#out CW, LI, TF, FT 

department wise combine data into single string....
SELECT
department,
string_agg(employee_name, '; ') AS names_in_department
FROM employees
GROUP BY department;


Normalization vs denormalization:
Normalization is the process of organizing data to reduce redundancy and dependency by spliting data into multiple related tables.
The goal is to make the database more efficient and avoid data duplicate
Reduced data redundancy: No repeated data means better storage efficiency.
Easier to maintain: it's easier to update, delete or insert data because each entity ( eg customer, order) is represented by one record.

Denormalization:
Denormalization is the process of combining tables or adding redundant data to the database to improve performance for certain read0heavy operations.
If increases data redundancy but reduce the number of joins needed when querying which can make queries faster,
when performance (speed) is more important than data storage efficiency
when the system has a read-heavy workload (eg frequent queries but fever updates).


Use case: 
use normalization: 
you are working with transactional systems (eg banking, ecommerce, inventory, management).
data integrity and consistency are the most important priorities.
storage efficiency and data updates are frequent. 
 
use Denormalization: 
you need to optimize query performance in systems where reading data is more frequent than writing it. 
(eg in data warehouses, reporting systems or analytics applications). 
storage is less of a concern and the goal is to speed up queries at the expense of increased redundancy.



example:
Pictures\nor-denor.png




self join:
A self-join in PostgreSQL is a regular JOIN (e.g., INNER JOIN, LEFT JOIN) where a table is joined to itself. 
This technique is used to compare rows within the same table or to query hierarchical data. 
Use: in Hierarchical data (manager - employee).
comparing rows

Hierarchical data:
SELECT e.Name AS EmployeeName, m.Name AS ManagerName
FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID

Comparing rows:
SELECT A.CustomerName AS Customer1, B.CustomerName AS Customer2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID AND A.City = B.City;


first_value:  with in the group it will return first value
first_value(amount) over(partition by region order by id) as fv


last_value: with out PRECEDING and following will not return exact result.
Expectation on this with in the group get the last value. using below syntax only we will get it.
last_value(amount) over(partition by region order by id rows BETWEEN
            UNBOUNDED PRECEDING AND
            UNBOUNDED FOLLOWING) as lv



Median:
If given data set as even numbers then middle two number average is Median
If given data set as odd numbers then middle number is medain.

first define row_number and get total count
((cnt + 1)/2 or (cnt + 2)/2).    -- works fine odd number but count is even number then one number will to handle that.

case when cnt %2 != 0 then rnum in (((cnt::numeric+1)/2), ((cnt::numeric+2)/2))  --   if total count is odd
else rnum in (floor((cnt::numeric+1)/2), (ceil(cnt::numeric+2)/2)) end     -- if total count is even
Both records will be pulled in even.
floor to lowest value and ceil to heighst value. 

If datatype is int or numeric




query:
with cte as (
select *, 
count(*) over() as cnt,
row_number() over(order by id) as rnum from lower_backup.employees )
select avg(salary) from cte where 
case when cnt %2 != 0 then rnum in (((cnt::numeric+1)/2), ((cnt::numeric+2)/2))  --   if total count is odd
else rnum in (floor((cnt::numeric+1)/2), (ceil(cnt::numeric+2)/2)) end;		-- if total count is even

floor() --> round to low value  ex: 200.5 --> 200
ceil()  --> if any decimal value then round to high value  200.5 --> 201


least and greatest:
least and greatest operate at row level and it will compare multiple value with in the row from different columns and return 
least and greatest values.
Ex:
least(createddate, lastmodifieddate) as least_value, 
greatest(createddate, lastmodifieddate) as great_value

Min and Max are different from least and greatest. Min and Max operations done overall at column level and 
return the max and min values but least and greatest are at row level.



case sensitive: ABC = ABC  
abc = ABC return false 

case insensitive abc = ABC return true.

String Char check:
Check any specific exist in the string or not
product_name ~ '^[A-Za-z]'   or ~'^[A-Z]';   ----- case sensitive

product_name ~*'^[A-Za-z]'   or ~'^[A-Z]';  ---- case insensitive (for case insensitive *) 


^ → Start of the string
[a-zA-Z]+ → Starts with at least one letter
[a-zA-Z0-9_/.-]* → Followed by any number of letters, digits, _ , . , or -
@leetcode.com → Must end with @leetcode.com ( escaped . )

mail ~ '^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'
^ and $ anchor the pattern to the start and end of the string
^  is caret  ---> typing in coding using shortcut as shift+6


select  content_id, content_text as original_text, initcap(content_text) as converted_text
from user_content where content_text  !~ '[,\^/@]'
union all
select  content_id, content_text as original_text, content_text as converted_text
from user_content where content_text  ~ '[,\^/@]'


# convert every word first letter to capital 
initcap('the QUICK-brown fox  ')
The Quick-Brown Fox  


numeric:
::numberic --> default convert int into decimal 5 as 5.00




In PostgreSQL, the "type" of execution plan generally refers to the estimated versus actual plan, 
or the specific nodes (operations) that make up the plan tree. The database planner automatically 
selects the most efficient plan based on available statistics. 

Types of Plans (by execution method)
PostgreSQL generates two main forms of a query plan using the EXPLAIN command: 
Estimated Execution Plan: Generated using EXPLAIN <query>. This plan shows how the database engine intends to execute the query, 
based on cost estimations and database statistics, without actually running it. 
It is useful for a quick analysis of potential issues without affecting data or performance for complex queries.

Actual Execution Plan: Generated using EXPLAIN ANALYZE <query>. This command runs the query and outputs the actual runtime statistics,
 including the time spent and rows returned by each node. This is essential for troubleshooting performance issues 
 and verifying if the planner's estimates match reality. 

Types of Plan Nodes (Operations)
An execution plan is a tree structure composed of various nodes, each representing a specific operation. 
These nodes can be broadly categorized into three classes: 
Scan Nodes
These nodes retrieve data directly from tables. 
Sequential Scan (Seq Scan): Reads the entire table, row by row, and checks each row against the query's conditions.
Index Scan: Uses an index to find the locations of specific rows that match a condition, 
then fetches the full row data from the table.

Index Only Scan: Similar to an index scan, but all required columns are available in the index itself, 
avoiding the need to fetch the actual table row (if the visibility information permits).

Bitmap Scan (Bitmap Index/Heap Scan): Uses an index to efficiently create a bitmap of matching row locations 
and then accesses those rows from the table in physical order to minimize I/O costs.

Parallel Scan: Modern PostgreSQL can perform certain scans, like sequential or index scans, in parallel across multiple workers. 

Join Nodes
These nodes combine rows from two or more child nodes using specific algorithms. 
Nested Loop Join: For every row in the outer table (or result set), it scans all matching rows in the inner table.

Hash Join: Creates a hash table of the inner table's rows and then probes it with values from the outer table to find matches.

Merge Join: Sorts both input sets of data and then merges them to find matching rows. 

Auxiliary Nodes
These nodes perform operations like aggregation, sorting, or filtering. 
Sort / Quick Sort / External Sort: Sorts the data based on ORDER BY or other clauses.
Aggregate / HashAggregate: Used for queries involving GROUP BY or aggregate functions (like SUM, COUNT).
Filter: Applies a WHERE condition to rows as they pass through the plan. 


Clustured Index vs Non-Clustered Index:
Clustered Index:
default index created on primary key, no need to create it explicitly.




Limit, OFFSET:
top n rows using LIMIT
top n rows skip using offset.

Example: If want to display records from the table 10 to 15 only five records. 
skip before and 10 and after 15 then using limit and offset we will do it.

limit 5 offset 10

Both queries are same:
select * from(
select generate_series(1, 20) as id)
limit 5 offset 10;

select * from(
select generate_series(1, 20) as id)
offset 10 limit 5;


Example: 
query return second salary, if record doesn't exist then no value return including null
select distinct salary   from Employee
order by salary desc
offset 1 limit 1

this query seams to be same but it will return null value if record doesn't EXIST because of 
entire result set is pulled as a column, if value exist it will return that if not null will be returned.
select (select distinct(salary) from Employee order by salary DESC offset 1 limit 1 ) as SecondHighestSalary

make_date('2020', '01', '01') as begin_date;
concat('2020', '01', '01')::date;


Three line segment triangle:
a + b > c
a + c > b
b + c > a  all the condition is satisfied then Yes else No.


analyze in postgres:
will analyze the STATISTICS on the table, these STATISTICS helps query planner to plan the query execution in bettern way.
which lead to faster query.



ACID in dataware house:
Atomicity:     complete entire transaction, if any failure occur revert entire transaction.
Consistency:   follow rules like, constraint, rules etcc .... (account balance can't be negative is a rule).
Isolcation:    concurrent transaction run one after another. (sequentically)
Durability:    once transaction is committed, changes saved permanently.


Data integrity:
Data integrity is the assurance that data remains accurate, consistent, complete, and reliable throughout its entire lifecycle, 
from creation to deletion, by preventing unauthorized changes, corruption, or loss, ensuring it's trustworthy for business decisions, 
operations, and compliance.

How to achieve data integrity:
Entity Integrity: each identify has unique value (primary key).
Referential Integrity: foreign key relationship between the tables.
Domain Integrity: maintain proper data types to the fields.
user-defined integrity: if above is not possible define a trigger or store proceducre like 
insert, update and deletes in the tables.

Keys: Accuracy, Completeness, Consistency, Reliability, Validity and Uniqueness.
How to implemenet it:
proper data TYPES
Constraints (default, check, unique and key)
Data validation process.


Data governance:
Data profiling:

Data quality checks:
Common Data Quality Checks in Pipelines:
Schema & Type Checks: Validating data types (string, int, date) and structure match expected formats, preventing errors from mismatched data.
Null/Missing Values: Ensuring critical fields aren't empty, as missing data breaks processes or skews analysis.
Uniqueness: Checking for duplicate primary keys or identifiers to maintain data integrity.
Referential Integrity: Verifying relationships between tables (e.g., foreign keys) remain intact.
Business Rule Validation: Enforcing specific rules, like age > 18 or percentages summing to 100%.
Range & Pattern Checks: Confirming data falls within expected values (e.g., 0-100) or matches patterns (email, phone).
Volume & Freshness: Monitoring record counts (too few/many) and ensuring data arrives on time.
Distribution & Outlier: Analyzing statistical properties (mean, median) to spot abnormal data points.
Consistency Checks: Cross-column or cross-table validation for logical agreement. 
Data Auditing and Logging


Transaction DB example:


Type of keys:
primary, foriegn, surrogate, natural, composite, unique, candidate and super.

A primary key in PostgreSQL can be both user-defined and system-generated.

surrogate key: is a system generated unique identifier for a row that has no business meaning or relation to the data itself.
Ex: auto incremented, UUID
these fields are designated as the primary key of a table.

* A table can have a surrogate key column and make it the primary key

Natural key: SSN, email, phone number.

composite key: is a primary key that uses a combination of two or more columns to uniquely identify each row in a table.

candidate key: ?

super key: ?

CRUD: 


Like:
conditions like 'DIAB1%' or  conditions like '% DIAB1%';


cross-join:
In cross join we don't have any joining conditions.
we just map one record from table1 to all records in table2

select * from table1 m1 cross join table2 m2;
table1 has two records and table2 has three records.
Data mapping like below:
1	John	3000.0	1	Iphone12	1100.0
1	John	3000.0	2	Iphone13	1200.0
1	John	3000.0	3	Iphone14	1300.0
2	Jack	2000.0	1	Iphone12	1100.0
2	Jack	2000.0	2	Iphone13	1200.0
2	Jack	2000.0	3	Iphone14	1300.0

------ both are same, cross join or on true condition.
------ if we want to map one record from table1 with all record from table2

If we need to join table A with table B without columns use below 
select * from lower_backup.mobile m1  inner join lower_backup.mobile2 m2
on true;

id	model	price	id	model	price
1	John	3,000	1	Iphone12	1,100
1	John	3,000	2	Iphone13	1,200
1	John	3,000	3	Iphone14	1,300
2	Jack	2,000	1	Iphone12	1,100
2	Jack	2,000	2	Iphone13	1,200
2	Jack	2,000	3	Iphone14	1,300


-----  alphabet in order   -- helpful in when ordering required in alphabetical order (lexicographically)
ASCII('A')  -- 65
ASCII('a')  -- 65

changing numbers back to alphabets
chr(65) -- A 


IN vs JOIN:
JOIN operations tend to execute faster than IN clauses for retrieving data, especially with large datasets and proper indexing.

Round() --> to nearest number example 38.5 to 39, 38.4 to 38


Nth Value:
https://www.commandprompt.com/education/how-to-use-nth_value-function-in-postgresql/

view vs MATERIALIZED views:
view: store the query no the result dataset. If base table data change it will result automatically in the view.

MATERIALIZED view: store result of the query and take a snapshot of the data at that certain point of time.
If base table data change it will not reflect automatically in the view. 
This has to be refreshed periodically or on-demand.

Refresh materialized view: REFRESH MATERIALIZED VIEW lower_backup.m_vw_employees;   


Regexp_count:
regexp_count('text/string', 'search char for count')
SELECT REGEXP_COUNT('foobarbaz', 'ba');
count is 2.



I have records for two employee id's where flag = Y for all three records then pull the employee id
If flag as N record in any one of the record those don't pull that employee record.

Employee_id  flag 
1			  Y
1			  Y
1			  Y
2			  Y
2			  N
2			  Y

using lag and case statement won't work use in clause.

select * from table where employee_id not in 
(select distinct employee_id from table where flag = 'N')


inner join vs intersect:
inner join: 
matching records or common records from both tables,  duplicate will return in query result.

intersect:
common records but duplicates are not allowed, structure of both  tables should be match.
NULL Value Comparisons Are Respected: Includes NULL comparisons, treating them distinctly.

unnest:
means expaning array

Id  location
1   {'Texas', 'Florida'}

select id, unnest(location)
from table 

id   unnest
1     Texas
2     Florida

data type define 
column text []
accessing column_name[1]

select array[column_name] --> write data into array format
array_column || array_newcolumn --> new column data is appending into odl column.



string_to_array():

192.168.01.1  convert this data into {"192", "168", "01", "1"}
string_to_array(ip, '.')::text[] as octet
converting to text is important because of 01, 0 should remain other wise 
0 will be trimmed if we convert it into int or floar.

unnest(above array)

regexp_count(replace(ip, '.', '#'), '#') as rep_ip_count

position('0' in ip) --> return 0 in which position

Inclause if we need to check with two or more fields, below way we need to follow.
where (task_id, subtask_id) not in (select task_id, subtask_id from Executed)
In the subquery both columns shouldn't be keep in single quotes.


consective date:
if given a is a date then they are in consective or not instead of applying row_number() and segrigating them as 
group or self join use this will return consective group of dates.
Leet code example: 1454 database
(login_date - (row_number() over(partition by id order by login_date) || 'day')::interval)::date as previous_day


convert the seconds in HH::MM::SS format.
TO_CHAR((duration || ' second')::interval, 'HH24:MI:SS') as duration_formatted


SQL coding, questions need to ask?
Same data 
duplicate data, 
multiple records, 
null values,
zeros, 

When working with consective date check the date range is asked with in the YEAR
or dates may fall into another YEAR.
Ex: 2021-12-01 
    2022-01-01  these two are consective month. If we apply just add as +1 then this kind of data will through an issues.



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

refer leetcode 3156.

1) Peak concurrent jobs (overlapping time windows)
Question: Given job intervals, compute the maximum number of jobs running at the same time.

2. Concurrency at each job start
Question: For each job, how many other jobs were already running when it started?

3. Find overlapping pairs (duplicate processing / collisions)
Question: Find all pairs of jobs on the same resource whose run windows overlap, and return the overlap interval.



overlapping shifts:
second shift start time should greater than first shift start time and 
second shift start time less than first shift end time.

e1.start_time > e2.start_time and 
e1.start_time < e2.end_time;




count(*) vs column(column):
count(*) vs count(1) both are same, counts null values
count(column) exclude null values, can be slower as it checks each value for null.


# Deadlocks:
deadlocks is a situtation in a database where two or more transactions are permanently waiting for each other to release 
locks and none of them can proceed.

Example:
begin tran;
update accounts set balance = balance - 100 where id = 1;

begin tran;
update accounts set balance =  balance + 100 where id = 2;

T1 locks Row 1 and tries to access Row2
T2 locks Row 2 and tries to access Row1

T1 waits for T2 
T2 waits for T1 --> Deadlock.

Apply + fix:
identify and kill one other continues.


Hints:
postgres default doesn't support hints like oracle or mysql.
why postgres doesn't support hints means default postgres will choose good execution plan.
In oracle if it doesn't pick good execution plan during run time oracle engine will pick good execution plan based on hints.

pg_hint_plan an extension need to be download then only hints will supported in postgresql.
create extension pg_hint_plan;

what these hints will do is getting the data very faster.
types of hints:
1. index scan   select /*+ IndexScan(employees idx_emp_id) */  
instead of scanning entire table it will fetch the data based on index.
2. seq scan   full table get scanned 
3. Hash join   (hash table will be created for smaller table instead of full scan it will fetch data from hash table)
4. merge join  (sorted merge join)
A Sort Merge Join in PostgreSQL combines two datasets by first ensuring both are sorted on the join key and then merging them in a single, synchronized pass
5. nestloop 



FILTER:
SUM(salary) FILTER (WHERE department = 'IT') AS it_salary
count(*) FILTER(where dept = 'Sales') as sales_count,
