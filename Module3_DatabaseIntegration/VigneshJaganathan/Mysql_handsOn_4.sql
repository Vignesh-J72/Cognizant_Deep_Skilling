-- hands on 4

-- Task 1
-- 48
EXPLAIN FORMAT=JSON 
    SELECT e.first_name, e.last_name, m.module_name FROM certifications c 
    JOIN employees e ON e.employee_id = c.employee_id 
    JOIN skill_modules m ON m.module_id = c.module_id 
    WHERE e.hiring_year = 2022;

/* | {
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "2.42"
    },
    "nested_loop": [
      {
        "table": {
          "table_name": "e",
          "access_type": "ALL",
          "possible_keys": [
            "PRIMARY"
          ],
          "rows_examined_per_scan": 10,
          "rows_produced_per_join": 1,
          "filtered": "10.00",
          "cost_info": {
            "read_cost": "1.15",
            "eval_cost": "0.10",
            "prefix_cost": "1.25",
            "data_read_per_join": "824"
          },
          "used_columns": [
            "employee_id",
            "first_name",
            "last_name",
            "hiring_year"
          ],
          "attached_condition": "(`corporate_db`.`e`.`hiring_year` = 2022)"
        }
      },
      {
        "table": {
          "table_name": "c",
          "access_type": "ref",
          "possible_keys": [
            "employee_id",
            "module_id"
          ],
          "key": "employee_id",
          "used_key_parts": [
            "employee_id"
          ],
          "key_length": "5",
          "ref": [
            "corporate_db.e.employee_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 1,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.42",
            "eval_cost": "0.17",
            "prefix_cost": "1.83",
            "data_read_per_join": "53"
          },
          "used_columns": [
            "employee_id",
            "module_id"
          ],
          "attached_condition": "(`corporate_db`.`c`.`module_id` is not null)"
        }
      },
      {
        "table": {
          "table_name": "m",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "module_id"
          ],
          "key_length": "4",
          "ref": [
            "corporate_db.c.module_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 1,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.42",
            "eval_cost": "0.17",
            "prefix_cost": "2.42",
            "data_read_per_join": "1K"
          },
          "used_columns": [
            "module_id",
            "module_name"
          ]
        }
      }
    ]
  }
} |
*/

-- 49
-- The query plan shows a full Table scan (ALL) on employees e.

-- 50
-- Number of rows examined = 10, query cost = 2.42

-- Task 2
-- 51
CREATE INDEX employees_hiring_year ON employees(hiring_year);

-- 52
CREATE UNIQUE INDEX certifications_obtained ON certifications(employee_id,module_id);

-- 53
CREATE INDEX module_code ON skill_modules(module_name);

-- 54
EXPLAIN FORMAT=JSON 
    SELECT e.first_name, e.last_name, m.module_name FROM certifications c 
    JOIN employees e ON e.employee_id = c.employee_id 
    JOIN skill_modules m ON m.module_id = c.module_id 
    WHERE e.hiring_year = 2022;

/* {
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "4.90"
    },
    "nested_loop": [
      {
        "table": {
          "table_name": "e",
          "access_type": "ref",
          "possible_keys": [
            "PRIMARY",
            "employees_hiring_year"
          ],
          "key": "employees_hiring_year",
          "used_key_parts": [
            "hiring_year"
          ],
          "key_length": "5",
          "ref": [
            "const"
          ],
          "rows_examined_per_scan": 4,
          "rows_produced_per_join": 4,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "0.50",
            "eval_cost": "0.40",
            "prefix_cost": "0.90",
            "data_read_per_join": "3K"
          },
          "used_columns": [
            "employee_id",
            "first_name",
            "last_name",
            "hiring_year"
          ]
        }
      },
      {
        "table": {
          "table_name": "c",
          "access_type": "ref",
          "possible_keys": [
            "certifications_obtained",
            "module_id"
          ],
          "key": "certifications_obtained",
          "used_key_parts": [
            "employee_id"
          ],
          "key_length": "5",
          "ref": [
            "corporate_db.e.employee_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 6,
          "filtered": "100.00",
          "using_index": true,
          "cost_info": {
            "read_cost": "1.00",
            "eval_cost": "0.67",
            "prefix_cost": "2.57",
            "data_read_per_join": "213"
          },
          "used_columns": [
            "employee_id",
            "module_id"
          ],
          "attached_condition": "(`corporate_db`.`c`.`module_id` is not null)"
        }
      },
      {
        "table": {
          "table_name": "m",
          "access_type": "eq_ref",
          "possible_keys": [
            "PRIMARY"
          ],
          "key": "PRIMARY",
          "used_key_parts": [
            "module_id"
          ],
          "key_length": "4",
          "ref": [
            "corporate_db.c.module_id"
          ],
          "rows_examined_per_scan": 1,
          "rows_produced_per_join": 6,
          "filtered": "100.00",
          "cost_info": {
            "read_cost": "1.67",
            "eval_cost": "0.67",
            "prefix_cost": "4.90",
            "data_read_per_join": "4K"
          },
          "used_columns": [
            "module_id",
            "module_name"
          ]
        }
      }
    ]
  }
} 
*/

-- 55
CREATE INDEX partial_certifications ON certifications(employee_id,grade);

-- Task 3 
-- 56
SELECT * FROM certifications THEN 