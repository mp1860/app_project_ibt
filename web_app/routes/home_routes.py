
from flask import Blueprint, request, render_template, url_for, flash, redirect, current_app, session, request
from web_app.services.gsheets import push_to_sheets

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> can be empty like {} or full of params like {"name":"Harper"}

    # compile message using specified "name" url parameter or a default value:
    name = url_params.get("name") or "Guest"
    message = f"Hello, {name}!"
    return render_template("home.html",message=message)

@home_routes.route("/overview")
def overview():
    print("OVERVIEW...")
    return render_template("overview.html")

@home_routes.route("/history")
def history():
    print("HISTORY...")
    return render_template("history.html")

@home_routes.route("/coins", methods=('GET','POST'))
def contact():
    print("COINS...")
    if request.method == 'POST':
        form_data = dict(request.form)
        push_to_sheets(form_data["title"],form_data["content"])
    return render_template("coins.html")
