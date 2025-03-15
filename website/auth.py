from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint("auth",__name__)

@auth.route("/")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
    
    return render_template("/login.html")

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

        # Basic validation
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for("auth.sign_up"))

        # Here, you can store the data in a database
        flash("Signup successful! You can now log in.", "success")
        return redirect(url_for("views.home"))

    return render_template("/signup.html")

@auth.route("/logout")
def log_out():
    return redirect(url_for("/login.html"))