from flask import Flask, request, redirect, session
import hashlib
from replit import db

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    page = ""

    with open("templates/index.html", "r") as f:
        page = f.read()

    return page


@app.route("/signup")
def signup_page():
    page = ""

    with open("templates/signup.html", "r") as f:
        page = f.read()

    return page


@app.route("/signup", methods=["POST"])
def signup():
    form = request.form

    keys = db.prefix("user")
    keys = keys[0:4]

    if form["user"] in keys:
        return redirect("/login")
    else:
        key = f"user{form['user']}"
        password = hashlib.sha256(form["password"].encode("utf-8")).hexdigest()

        db[key] = {"name": form["name"], "password": password}


@app.route("/login")
def login_page():
    page = ""

    with open("templates/login.html", "r") as f:
        page = f.read()

    return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    keys = db.prefix("user")
    keys = keys[0:4]

    if form["user"] not in keys:
        return redirect("/signup")
    else:
        form_pass = form["password"]
        form_pass = hashlib.sha256(form_pass.encode("utf-8")).hexdigest()
        form_user = form["user"]

        if form_user == form["user"] and form_pass == form["password"]:
            session["username"] = form_user
            return redirect("/home")
        else:
            return redirect("/login")


@app.route("/home")
def home_page():
    page = ""

    with open("templates/home.html", "r") as f:
        page = f.read()

    return page


@app.route("/home", methods=["POST"])
def home_system():
    pass


app.run(host="0.0.0.0", port=81)
