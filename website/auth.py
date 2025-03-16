from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import db, login_manager, User


auth = Blueprint("auth", __name__)

@auth.route("/")
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("views.map"))
        else:
            flash("Invalid email or password", "error")

    return render_template("login.html")

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for("auth.sign_up"))

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered!", "error")
            return redirect(url_for("auth.sign_up"))

        user = User(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            gender=gender,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()

        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for("views.map"))

    return render_template("signup.html")

@auth.route("/logout")
@login_required
def log_out():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("/login.html"))
