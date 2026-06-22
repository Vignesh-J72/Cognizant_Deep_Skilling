/* Task 1*/
-- 35
SELECT employee_id,COUNT(module_id) FROM certifications GROUP BY employee_id HAVING COUNT(module_id) 
       >(SELECT AVG((module_no)) FROM (
        SELECT COUNT(module_id) AS module_no FROM certifications GROUP BY employee_id) AS T);

-- 36
SELECT s.module_name FROM skill_modules s 
WHERE EXISTS (
    SELECT 1 FROM certifications c WHERE c.module_id = s.module_id
) 
AND NOT EXISTS (
    SELECT 1 FROM certifications c WHERE c.module_id = s.module_id AND (c.grade != 'A' OR c.grade IS NULL)
);

-- 37
SELECT i.instructor_name,i.department_id,i.salary FROM instructors i
    WHERE i.salary=(
        SELECT MAX(s.salary) FROM instructors s WHERE s.department_id=i.department_id
    );

-- 38
SELECT depart.department_id,depart.avg_salary FROM (
    SELECT department_id,AVG(salary) as avg_salary FROM instructors 
    GROUP BY department_id ) AS depart 
    WHERE depart.avg_salary>85000; 

/* Task 2 */
-- 39
CREATE VIEW vw_employee_completion_summary AS 
    SELECT e.employee_id, CONCAT(e.first_name,' ',e.last_name) AS employee_name
    ,d.dept_name, COUNT(c.module_id) AS courses_enrolled,
    ROUND( AVG(
        CASE c.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
            END),2)
            AS gpa
    FROM employees e LEFT JOIN certifications c ON e.employee_id=c.employee_id
    JOIN departments on e.dept_name=d.dept_name
    GROUP BY e.employee_id, e.first_name, e.last_name, e.department;

-- 40
CREATE VIEW vw_course_stats AS
    SELECT s.module_name,s.module_code, COUNT(c.employee_id),
    ROUND(AVG(
        CASE c.grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
            END),2)
            AS gpa 
        FROM skill_modules s LEFT JOIN certifications c ON s.module_id=c.module_id
        GROUP BY s.module_name,s.module_code HAVING count(c.employee_id)>0;

-- 41
SELECT employee_name FROM vw_employee_completion_summary WHERE gpa>3.00;

-- 42
UPDATE vw_employee_completion_summary SET gpa=4.5 WHERE employee_id=1;
/*ERROR 1288 (HY000): The target table vw_employee_completion_summary of 
  the UPDATE is not updatable is displayed when attempting to update view*/

-- 43
DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_employee_completion_summary;

CREATE VIEW vw_employee_completion_summary AS
SELECT employee_id,first_name,last_name FROM employees WHERE dept_id=1 WITH CHECK OPTION;

/*task 3 */
-- 44
DELIMITER $$

CREATE PROCEDURE sp_enroll_employee(
    IN p_employee_id INT,
    IN p_module_id INT,
    IN p_enrollment_date DATE
)
BEGIN
    DECLARE v_duplicate_count INT DEFAULT 0;

    SELECT COUNT(*) INTO v_duplicate_count 
    FROM certifications 
    WHERE employee_id = p_employee_id AND module_id = p_module_id;

    IF v_duplicate_count > 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Enrollment Rejected: This employee is already registered for this specific module.';
    ELSE
        INSERT INTO certifications (employee_id, module_id, enrollment_date)
        VALUES (p_employee_id, p_module_id, p_enrollment_date);
    END IF;
END$$

DELIMITER ;


-- 45
CREATE TABLE IF NOT EXISTS department_transfer_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    old_department_id INT,
    new_department_id INT,
    transfer_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER $$

CREATE PROCEDURE sp_transfer_student(
    IN p_employee_id INT,
    IN p_new_department_id INT
    )
    BEGIN
    DECLARE v_old_department_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Transaction Aborted: Structural exception caught. System state rolled back.';
    END;

SELECT department_id INTO v_old_department_id FROM employees WHERE employee_id = p_employee_id;
    START TRANSACTION;
        UPDATE employees 
        SET department_id = p_new_department_id 
        WHERE employee_id = p_employee_id;
        
      
        INSERT INTO department_transfer_log (employee_id, old_department_id, new_department_id)
        VALUES (p_employee_id, v_old_department_id, p_new_department_id);
        
    COMMIT;
END$$

DELIMITER ;

-- 46
SELECT employee_id, department_id FROM employees WHERE employee_id = 1;
CALL sp_transfer_student(1, 999999);
SELECT employee_id, department_id FROM employees WHERE employee_id = 1;

-- 47
START TRANSACTION;
    INSERT INTO certifications (employee_id, module_id, enrollment_date)
    VALUES (1, 101, '2026-06-17');
    SAVEPOINT first_insert_checkpoint;
    INSERT INTO certifications (employee_id, module_id, enrollment_date)
    VALUES (NULL, 999, '2026-06-17'); 
    ROLLBACK TO SAVEPOINT first_insert_checkpoint;

COMMIT;
SELECT * FROM certifications WHERE employee_id = 1 AND module_id = 101;
