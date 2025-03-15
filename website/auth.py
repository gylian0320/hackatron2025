from flask import Blueprint, render_template,redirect, url_for, request, flash
# from . import db
# from flask_login import login_user, logout_user, login_required, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from .member import Member

auth = Blueprint("auth",__name__)

@auth.route("/")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("/login.html")

@auth.route("/signup_page", methods=["GET", "POST"])
def signup():
    return render_template("/signup.html")

@auth.route("/logout")
def log_out():
    return redirect(url_for("/login.html"))