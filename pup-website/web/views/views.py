from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_login import login_required, current_user

views = Blueprint('views/views', __name__)

@views.route('/', methods=['GET', 'POST'])
@views.route('/index', methods=['GET', 'POST'])
def index():
    session['user_type'] = 'none'
    
    if request.method == 'POST':
        btn_student = request.form.get('btnStudent')
        btn_admin = request.form.get('btnAdmin')
        if btn_student:
            session['user_type'] = 'student'
        elif btn_admin:
            session['user_type'] = 'admin'

        print('### ' + session['user_type'] + ' ####')

        return redirect(url_for('views/auth.log_in', type=type))

    return render_template('index.html', user=current_user)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    user_type = session['user_type']
    return render_template('home.html', user=current_user, user_type=user_type)

@views.route('/grades', methods=['GET', 'POST'])
@login_required
def grades():
    user_type = session['user_type']
    return render_template('grades.html', user=current_user, user_type=user_type)

@views.route('/enrollment', methods=['GET', 'POST'])
@login_required
def enrollment():
    user_type = session['user_type']
    return render_template('enrollment.html', user=current_user, user_type=user_type)

@views.route('/schedule', methods=['GET', 'POST'])
@login_required
def schedule():
    user_type = session['user_type']
    return render_template('schedule.html', user=current_user, user_type=user_type)

@views.route('/students-list', methods=['GET', 'POST'])
@login_required
def students_list():
    user_type = session['user_type']
    return render_template('students_list.html', user=current_user, user_type=user_type)