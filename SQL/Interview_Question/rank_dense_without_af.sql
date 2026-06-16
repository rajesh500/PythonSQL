---- assign a rank without using an analytic function
select *, 
(select (count(*)+ 0) from employee b where a.salary <= b.salary) as rank
from employee a
order by a.sal desc;


---- dense rank without using analytic function
select *, 
(select (count(distinct b.salary)+ 0) from employee b where a.salary <= b.salary) as rank
from employee a
order by a.sal desc;
