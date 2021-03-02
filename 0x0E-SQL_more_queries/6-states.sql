-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- id INT unique, auto generated, can’t be null and is a primary key and name VARCHAR(256) can’t be null
-- if hbtn_0d_usa and states exist script shouldn't fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE IDENTITY PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL
	);
