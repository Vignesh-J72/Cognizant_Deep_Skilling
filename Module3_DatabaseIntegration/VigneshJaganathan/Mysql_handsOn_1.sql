/*task 1*/
CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;

CREATE TABLE departments(
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE students(
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    department_id INT,
    enrollment_year INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE courses(
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    department_id INT,
    FOREIGN KEY(department_id) REFERENCES departments(department_id)
);

CREATE TABLE professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    grade CHAR(2), 
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

/*task 3*/
ALTER TABLE students ADD phone_number VARCHAR(15);
ALTER TABLE courses ADD max_seats INT DEFAULT 60;
ALTER TABLE enrollments ADD CHECK (grade in ('A','B','C','D','F') OR grade IS NULL);
ALTER TABLE departments RENAME COLUMN hod_name TO head_of_dept;
ALTER TABLE  students DROP COLUMN phone_number;
ALTER TABLE departments RENAME COLUMN head_of_dept TO hod_name;