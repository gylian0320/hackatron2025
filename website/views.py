from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint("views",__name__)

@views.route("/todo_list")
def todo_list():
    return render_template("/todo_list.html")
