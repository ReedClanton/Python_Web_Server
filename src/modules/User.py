## External Import(s) ##
# NoOp

## Internal Import(s) ##
from .. import db

class User(db.Model):
    '''TODO'''
    id = db.Column(db.Integer, primary_key=True)
    '''Primary key associated with these objects.'''
    email = db.Column(db.String(100), unique=True)
    '''Email address associated with user.'''
    password = db.Column(db.String(100))
    '''TODO: Comment/make more secure.'''
    first_name = db.Column(db.String(500))
    '''First name of user.'''
    middle_name = db.Column(db.String(500))
    '''Middle name of user.'''
    last_name = db.Column(db.String(500))
    '''Last name of user.'''
