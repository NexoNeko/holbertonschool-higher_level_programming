-- creates the MySQL server user user_0d_1 if it does not exists, w/all privileges
CREATE USER IF NOT EXISTS 'newuser'@'localhost' IDENTIFIED BY 'pa$$word';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
