-- Write a SQL query to find the names and salaries of employees along with their managers' names and salaries,
-- where the manager's salary is greater than the employee's salary.
-- The result should include the employee's name, employee's salary, manager's name, and manager's salary.

-- employee salary greater than manager salary
select b.name as emplyoeename, b.salary as employee_salary, a.name as managername, a.salary as manager_salary
from employee a
join employee b on a.id = b.manager_id
where a.salary > b.salary;



select a.name, a.salary, b.name, b.salary
from employee a 
join employee b on a.manager_id = b.id
where a.salary > b.salary;


-- manager salary greater than employee salary
select b.name as emplyoeename, b.salary as employee_salary, a.name as managername, a.salary as manager_salary
from employee a    
join employee b on a.id = b.manager_id
where a.salary < b.salary;

select a.name, a.salary, b.name, b.salary
from employee a 
join employee b on a.manager_id = b.id
where a.salary < b.salary;


-- manager salary equal to employee salary
select b.name as emplyoeename, b.salary as employee_salary, a.name as managername, a.salary as manager_salary               
from employee a    
join employee b on a.id = b.manager_id
where a.salary = b.salary;  

