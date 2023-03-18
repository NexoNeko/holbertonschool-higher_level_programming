/* creates the database hbtn_0d_2 and the user user_0d_2, with
nothing but SELECT privilege.
Password set to user_0d_2_pwd
if database or user exists, script doesn't fails.*/
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';