use training;

show tables;

create table employees(
	employee_id int, 
	first_name varchar(50),
	last_name varchar(50),
	salary int,
	primary key(employee_id)
);

INSERT INTO employees (employee_id, first_name, last_name, salary) VALUES
(1, 'Hannah', 'Walker', 54139),
(2, 'George', 'Lee', 58070),
(3, 'Charlie', 'King', 48927),
(4, 'Fiona', 'Smith', 64272),
(5, 'Bob', 'Taylor', 119508),
(6, 'George', 'Taylor', 102073),
(7, 'Hannah', 'Taylor', 69990),
(8, 'Hannah', 'Taylor', 45726),
(9, 'Charlie', 'Allen', 77297),
(10, 'Ethan', 'Walker', 114602);

select * from employees;

select sum(salary) from employees;

select avg(salary) from employees;

select max(salary) from employees;

select min(salary) from employees;

select count(*) from employees;

select last_name, avg(salary) as avg_salary
from employees
group by last_name;

select count(*) as high_salary, 
       sum(salary) as high_salary_total
from employees
where salary > 80000;

select 
  last_name, 
  MAX(salary) as max_salary,
  Min(salary) as min_salary
from employees
group by last_name;

