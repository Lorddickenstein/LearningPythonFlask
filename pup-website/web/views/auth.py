from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import student, admin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db

auth = Blueprint('views/auth', __name__)

@auth.route('/log-in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        student_num = request.form.get('student-num')
        password = request.form.get('password')
    return render_template('login.html', bg_image="login")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        fname = request.form.get('fname')
        mname = request.form.get('mname')
        lname = request.form.get('lname')
        address = request.form.get('address')
        age = request.form.get('age')
        age = 22
        sex = request.form.get('sex')
        email = request.form.get('email')
        birthday = request.form.get('birthday')
        stud_num = request.form.get('student-num')
        department = request.form.get('department')
        section = request.form.get('section')
        password = request.form.get('password')
        pass_confirmation = request.form.get('confirmpass')
        
        if len(password) < 4:
            flash('Password is too short. Must have a strong password.', category='error')
        elif password != pass_confirmation:
            flash('Passwords do not match.', category='error')
        else:
            flash('Account has been created!', category='success')
            new_user = student(stud_num=stud_num, section=section, department=department, fname=fname, mname=mname, lname=lname, address=address, age=age, sex=sex, email=email, birthday=birthday, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('views.views.home'))

    return render_template('signup.html', bg_image="signup")

@auth.route('/log-out')
def log_out():
    return "<h3>Logged-out</h3>"