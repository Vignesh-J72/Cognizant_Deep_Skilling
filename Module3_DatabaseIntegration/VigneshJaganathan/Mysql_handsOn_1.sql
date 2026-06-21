/*task 1*/
CREATE DATABASE IF NOT EXISTS corporate_db;
USE corporate_db;

CREATE TABLE departments(
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE employees(
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    hiring_year INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE skill_modules(
    module_id INT PRIMARY KEY AUTO_INCREMENT,
    module_name VARCHAR(150) NOT NULL,
    module_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY(department_id) REFERENCES departments(department_id)
);

CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    instructor_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE certifications (
    certification_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    module_id INT,
    completion_date DATE,
    grade CHAR(2), 
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (module_id) REFERENCES skill_modules(module_id)
);
--3NF has been verified

/*task 3*/
ALTER TABLE employees ADD contact_number VARCHAR(15);
ALTER TABLE skill_modules ADD max_seats INT DEFAULT 60;
ALTER TABLE certifications ADD CHECK (grade in ('A','B','C','D','F') OR grade IS NULL);
ALTER TABLE departments RENAME COLUMN hod_name TO head_of_dept;
ALTER TABLE employees DROP COLUMN contact_number;
ALTER TABLE departments RENAME COLUMN head_of_dept TO hod_name;


