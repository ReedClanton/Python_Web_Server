## External Import(s) ##
from flask import Blueprint, render_template

## Internal Import(s) ##
from . import db

# TODO: Comment.
auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    return render_template("signup.html")

@auth.route("/login")
def login():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    return render_template("login.html")

@auth.route("/logout")
def logout():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    return render_template("logout.html")
