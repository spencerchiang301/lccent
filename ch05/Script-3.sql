create user 'user1'@'%' identified by 'nicole';
grant all privileges on *.* to 'user1'@'%' with grant option;

select user, host from mysql.user;

create user 'user100'@'%' identified by 'abc123';
grant select, insert, update, delete on training.* to 'user100'@'%';
