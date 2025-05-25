create table person(
	id int primary key,
	name varchar(20), 
	manager_id varchar(2)
);

create table person_info(
	id int primary key,
	age int,
	phone varchar(20)
	);

insert into person(id, name, manager_id) values(1, 'Jack', null),
(2, 'Helen', 1),(3,'Tom', 1),(4,'Jane', 2),(5,'Lisa',2);

insert into person_info values(1, 22, '0911222333'),(3,33,'0977666555'),
(5, 35,'0976555444'),(7, 34, '0933444555'),(9,45,'0965555444');

drop table person;

select * from person;

select * from person_info;

select id, name from person;
select age, phone from person_info;

# left join, right join, inner join, self.join

# left join 左表為準, 右表沒有值的地方補null
select person.id, person.name, person_info.id, person_info.age, person_info.phone 
from person
left join person_info 
   on person.id = person_info.id;

select p.id, p.name, pi.age, pi.phone 
from person as p
left join person_info as pi 
   on p.id = pi.id;

# right join, 右表為準, 沒有值也是補 null
select person.id 'person_id', person.name, person_info.id 'person_info_id', person_info.age, person_info.phone 
from person
right join person_info 
   on person.id = person_info.id;

# inner join, 交集
select person.id, person.name, person_info.id, person_info.age, person_info.phone 
from person
inner join person_info 
   on person.id = person_info.id;

# self join
select p.id, p.name, p2.name 'Manager Name', p.manager_id
from person p
left join person p2 
on p.manager_id = p2.id


select * from person;
