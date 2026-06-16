
---- 1---- 
------ calcualte the percentage of each age record in the table.
----- what is the percentage share of each record.

example data:
person age  
A1 54
A2 53   
A3 52
A4 58   
A5 54
C1 20
C2 19
C3 22
C4 15


select age, count(*)*100/sum(count(*)) over () as percentage
from person 
group by age;

---- another way

select age, count(*) * 100.0 / (select count(*) from person) as percentage as percentage
from person;

---- 2 ----
----- percentage of each department
SELECT
    department,
    SUM(sales) * 100.0 / (SELECT SUM(sales) FROM sales_data) AS pct_sales
FROM sales_data
GROUP BY department;


---- 3 ----
---- with in the department each record percentage calculation
SELECT
  region,
  salesperson,
  amount,
  ROUND(
    amount * 100.0 / SUM(amount) OVER (PARTITION BY region), 
    2
  ) AS pct_within_region
FROM sales;

---- 4 ----
----  Percentage Change Between Rows
----  how much percentage change from previous day to current day
----  sales growth percentage ... day by day, week by week , month by month, year by year.

------ *** formula *** -------
---- ((current_value - previous_value) / previous_value ) * 100

SELECT
    sales_date,
    amount,
    LAG(amount) OVER (ORDER BY sales_date) AS previous_amount,
    ROUND(
        ((amount - LAG(amount) OVER (ORDER BY sales_date)) * 100.0) / 
        NULLIF(LAG(amount) OVER (ORDER BY sales_date), 0), 
        2
    ) AS pct_change




