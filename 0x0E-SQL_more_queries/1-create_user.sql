-- a script that creates the MySQL server user user_0d_1 and a password user_0d_1_pwd
-- if user exists script shouldn't fail

CREATE IF NOT EXIST USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
