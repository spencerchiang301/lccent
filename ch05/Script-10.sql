use training;

select * from students;

select first_name, last_name from students;

select first_name, last_name, age from students;


select first_name AS 'test名', last_name AS '姓', age '年齡' from students;


INSERT INTO students (id, first_name, last_name, age, sex) VALUES
(4, 'Amy', 'Chen', 21, 2),
(5, 'Brian', 'Lee', 25, 1),
(6, 'Cindy', 'Wu', 23, 2),
(7, 'David', 'Huang', 24, 1),
(8, 'Emma', 'Chang', 22, 2),
(9, 'Frank', 'Liu', 26, 1),
(10, 'Grace', 'Hsu', 21, 2),
(11, 'Henry', 'Wang', 27, 1),
(12, 'Ivy', 'Tsai', 20, 2),
(13, 'Jason', 'Lin', 22, 1),
(14, 'Kelly', 'Chen', 23, 2),
(15, 'Leo', 'Shen', 25, 1),
(16, 'Mia', 'Kao', 21, 2),
(17, 'Nathan', 'Yang', 24, 1),
(18, 'Olivia', 'Wang', 20, 2),
(19, 'Peter', 'Wu', 26, 1),
(20, 'Queenie', 'Lin', 22, 2),
(21, 'Ryan', 'Liao', 27, 1),
(22, 'Sandy', 'Chang', 21, 2),
(23, 'Tony', 'Chen', 25, 1),
(24, 'Una', 'Ho', 23, 2),
(25, 'Victor', 'Huang', 26, 1),
(26, 'Wendy', 'Liu', 22, 2),
(27, 'Xavier', 'Tsai', 24, 1),
(28, 'Yuki', 'Wang', 21, 2),
(29, 'Zack', 'Wu', 27, 1),
(30, 'Amber', 'Lin', 22, 2),
(31, 'Ben', 'Chang', 20, 1),
(32, 'Claire', 'Chen', 23, 2),
(33, 'Derek', 'Lee', 25, 1),
(34, 'Ella', 'Liao', 21, 2),
(35, 'Finn', 'Yang', 26, 1),
(36, 'Gina', 'Huang', 22, 2),
(37, 'Harry', 'Shen', 24, 1),
(38, 'Isabelle', 'Liu', 20, 2),
(39, 'Jacky', 'Wu', 27, 1),
(40, 'Kathy', 'Chen', 21, 2),
(41, 'Louis', 'Tsai', 26, 1),
(42, 'May', 'Kao', 23, 2),
(43, 'Noah', 'Ho', 24, 1),
(44, 'Olga', 'Lin', 22, 2),
(45, 'Paul', 'Yang', 25, 1),
(46, 'Rita', 'Hsu', 20, 2),
(47, 'Steve', 'Wang', 27, 1),
(48, 'Tina', 'Wu', 21, 2),
(49, 'Ulysses', 'Chang', 24, 1),
(50, 'Vivian', 'Lee', 23, 2),
(51, 'Will', 'Chen', 25, 1),
(52, 'Xena', 'Liao', 22, 2),
(53, 'Yves', 'Kao', 26, 1);
