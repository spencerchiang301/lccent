use training;

# 插入資料至資料表裡 - insert into
insert into students(id, first_name, last_name, age, sex)
values(1,'Jack', 'Wang', 33, 1);

insert into students(id, first_name, last_name, age, sex)
values(2,'Helen', 'Lin', 22, 2);

insert into students(id, first_name, last_name, age, sex)
values(3,'Tom', 'Chang', 30, 1);

# 查詢資料表總筆數 -select 
select count(*) from students;

# 取出該資料表的內容
select * from students;



