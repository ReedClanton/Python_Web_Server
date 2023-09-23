## External Import(s) ##
from os.path import abspath, dirname, join
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

## Internal Import(s) ##
from .db import auth_db


def create_app():
    '''
    Called by Flask to create an instance of this application.

    :return: Instance of this application.
    :rtype: :py:obj:`flask.Flask`
    '''
    # Create instance of application.
    auth_app = Flask(__name__)

    # Initial DB configuration.
    auth_app.config["SECRET_KEY"] = "some-secret-key"
    auth_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{join(abspath(dirname(__file__)), 'database.db')}"

    # Initialize DB with application.
    auth_db.init_app(auth_app)

    # Blueprint of app's authentication route(s).
    from .auth import auth as auth_blueprint
    auth_app.register_blueprint(auth_blueprint)

    # Blueprint of app's non-authenticated route(s).
    from .main import main as main_blueprint
    auth_app.register_blueprint(main_blueprint)

    # Locally import modules to prevent circular references.
    from .models.User import User

    # Create db based on module(s).
    with auth_app.app_context():
        auth_db.create_all()

    # Let Flask extention handle login process.
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(auth_app)

    @login_manager.user_loader
    def load_user(user_id: str) -> User:
        '''
        Flask callback for loading user associated with provided user ID.

        :param user_id: ID (primary key) of user caller would like to get instance of.
        :type user_id: str
        :return: User associated with provided value.
        :rtype: :py:obj:`models.User.User`
        '''
        return User.query.get(int(user_id))

    return auth_app

