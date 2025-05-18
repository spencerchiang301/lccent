# 建立資料庫
create database training;
create database lcc;

# 查詢資料庫
show databases;

# 刪除資料庫, 要非常的小心
drop database training;

drop table students;


# 選擇資料庫
use training;

# 建立資料表
create table students(
	id int,
	first_name char(10), 
	last_name char(10),
	age int, 
	sex bool
);

# 查詢資料表
show tables;

# 查詢表格資料欄位
show columns from students;


