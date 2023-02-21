from flask import Flask, request, redirect, session
import hashlib
from replit import db
import mrcdb
import datetime


app = Flask(__name__, static_url_path="/static")
app.secret_key = "JKLjslDÑKJJKljlkvjkDFJKlnhjkldlkfñjKDCkclsJKLAjxnk"


try:
    db_users = mrcdb.CSV_to_2Ddict("users.csv", "user")
    db_posts = mrcdb.CSV_to_2Ddict("messages.csv", "timestamp")
except:
    db_users = {}
    db_posts = {}


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

    print(db_users.keys())
    if form["user"] in db_users.keys():
        return redirect("/login")
    else:
        key = form['user']
        password = hashlib.sha256(form["password"].encode("utf-8")).hexdigest()

        db_users[key] = {"name": form["name"], "password": password}
        mrcdb.dict2D_to_CSV("users.csv", "user", db_users)
        return redirect("/")


@app.route("/login")
def login_page():
    page = ""

    with open("templates/login.html", "r") as f:
        page = f.read()

    return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    print("ESTOY EN EL LOGIN")
    if form["user"] in db_users.keys():
        print("ESTOY ENTRE LAS KEYS")
        form_pass = form["password"]
        form_pass = hashlib.sha256(form_pass.encode("utf-8")).hexdigest()
        form_user = form["user"]

        print(form_pass)
        for key in db_users.keys():
            print()
            print(key)
            db_users.keys()
            if form_user == key and form_pass == db_users[key]["password"]:
                print("HAY COINCIDENCIA")
                session["username"] = form_user
                return redirect("/home")

        return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/home", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        form = request.form
        timestamp = datetime.datetime.now().timestamp()

        db_posts[timestamp] = {
            "user": session["username"], "message": form["message"]}
        mrcdb.dict2D_to_CSV("messages.csv", "timestamp", db_posts)

    home = ""
    with open("templates/home.html", "r") as f:
        home = f.read()

    home = home.replace("{name}", session["username"])

    keys = list(db_posts.keys())
    keys.reverse()
    counter = 0

    if keys != []:
        post = ""
        for key in keys:
            if counter == 5:
                break

            with open("templates/post.html", "r") as f:
                post += f.read()

            post = post.replace("{name}", db_posts[key]["user"])
            post = post.replace("{date}", str(key))
            post = post.replace("{message}", db_posts[key]["message"])
            counter += 1

        home = home.replace("{content}", post)
        return home

    else:
        home = home.replace("{content}", "")
        return home


@app.route("/logout")
def log():
    session.clear()
    return redirect("/")


app.run(host="0.0.0.0", port=81)


@app.route("/home", methods=["POST"])
def home_system():
    if session.get("username"):
        if session.get("username") == "mrcdev":
            pass
            # TAMBIEN TIENE QUE AGREGAR EL POST A LA BASE DE DATOS
        else:
            form = request.form
            timestamp = datetime.datetime.now().timestamp()

            db_posts[timestamp] = {"user": session["username"],
                                   "message": form["message"]}
            mrcdb.dict2D_to_CSV("messages.csv", "timestamp", db_posts)

    # Show post
    # Get the home template
    home = ""
    with open("templates/home.html", "r") as f:
        home = f.read()

    home = home.replace("{name}", session["username"])

    print(db_posts.keys())

    keys = list(db_posts.keys())
    keys.reverse()
    counter = 0

    print(keys)
    if keys != []:
        for key in keys:
            if counter == 5:
                break

            post = ""
            with open("templates/post.html", "r") as f:
                post += f.read()

            post = post.replace("{name}", db_posts[key]["user"])
            post = post.replace("{date}", str(key))
            post = post.replace("{message}", db_posts[key]["message"])
            counter += 1

        home = home.replace("{content}", post)
        return home

    else:
        home = home.replace("{content}", "")
        return home
