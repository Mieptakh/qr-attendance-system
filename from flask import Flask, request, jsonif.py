from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    student_id = request.json.get('student_id')
    date = request.json.get('date')
    status = request.json.get('status')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)", (student_id, date, status))
    conn.commit()
    conn.close()

    return jsonify({"message": "Attendance marked successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
