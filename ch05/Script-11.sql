use training;

drop table students;

create table students(
	id int not null, 
	first_name char(10) not null,  
	last_name char(10) not null,
	age int not null,
	sex char(1),
	primary key(id)
);


select * from students;

# filter -> where 
select * from students where age >= 25;

select * from students where age >= 25 and sex = 1;

select * from students where age between 25 and 27;

# sort -> order by
select * from students order by first_name;
select * from students order by first_name desc;

# combined
select * from students where age = 25 order by first_name desc;

# group -> group by

select last_name, count(*) from students group by last_name having count(*) > 2;

# LIMIT -> limit number

select * from students where age > 25 limit 2;

# distinct
select last_name from students;

select distinct last_name from students;

create table grades(
	id int not null, 
	english int not null, 
	chinese int not null
);

select * from grades;

insert into grades(id, english, chinese) values(10, 80, 90);
insert into grades(id, english, chinese) values(11, 75, 82);
insert into grades(id, english, chinese) values(12, 66, 85);

# JOIN 
select s.first_name, s.last_name, g.english, g.chinese from students as s
left join grades as g
on s.id = g.id;