use training;

show tables;

select * from employees;


select * from employees 
where salary > 
(select avg(salary) from employees);

select * from employees;