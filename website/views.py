from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint("views",__name__)

@views.route("/home")
def home():
    return "Home"

@views.route("/")
@views.route("/signup_page", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for("views.signup"))

        # Here, you can store the data in a database
        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for("views.home"))

    return render_template("/signup.html")
