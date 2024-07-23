CREATE SCHEMA dbo

CREATE TABLE dbo.user (
  user_id serial PRIMARY KEY,
  email varchar(256) NOT NULL UNIQUE,
  first_name varchar(256) NOT NULL,
  last_name varchar(256) NOT NULL,
  phone_number varchar(256) NOT NULL,
  password_hash char(60) NOT NULL,
  UNIQUE (email)
);

-- The type serial stores a sequential integer (INT) that is automatically assigned by the database server when a new row is intserted
-- The type varchar(256) is a char always stored at 256 characters 

CREATE TABLE dbo.plant_foods (
  plant_id serial PRIMARY KEY, 
  food_name varchar(256) NOT NULL UNIQUE,
  food_kind varchar(256) NOT NULL,
  UNIQUE (food_name)
)

-- TO DO: Create a table to represent data for the food classifier
-- TO DO: Add sample data to the users table
-- TO DO: Automatically add all data from the food classifier csvs to postgres on startup