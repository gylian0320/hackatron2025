from flask import Blueprint, render_template

views = Blueprint("views",__name__)

@views.route("/home")
def home():
    return "Home"

@views.route("/")
@views.route("/signup_page")
def signup():
    return render_template("/signup.html")

