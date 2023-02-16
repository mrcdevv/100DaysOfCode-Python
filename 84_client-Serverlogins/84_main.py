from flask import Flask, request, redirect
from replit import db

app = Flask(__name__)


@app.route("/")
def index():
    page = ""

    f = open("templates/index.html", "r")
    page = f.read()
    f.close()

    return page


@app.route("/signup")
def signupPage():
    page = ""

    f = open("templates/signup.html", "r")
    page = f.read()
    f.close()

    return page


@app.route("/signup", methods=["POST"])
def signUp():
    form = request.form

    if form["user"] not in db.keys():
        db[form["username"]] = {
            "name": form["name"], "password": form["password"]}
        return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/login")
def loginPage():
    page = ""

    f = open("templates/login.html", "r")
    page = f.read()
    f.close()

    return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    try:
        if form["user"] in db.keys():
            if form["password"] == db[form["user"]["password"]]:
                return f"Welcome {db[form['user']]['name']}"
            else:
                return redirect("/login")
        else:
            return redirect("/signup")
    except:
        return redirect("/signup")


app.run(host="0.0.0.0", port=81)
