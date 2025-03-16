from flask import Blueprint, render_template

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