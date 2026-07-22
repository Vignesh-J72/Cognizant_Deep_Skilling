from flask import Flask, jsonify, request
import sqlite3

app=Flask(__name__)
DB_FILE="courses.db"

def init_db():
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_name TEXT NOT NULL,
            module_code TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/courses/', methods=['POST'])
def create_course():
    data=request.get_json() or {}
    name=data.get("module_name")
    code=data.get("module_code")
    if not name or not code:
        return jsonify({"error": "Missing fields"}), 400
    try:
        conn=sqlite3.connect(DB_FILE)
        cursor=conn.cursor()
        cursor.execute('INSERT INTO courses (module_name, module_code) VALUES (?, ?)', (name, code))
        course_id=cursor.lastrowid
        conn.commit()
        conn.close()
        return jsonify({"id": course_id, "module_name": name, "module_code": code}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Course code already exists"}), 409

@app.route('/api/courses/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    conn=sqlite3.connect(DB_FILE)
    cursor=conn.cursor()
    cursor.execute('SELECT id, module_name, module_code FROM courses WHERE id=?', (course_id,))
    row=cursor.fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "Course not found"}), 404
    return jsonify({"id": row[0], "module_name": row[1], "module_code": row[2]}), 200

if __name__=='__main__':
    init_db()
    app.run(port=5001, debug=True)