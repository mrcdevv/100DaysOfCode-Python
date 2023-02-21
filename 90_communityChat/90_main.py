from flask import Flask, request, redirect, session
import hashlib
from replit import db
import mrcdb
import datetime


app = Flask(__name__, static_url_path="/static")
app.secret_key = "JKLjslDÑKJJKljlkvjkDFJKlnhjkldlkfñjKDCkclsJKLAjxnk"

# Load the dictionaries with data
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
    if session.get("username"):
        return redirect("/home")
    else:
        page = ""
        with open("templates/signup.html", "r") as f:
            page = f.read()
        return page


@app.route("/signup", methods=["POST"])
def signup():
    form = request.form

    if form["user"] in db_users.keys():
        return redirect("/login")
    else:
        key = form['user']
        password = hashlib.sha256(form["password"].encode("utf-8")).hexdigest()

        # Add a new user in the dictionary and then in the CSV
        db_users[key] = {"name": form["name"], "password": password}
        mrcdb.dict2D_to_CSV("users.csv", "user", db_users)
        return redirect("/")


@app.route("/login")
def login_page():
    if session.get("username"):
        return redirect("/home")
    else:
        page = ""
        with open("templates/login.html", "r") as f:
            page = f.read()
        return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    if form["user"] in db_users.keys():
        form_pass = form["password"]
        form_pass = hashlib.sha256(form_pass.encode("utf-8")).hexdigest()
        form_user = form["user"]

        for key in db_users.keys():
            # Check for credentials
            if form_user == key and form_pass == db_users[key]["password"]:
                session["username"] = form_user
                return redirect("/home")

        return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/home", methods=["GET", "POST"])
def home_page():
    if session.get("username"):
        if request.method == "POST":
            form = request.form
            timestamp = datetime.datetime.now().timestamp()
            # Add a new message in the dictionary and then in the CSV
            db_posts[timestamp] = {
                "user": session["username"], "message": form["message"]}
            mrcdb.dict2D_to_CSV("messages.csv", "timestamp", db_posts)

        home = ""
        with open("templates/home.html", "r") as f:
            home = f.read()

        keys = list(db_posts.keys())
        keys.reverse()
        counter = 0

        if keys != []:
            post = ""
            for key in keys:
                # Show only the last 5 messages
                if counter == 5:
                    break

                with open("templates/post.html", "r") as f:
                    post += f.read()

                post = post.replace("{name}", db_posts[key]["user"])
                post = post.replace("{date}", str(key))
                post = post.replace("{message}", db_posts[key]["message"])

                # If the admin is loged in, add the option to delete messages
                if session["username"] == "admin":
                    post = post.replace(
                        "{admin}", f" <a href='/remove?post={str(key)}'>❌</a>")
                else:
                    post = post.replace("{admin}", "")

                counter += 1

            home = home.replace("{content}", post)
            return home

        else:
            home = home.replace("{content}", "")
            return home

    else:
        return redirect("/login")


@app.route("/logout")
def log():
    session.clear()
    return redirect("/")


@app.route("/remove", methods=["GET"])
def remove_message():
    if session.get("username") == "admin":
        timestamp = request.args.get("post")
        db_posts.pop(timestamp)
        mrcdb.dict2D_to_CSV("messages.csv", "timestamp", db_posts)
        return redirect("/home")
    else:
        return redirect("/home")


app.run(host="0.0.0.0", port=81)
