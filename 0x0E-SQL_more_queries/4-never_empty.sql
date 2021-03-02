-- a script that creates the table id_not_null on your MySQL server and if it exists script shouldn't fail
-- the database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT 1,
	name VARCHAR(256)
	);
