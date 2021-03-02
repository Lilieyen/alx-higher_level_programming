-- a script that creates the table unique_id on your MySQL server and if it exists it shouldn't fail
-- the database name will be passed as an argument of the mysql command
-- id INT shold have defailt value 1 and should be unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
