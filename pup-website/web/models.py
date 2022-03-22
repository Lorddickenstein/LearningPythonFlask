from . import db
from flask_login import UserMixin

class Student(db.Model, UserMixin):
    stud_num = db.Column(db.String(15), primary_key=True)
    section = db.Column(db.String(4))
    department = db.Column(db.String(4))
    is_enrolled = db.Column(db.String(3), default="No")
    no_of_subjs = db.Column(db.Integer, default=0)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    address = db.Column(db.String(200))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(11))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.Date)
    password = db.Column(db.String(150))
    grades = db.relationship('Grades')

    def get_id(self):
        # Overwrite login_user get_id(id)
        return (self.stud_num)


class Admin(db.Model, UserMixin):
    admin_num = db.Column(db.String(15), primary_key=True)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    address = db.Column(db.String(120))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(11))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.Date)
    password = db.Column(db.String(50))
    grades = db.relationship('Grades')

    def get_id(self):
        return (self.admin_num)


class Department(db.Model):
    dep_id = db.Column(db.String(10), primary_key=True)
    description = db.Column(db.String(120))
    
    def get_id(self):
        return self.dep_id


class Subject(db.Model):
    sub_code = db.Column(db.String(10), primary_key=True)
    year_level = db.Column(db.Integer, default=0)
    description = db.Column(db.String(120))
    units = db.Column(db.Integer)
    grades = db.relationship('Grades')

    def get_id(self):
        return (self.sub_code)


class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stud_num = db.Column(db.String(15), db.ForeignKey('student.stud_num'))
    sub_code = db.Column(db.String(10), db.ForeignKey('subject.sub_code'))
    admin_num = db.Column(db.String(15), db.ForeignKey('admin.admin_num'))
    final_grade = db.Column(db.Float(precision=3, asdecimal=True, decimal_return_scale=2), default=0.0)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stud_num = db.Column(db.String(15), db.ForeignKey('student.stud_num'))
    day_sched = db.Column(db.String(10))
    time_sched = db.Column(db.String(120))
    admin_num = db.Column(db.String(15), db.ForeignKey('admin.admin_num'))