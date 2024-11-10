-- A SQL script that creates a table users with id, email, name and country columns

-- Create a table
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM("US", "CO", "TN") NOT NULL
);