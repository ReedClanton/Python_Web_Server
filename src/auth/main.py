## External Import(s) ##
from flask import Blueprint, render_template
from flask_login import login_required, current_user

## Internal Import(s) ##
# NoOp

main = Blueprint("main", __name__)

@main.route("/")
def index():
    '''
    Returns index page's HTML.

    :return: HTML of page.
    :rtype: str
    '''
    return render_template("index.html")

@main.route("/profile")
@login_required
def profile() -> str:
    '''
    Returns profile page's HTML.

    :return: HTML of page.
    :rtype: str
    '''
    return render_template("profile.html", full_name=current_user.full_name)

