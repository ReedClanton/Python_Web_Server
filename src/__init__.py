## External Import(s) ##
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## Internal Import(s) ##
# NoOp

# Initialize DB so it may be utilized in module(s).
db = SQLAlchemy()

def create_app():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    # Create instance of application.
    app = Flask(__name__)

    # Initial app configuration.
    app.config["SECRET_KEY"] = "secret-key-goes-here"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    # Initialize DB with application.
    db.init_app(app)

    # Blueprint of app's authentication route(s).
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint of app's non-authenticated route(s).
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # TODO: Comment.
    from .modules.User import User
    with app.app_context():
        db.create_all()

    return app
