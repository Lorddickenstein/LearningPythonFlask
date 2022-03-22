from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from os import path
from datetime import date

db = SQLAlchemy()
DB_NAME = 'pupWebsiteDB.db'

def create_app():
    app = Flask(__name__)
    # Encrypts/secure the cookies and session data related to the website
    app.config['SECRET_KEY'] = 'aihai alkhfq'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from web.views.views import views
    from web.views.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Student, Admin, Department, Schedule, Subject

    # Populate Department, Subjects, Students (Initial Records)
    def populate_tables():
        from utils import read_files

        # Departments
        departments = read_files(file_name='departments.txt')
        for dep in departments:
            new_dep = Department(
                dep_id=dep.get('dep_id'),
                description=dep.get('description')
            )
            try:
                with app.app_context():
                    db.session.add(new_dep)
                    db.session.commit()
            except Exception as exc:
                print(exc)
                print('### There is an error adding department records. ###')
        
        # Subjects
        subjects = read_files(file_name='subjects.txt')
        for sub in subjects:
            new_sub = Subject(
                sub_code=sub.get('sub_code'),
                year_level=int(sub.get('year_level')),
                description=sub.get('description'),
                units=int(sub.get('units'))
            )
            try:
                with app.app_context():
                    db.session.add(new_sub)
                    db.session.commit()
            except Exception as exc:
                print(exc)
                print('### There is an error adding subject records. ###')

        # Students
        students = read_files(file_name='students.txt')
        for stud in students:
            new_stud = Student(
                stud_num=stud.get('stud_num'),
                section=stud.get('section'),
                department=stud.get('department'),
                is_enrolled=stud.get('is_enrolled'),
                no_of_subjs=int(stud.get('no_of_subs')),
                fname=stud.get('fname'),
                mname=stud.get('mname'),
                lname=stud.get('lname'),
                address=stud.get('address'),
                age=int(stud.get('age')),
                sex=stud.get('sex'),
                email=stud.get('email'),
                birthday=date.fromisoformat(stud.get('birthday')),
                password=generate_password_hash(stud.get('password'), method='sha256'),
            )
            try:
                with app.app_context():
                    db.session.add(new_stud)
                    db.session.commit()
            except Exception as exc:
                print(exc)
                print('### There is an error adding student records. ###')
        
        # Admins
        admins = read_files(file_name='admins.txt')
        for admin in admins:
            new_admin = Admin(
                admin_num=admin.get('admin_num'),
                fname=admin.get('fname'),
                mname=admin.get('mname'),
                lname=admin.get('lname'),
                address=admin.get('address'),
                age=int(admin.get('age')),
                sex=admin.get('sex'),
                email=admin.get('email'),
                birthday=date.fromisoformat(admin.get('birthday')),
                password=generate_password_hash(admin.get('password'), method='sha256')
            )
            try:
                with app.app_context():
                    db.session.add(new_admin)
                    db.session.commit()
            except Exception as exc:
                print(exc)
                print('### There is an error adding admin records. ###')


    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        populate_tables()
        print('### Created a database! ###')

    login_manager = LoginManager()
    login_manager.login_view = 'views/views.index'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_num):
        # return Student.query.get(id_num)
        user_type = session['user_type']
        if user_type == 'student':
            return Student.query.get(id_num)
        
        return Admin.query.get(id_num)

    return app
