CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Sales'),
(4, 'HR'),
(5, 'Finance');

select * from departments;

CREATE TABLE employees2 (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary INT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

create index 

INSERT INTO employees2 (employee_id, first_name, last_name, salary, department_id) VALUES
(1, 'Hannah', 'Lee', 64417, 1),
(2, 'Hannah', 'Walker', 58295, 1),
(3, 'Fiona', 'Brown', 92437, 3),
(4, 'Alice', 'Taylor', 94427, 5),
(5, 'Ian', 'Allen', 79038, 4),
(6, 'Charlie', 'Allen', 46427, 1),
(7, 'Fiona', 'Young', 52817, 5),
(8, 'Julia', 'Young', 60739, 2),
(9, 'Charlie', 'Lee', 84298, 4),
(10, 'Bob', 'Young', 41372, 2);

#薪資最高的那個部門
SELECT department_name, avg_salary FROM (
    SELECT
        d.department_name,
        AVG(e.salary) AS avg_salary
    FROM employees2 e
    JOIN departments d ON e.department_id = d.department_id
    GROUP BY d.department_name
) AS dept_avg
ORDER BY avg_salary DESC
LIMIT 1;

#找出每個部門中薪資最高的員工
SELECT e.*
FROM employees2 e
WHERE salary = (
    SELECT MAX(salary)
    FROM employees2
    WHERE department_id = e.department_id
);



