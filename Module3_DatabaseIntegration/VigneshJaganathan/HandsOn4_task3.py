import pymysql
import time

# Base DB Connection Details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'vigneshj722',
    'database': 'corporate_db',
    'cursorclass': pymysql.cursors.DictCursor   
}

#task 56
def n_plus_one():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    
    start_time = time.time()
    query_count = 0
    cursor.execute("SELECT * FROM certifications;")
    certifications = cursor.fetchall()
    query_count += 1
    
    for i in certifications:
        cursor.execute(f"SELECT first_name, last_name FROM employees WHERE employee_id = {i['employee_id']};")
        student = cursor.fetchone()
        query_count += 1
        
    end_time = time.time()
    print("N+1:")
    print("Total Queries Executed:", query_count)
    print(f"Execution Time: {end_time - start_time:.4f} seconds\n")
    
    cursor.close()
    conn.close()

# task 57
def resolve_with_join():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    
    start_time = time.time()
    query_count = 0
    
    optimized_query = """
        SELECT c.*, e.first_name, e.last_name 
        FROM certifications c
        JOIN employees e ON c.employee_id = e.employee_id;
    """
    cursor.execute(optimized_query)
    results = cursor.fetchall()
    query_count += 1
    
    end_time = time.time()
    print("Single join")
    print("Total Queries Executed:", query_count)
    print(f"Execution Time: {end_time - start_time:.4f} seconds\n")
    
    cursor.close()
    conn.close()

if __name__ == "__main__":
    n_plus_one()
    resolve_with_join()