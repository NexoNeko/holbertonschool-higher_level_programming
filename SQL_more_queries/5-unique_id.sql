-- creates the table unique_id with an unique id
CREATE TABLE IF NOT EXISTS 
unique_id (
	id INT NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR (256)
);