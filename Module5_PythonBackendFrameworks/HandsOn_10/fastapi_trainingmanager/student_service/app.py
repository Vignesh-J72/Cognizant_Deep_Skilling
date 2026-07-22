from flask import Flask, jsonify, request
import sqlite3
import requests

app=Flask(__name__)
DB_FILE="students.db"
COURSE_SERVICE_URL="http://localhost:5001/api/courses/"

def init_db():
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/students/', methods=['POST'])
def create_student():
    data=request.get_json() or {}
    name=data.get("full_name")
    if not name:
        return jsonify({"error": "Missing full_name"}), 400
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute('INSERT INTO students (full_name) VALUES (?)', (name,))
    student_id=cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"id": student_id, "full_name": name}), 201

@app.route('/api/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    data=request.get_json() or {}
    course_id=data.get("course_id")
    if not course_id:
        return jsonify({"error": "Missing course_id"}), 400
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute('SELECT id FROM students WHERE id=?', (student_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"error": "Student not found"}), 404
    try:
        response=requests.get(f"{COURSE_SERVICE_URL}{course_id}/", timeout=3)
        if response.status_code==404:
            conn.close()
            return jsonify({"error": "Target course does not exist"}), 404
        elif response.status_code!=200:
            conn.close()
            return jsonify({"error": "Failed to verify course"}), 502
    except requests.exceptions.ConnectionError:
        conn.close()
        return jsonify({"error": "Course Service unavailable"}), 503
    cursor.execute('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Enrollment successful"}), 201

if __name__=='__main__':
    init_db()
    app.run(port=5002, debug=True)