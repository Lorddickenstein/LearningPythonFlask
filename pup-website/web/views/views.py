from flask import Blueprint, render_template

views = Blueprint('views/views', __name__)

@views.route('/index', methods=['GET'])
def index():
    return '<h1>This is the index</h1>'

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', bg_image="home")

@views.route('/grades', methods=['GET', 'POST'])
def grades():
    return render_template('grades.html', bg_image="grades")

@views.route('/enrollment', methods=['GET', 'POST'])
def enroll():
    return render_template('enrollment.html', bg_image="enrollment")

@views.route('/schedule', methods=['GET', 'POST'])
def schedule():
    return render_template('schedule.html', bg_image="enrollment")