from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from . import db


views = Blueprint("views", __name__)

@views.route("/home")
def home():
    return render_template("/home.html")

@views.route("/todo_list")
def todo_list():
    return render_template("/todo_list.html")

@views.route("/map")
def map():
    return render_template("/map.html")

@views.route("/profile_page")
def profile_page():
    return render_template(
        "/profile_page.html",
        first_name = current_user.first_name,
        last_name = current_user.last_name,
        birthday = current_user.birthday,
        gender = current_user.gender,
        email = current_user.email
        )

@views.route("/update_profile", methods=["GET", "POST"])
def update_profile():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        email = request.form.get("email")
        
        # Update the current user's data
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.birthday = birthday
        current_user.gender = gender
        current_user.email = email
        
        db.session.commit()
        
        return redirect(url_for("views.profile_page"))

    return render_template(
        "/update_profile.html",
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        birthday=current_user.birthday,
        gender=current_user.gender,
        email=current_user.email
    )
