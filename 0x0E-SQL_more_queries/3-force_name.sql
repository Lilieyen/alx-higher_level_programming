-- a script that creates the table force_name on your MySQL server and if it exists script shouldn't fail
-- the database name will be passed as an argument of the mysql command

CREATE TABLE force_name IF NOT EXISTS (
	id INT,
	name VARCHAR(256) NOT NULL
	);
