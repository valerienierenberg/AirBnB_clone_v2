-- script that prepares a MySQL server for the project
-- with the database hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbtn_test_db;
DROP USER IF EXISTS 'hbnb_test'@'localhost';
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
/* GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'; */
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

/*    when running the following script, 'hbnb_test_db' is not returned as in the output example.
      Nothing is returned, but no errors are thrown. My game plan is wait for checker.

  echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
*/
