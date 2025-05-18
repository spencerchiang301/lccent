use mysql;

create user 'user100'@'%' identified by 'abc123';
grant select on training.students to 'user100'@'%';