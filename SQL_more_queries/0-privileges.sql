-- a script that lists all privileges of the MySQL users
SELECT *
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');
