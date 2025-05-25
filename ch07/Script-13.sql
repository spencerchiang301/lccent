# 顯示所有的資料庫
show databases;

# 連接資料庫
use training;

# 顯示所有的資料表
show tables;

# 顯示所有的資料
select * from students;

# 正確
select first_name from students;

# 欄位名稱錯誤
select frist_name, last_name from students;
 
# 確認值是存在的
select * from students where age = '25';

# 正確的語法
select last_name from students group by last_name;

# group by
select first_name, last_name from students group by last_name ;
 
insert into students(first_name , last_name) values('Linda', 'Wang');

# 要補足所有的欄位值
insert into students values(99,'Linda', 'Wang',22,1,'0988121222');

# 主鍵錯誤
insert into students values(1,'Linda', 'Wang',22,1, '0922333222');

