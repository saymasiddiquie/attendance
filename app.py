from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    class_name = db.Column(db.String(20), nullable=False)
    attendance = db.relationship('Attendance', backref='student', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)

# Create database tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mark_attendance', methods=['GET', 'POST'])
def mark_attendance():
    if request.method == 'POST':
        roll_number = request.form.get('roll_number')
        student = Student.query.filter_by(roll_number=roll_number).first()
        if student:
            # Mark attendance
            today = datetime.utcnow().date()
            attendance = Attendance.query.filter_by(student_id=student.id, date=today).first()
            if not attendance:
                attendance = Attendance(student_id=student.id, status=True)
                db.session.add(attendance)
                db.session.commit()
                flash(f'Attendance marked for {student.name}', 'success')
            else:
                flash('Attendance already marked for today', 'info')
        else:
            flash('Student not found', 'danger')
        return redirect(url_for('mark_attendance'))
    return render_template('mark_attendance.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        roll_number = request.form.get('roll_number')
        class_name = request.form.get('class_name')
        
        if not all([name, roll_number, class_name]):
            flash('All fields are required', 'danger')
        else:
            student = Student(name=name, roll_number=roll_number, class_name=class_name)
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully', 'success')
            return redirect(url_for('add_student'))
    return render_template('add_student.html')

if __name__ == '__main__':
    app.run(debug=True)