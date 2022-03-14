from flask import Blueprint, render_template

auth = Blueprint('views/auth', __name__)

@auth.route('/log-in', methods=['GET', 'POST'])
def log_in():
    return render_template('login.html', bg_image="login")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template('signup.html', bg_image="signup")

@auth.route('/log-out')
def log_out():
    return "<h3>Logged-out</h3>"