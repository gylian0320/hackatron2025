from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from . import db
from flask_login import login_user, login_required, logout_user
from .todo import get_current_user_tasks

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home():
    return render_template("/home.html")

@views.route("/todo_list")
@login_required
def todo_list():
    return render_template("/todo_list.html", tasks = get_current_user_tasks(current_user.id))

@views.route("/map")
@login_required
def map():
    return render_template("/map.html")

@views.route("/profile_page")
@login_required
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
@login_required
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
