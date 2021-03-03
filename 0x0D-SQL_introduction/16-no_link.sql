-- a script that lists all records of the table
-- don't list rows without a name value
-- results should display score and name and score should be listed by descending order

SELECT score, name FROM second_table WHERE name NOT NULL ORDER BY DESC;
