from . import db
from flask_login import UserMixin

class student(db.Model, UserMixin):
    stud_num = db.Column(db.String(15), primary_key=True)
    section = db.Column(db.String(4))
    department = db.Column(db.String(4))
    is_enrolled = db.Column(db.String(3), default="no")
    no_of_subjs = db.Column(db.Integer, default=0)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    address = db.Column(db.String(200))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(11))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.DateTime(timezone=True))
    password = db.Column(db.String(150))

class admin(db.Model, UserMixin):
    admin_num = db.Column(db.String(3), primary_key=True)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    address = db.Column(db.String(120))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(11))
    email = db.Column(db.String(120), unique=True)
    birthday = db.Column(db.DateTime(timezone=True))
    password = db.Column(db.String(50))
