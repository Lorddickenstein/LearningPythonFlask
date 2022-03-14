from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

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

    from .models import student, admin

    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print('Created a database!')

    return app
