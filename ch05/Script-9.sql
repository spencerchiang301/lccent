use training;

select * from students;

describe students;

insert into students(first_name, last_name) values('spencer','chiang');

insert into students(id, first_name, last_name, age, sex) values(1, 'cindy','Wu1', 23, 2);

insert into students(id, first_name, last_name, age, sex) 
values(2, 'cindy2','Wu', 23, 2),(3, 'jack','liu', 33, 2);
2
insert into students(id, first_name, last_name, age, sex) values(1, 'cindy2','Wu1', 25, 2);


drop table students;

create table students(
	id int not null, 
	first_name char(10) not null,  
	last_name char(10) not null,
	age int not null,
	sex char(1),
	primary key(id)
);
