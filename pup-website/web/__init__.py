from flask import Flask

def create_app():
    app = Flask(__name__)
    # Encrypts/secure the cookies and session data related to the website
    app.config['SECRET_KEY'] = 'aihai alkhfq'

    from web.views.views import views
    from web.views.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
