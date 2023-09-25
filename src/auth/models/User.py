## External Import(s) ##
from flask_login import UserMixin

## Internal Import(s) ##
from ..db import auth_db

class User(UserMixin, auth_db.Model):
    '''Model of user accounts.'''

    id = auth_db.Column(auth_db.Integer, primary_key=True)
    '''Primary key associated with these objects.'''
    email = auth_db.Column(auth_db.String(1000), unique=True)
    '''Email address associated with user.'''
    password = auth_db.Column(auth_db.String(1000))
    '''Tracks hashed password.'''
    full_name = auth_db.Column(auth_db.String(1500))
    '''Stores user's full name.'''
