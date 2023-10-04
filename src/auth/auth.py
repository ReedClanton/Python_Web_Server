## External Import(s) ##
from flask import Blueprint, render_template, redirect, url_for, request, flash, Response
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

## Internal Import(s) ##
from .db import auth_db
from .models.User import User

auth = Blueprint("auth", __name__)

@auth.route("/signup")
def signup() -> str:
	'''
	Returns signup page's HTML

	:return: HTML of page.
	:rtype: str
	'''
	return render_template("signup.html")

@auth.route("/signup", methods=["POST"])
def signup_post() -> Response:
	'''
	Handles signup post request and responds to it.

	:return: Response to signup attempt.
	:rtype: :py:obj:`flask.Response`
	'''
	# Read new user data from post.
	email = request.form.get("email")
	full_name = request.form.get("full_name")
	password = request.form.get("password")

	# Ensure duplicate user isn't added.
	if not User.query.filter_by(email=email).first():
		# Generate new user db entry.
		new_user = User(
			email=email,
			full_name=full_name,
			password=generate_password_hash(password, method="sha256")
		)
		# Add db entry.
		auth_db.session.add(new_user)
		auth_db.session.commit()

		return redirect(url_for("auth.login"))

	flash("Account already exists, try again.")
	return redirect(url_for("auth.signup"))

@auth.route("/login")
def login() -> str:
	'''
	Returns login page's HTML.

	:return: HTML of page.
	:rtype: str
	'''
	return render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post() -> Response:
	'''
	Handles login post request and responds to it.

	:return: Response to login attempt.
	:rtype: :py:obj:`flask.Response`
	'''
	# Read login data from post.
	email = request.form.get("email")
	password = request.form.get("password")
	remember = True if request.form.get("remember") else False

	# Use provided data to find and login user.
	user = User.query.filter_by(email=email).first()
	if user and check_password_hash(user.password, password):
		login_user(user, remember=remember)
		return redirect(url_for("main.profile"))

	flash("Check credentials and try again.")
	return redirect(url_for("auth.login"))

@auth.route("/logout")
@login_required
def logout() -> str:
	'''
	Returns logout page's HTML

	:return: HTML of page.
	:rtype: str
	'''
	logout_user()
	return redirect(url_for("main.index"))

@auth.route("/delete", methods=["POST"])
@login_required
def delete() -> str:
	'''
	Returns HTML of page user is directed to post account deletion.

	:return: HTML of page.
	:rtype: str
    '''
	current_user.delete()
	auth_db.session.commit()
	flash("Your account has been deleted.")
	return redirect(url_for("main.index"))

