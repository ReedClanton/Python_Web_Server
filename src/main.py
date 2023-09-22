## External Import(s) ##
from flask import Blueprint, render_template

## Internal Import(s) ##
from . import db

# TODO: Comment.
main = Blueprint("main", __name__)

@main.route("/")
def index():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    return render_template("index.html")

@main.route("/profile")
def profile():
    '''
    TODO

    :return: TODO
    :rtype: TODO
    '''
    return render_template("profile.html")
