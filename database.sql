CREATE DATABASE IF NOT EXISTS tv_store;
USE tv_store

CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS televisions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(100),
    model VARCHAR(100),
    price DECIMAL(10,2),
    description TEXT
);

INSERT INTO admin (username, password) VALUES ('admin', 'admin123'); -- Plaintext for demo only
