-- creates the database hbtn 0d usa
CREATE DATABASE IF NOT EXISTS
hbtn_0d_usa;
-- switches to the database in order to create the table
USE hbtn_0d_usa;
-- creates the table with auto-incrementing id and sets primary key
CREATE TABLE IF NOT EXISTS states (
	id INT(1) NOT NULL AUTO_INCREMENT,
	name VARCHAR (256) NOT NULL,
	PRIMARY KEY (id)
);
