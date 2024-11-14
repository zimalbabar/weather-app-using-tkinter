CREATE DATABASE WEATHER_DB;
USE WEATHER_DB;
CREATE TABLE weather_days (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255),
    temp_day DECIMAL(5, 2),
    temp_night DECIMAL(5, 2),
    humidity INT,
    pressure DECIMAL(6, 2),
    wind_speed DECIMAL(6, 2),
    description VARCHAR(255),
    icon varchar(255),
    date_time DATETIME
);
CREATE TABLE weather_db (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255),
    temp DECIMAL(5, 2),
    humidity INT,
    pressure DECIMAL(6, 2),
    wind_speed DECIMAL(6, 2),
    description VARCHAR(255)
);
CREATE TABLE sugg_box (
    name varchar(255),
    email varchar(255),
    suggestion varchar(255)
)