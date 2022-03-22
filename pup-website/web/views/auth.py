from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Student, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from datetime import date

auth = Blueprint('views/auth', __name__)

@auth.route('/log-in', methods=['GET', 'POST'])
def log_in():
    user_type = session['user_type']

    if request.method == 'POST':
        # Query user existence
        if user_type == 'student':
            stud_num = request.form.get('student-num')
            user = Student.query.filter_by(stud_num=stud_num.upper()).first()
        else:
            admin_num = request.form.get('admin-num')
            user = Admin.query.filter_by(admin_num=admin_num.upper()).first()
        
        password = request.form.get('password')

        if user:
            # Verify Password
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)

                return redirect(url_for('views/views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Account does not exist.', category='error')

    return render_template('login.html', user=current_user, user_type=user_type)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    user_type = session['user_type']

    if request.method == 'POST':
        fname = request.form.get('fname')
        mname = request.form.get('mname')
        lname = request.form.get('lname')
        address = request.form.get('address')
        sex = request.form.get('sex')
        email = request.form.get('email')
        birthday = date.fromisoformat(request.form.get('birthday'))
    
        if user_type == 'student':
            stud_num = request.form.get('student-num')
            department = request.form.get('department')
            section = request.form.get('section')
        else:
            admin_num = request.form.get('admin-num')

        password = request.form.get('password')
        pass_confirmation = request.form.get('confirmpass')

        # Calculate age
        def calc_age(birthday):
            today = date.today()
            return (today.year - birthday.year) - ((today.month, today.day) < (birthday.month, birthday.day))
        
        # Check if student number already exists
        def check_existence(field, user_type):
            if user_type == 'student':
                if field == 'id_num':
                    return Student.query.filter_by(stud_num=stud_num).first()
                elif field == 'email':
                    return Student.query.filter_by(email=email).first()
            else:
                if field == 'id_num':
                    return Admin.query.filter_by(admin_num=admin_num).first()
                elif field == 'email':
                    return Admin.query.filter_by(email=email).first()
        
        # Check if stud_num or admin_num exists
        if check_existence('id_num', user_type):
            if user_type == 'student':
                flash('Student number already in use.', category='error')
            else:
                flash('Admin number already in use.', category='error')

        # Check if email is already in use
        elif check_existence('email', user_type):
            if user_type == 'student':
                flash('Email is already been used by another student. Use other emails.', category='error')
            else:
                flash('Email is already been used by another admin. Use other emails.', category='error')
        
        # Check if password is too short
        elif len(password) < 4:
            flash('Password is too short. Must have a strong password.', category='error')
        
        # Check if password = password confirmation
        elif password != pass_confirmation:
            flash('Passwords do not match.', category='error')

        # Finally create a new record and login the new user
        else:
            if user_type =='student':
                new_user = Student(
                    stud_num=stud_num.strip().upper(),
                    section=section,
                    department=department,
                    fname=fname.strip(),
                    mname=mname.strip(),
                    lname=lname.strip(),
                    address=address.strip(),
                    age=calc_age(birthday),
                    sex=sex,
                    email=email.strip(),
                    birthday=birthday,
                    password=generate_password_hash(password, method='sha256')
                )
            else:
                new_user = Admin(
                    admin_num=admin_num,
                    fname=fname,
                    mname=mname,
                    lname=lname,
                    address=address,
                    age=calc_age(birthday),
                    sex=sex,
                    email=email,
                    birthday=birthday,
                    password=generate_password_hash(password, method='sha256')
                )
            try:
                # Insert to database
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account has been created!', category='success')
                
                return redirect(url_for('views/views.home'))
            except:
                flash('There was an error creating your account', category='error')

    return render_template('signup.html', user=current_user, user_type=user_type)

@auth.route('/log-out')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('views/views.index'))