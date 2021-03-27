-- script that prepares a MySQL server for the project
-- with the database hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
/* GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'; */
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
