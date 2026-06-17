/*task 1*/
INSERT INTO departments (dept_name, hod_name, budget) VALUES
    ('Computer Science', 'Dr. Ramesh Kumar', 850000.00),
    ('Electronics', 'Dr. Priya Nair', 620000.00),
    ('Mechanical', 'Dr. Suresh Iyer', 540000.00),
    ('Civil', 'Dr. Ananya Sharma', 430000.00);


INSERT INTO employees (first_name, last_name, email, date_of_birth, department_id,
hiring_year) VALUES
    ('Arjun', 'Mehta', 'arjun.mehta@corporate.com', '2003-04-12', 1, 2022),
    ('Priya', 'Suresh', 'priya.suresh@corporate.com', '2003-07-25', 1, 2022),
    ('Rohan', 'Verma', 'rohan.verma@corporate.com', '2002-11-08', 2, 2021),
    ('Sneha', 'Patel', 'sneha.patel@corporate.com', '2004-01-30', 3, 2023),
    ('Vikram', 'Das', 'vikram.das@corporate.com', '2003-09-14', 1, 2022),
    ('Kavya', 'Menon', 'kavya.menon@corporate.com', '2002-05-17', 2, 2021),
    ('Aditya', 'Singh', 'aditya.singh@corporate.com', '2004-03-22', 4, 2023),
    ('Deepika','Rao', 'deepika.rao@corporate.com', '2003-08-09', 1, 2022);


INSERT INTO skill_modules (module_name, module_code, credits, department_id) VALUES
    ('Data Structures & Algorithms', 'CS101', 4, 1),
    ('Database Management Systems', 'CS102', 3, 1),
    ('Object Oriented Programming', 'CS103', 4, 1),
    ('Circuit Theory', 'EC101', 3, 2),
    ('Thermodynamics', 'ME101', 3, 3);


INSERT INTO certifications (employee_id, module_id, completion_date, grade) VALUES
    (1, 1, '2022-07-01', 'A'), (1, 2, '2022-07-01', 'B'),
    (2, 1, '2022-07-01', 'B'), (2, 3, '2022-07-01', 'A'),
    (3, 4, '2021-07-01', 'A'), (4, 5, '2023-07-01', NULL),
    (5, 1, '2022-07-01', 'C'), (5, 2, '2022-07-01', 'A'),
    (6, 4, '2021-07-01', 'B'), (7, 5, '2023-07-01', NULL),
    (8, 1, '2022-07-01', 'A'), (8, 3, '2022-07-01', 'B');


INSERT INTO instructors (instructor_name, email, department_id, salary) VALUES
    ('Dr. Anand Krishnan', 'anand.k@corporate.com', 1, 95000.00),
    ('Dr. Meena Pillai', 'meena.p@corporate.com', 1, 88000.00),
    ('Dr. Sunil Rajan', 'sunil.r@corporate.com', 2, 82000.00),
    ('Dr. Latha Gopal', 'latha.g@corporate.com', 3, 79000.00),
    ('Dr. Kartik Bose', 'kartik.b@corporate.com', 4, 76000.00);

INSERT INTO employees (first_name, last_name, email, date_of_birth, department_id,
hiring_year) VALUES 
    ('Ankit','Juju','ankit.juju@corporate.com.in','2005-10-18',1,2024),
    ('Banu','Shree','banu.shree@corporate.com.in','2004-10-01',1,2023);
SELECT * FROM employees;

UPDATE certifications SET grade='B' WHERE employee_id=5 AND module_id=1;
SELECT * FROM certifications;

DELETE FROM certifications WHERE grade IS NULL;
SELECT * FROM certifications;

/* Task 2*/
SELECT * FROM employees WHERE hiring_year=2022 ORDER BY last_name DESC;

SELECT * FROM instructors WHERE salary<=95000 AND salary>=80000;

SELECT module_name, credits FROM skill_modules WHERE credits>3 ORDER BY credits DESC;

SELECT CONCAT(first_name,last_name) as employee_name FROM employees where email LIKE '%@corporate.com';

SELECT COUNT(*) FROM employees;

/*task 3*/

SELECT CONCAT(e.first_name,' ',e.last_name),d.dept_name FROM employees e JOIN  departments d ON e.department_id=d.department_id;

SELECT c.certification_id,CONCAT(e.first_name, ' ', e.last_name) AS employee_name,m.module_name
    FROM certifications c JOIN employees e ON c.employee_id = e.employee_id
    JOIN skill_modules m ON c.module_id = m.module_id;

SELECT CONCAT(e.first_name,' ',e.last_name) FROM employees e LEFT JOIN certifications c ON e.employee_id =c.employee_id IS NULL;

SELECT s.module_name,s.module_id, COUNT(DISTINCT(c.employee_id)) FROM skill_modules s LEFT JOIN certifications c ON s.module_id=c.module_id GROUP BY s.module_name,s.module_id;

SELECT d.dept_name,i.instructor_name,i.salary FROM departments d 
    LEFT JOIN instructors i ON d.department_id=i.department_id;

/*TASK 4*/

SELECT s.module_name,COUNT(c.module_id) AS enrollment_count 
  FROM skill_modules s JOIN certifications c ON s.module_id=c.module_id GROUP BY s.module_name;

SELECT instructor_name, ROUND(AVG(salary),2) FROM instructors GROUP BY instructor_name;

SELECT dept_name, budget FROM departments WHERE budget >600000;

SELECT c.grade, COUNT(*), from certifications c JOIN skill_modules s ON c.module_id=s.module_id WHERE s.module_code='CS101'  GROUP BY grade;

SELECT d.dept_name from departments d JOIN employees e ON d.department_id=e.department_id HAVING count(*)>2;
