#update

use training;

select * from students where last_name = 'Lee';`

update students set age=35 where id = 5;
update students set age = 32, sex =2
where last_name='Lee';

#like '%%'

select * from students where first_name like '%v%';
select * from students where first_name like 'v%';
select * from students where first_name like '%v';


select * from students WHERE age = 33 and sex=2;

delete from students where first_name like 'v%';

#alter table
describe students;

alter table students add column phone varchar(20);
alter table students modify column phone varchar(30);

select version();




