-- prepares a MySQL server for the project database hbnb_dev_db
-- new user hbnb_dev in localhost
-- password of hbnb_dev set to hbnb_dev_pwd
-- user should have all privileges on hbnb_dev_db
-- user should have SELECT privileges on database performance_schema
-- if the database hbnb_dev_db or user hbnb_dev already exist script shouldnt
-- fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
DROP USER IF EXISTS 'hbnb_dev'@'localhost';
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
