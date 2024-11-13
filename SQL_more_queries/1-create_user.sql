-- comment
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant only the necessary privileges
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, INDEX, SHOW DATABASES, EXECUTE
    ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
