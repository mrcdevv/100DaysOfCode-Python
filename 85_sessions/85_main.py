# Day 85 on Replit: "HTTP & Sessions"

# Challenge section
from flask import Flask, request, redirect, session
import mrcdb
import random
import os
import hashlib

# Load the dictionary with the db data or create an empty dictionary
try:
    absFilePath = os.path.abspath(__file__)
    path, filename = os.path.split(absFilePath)
    db = mrcdb.cvsTo2DDict(f"{path}/clients.csv", "user")
except:
    db = {}


app = Flask(__name__)
app.secret_key = "LKJDF890E4WFUJ9O83I45NHJRULHJRNE9P8GYUHJR784EHSDV"


@app.route("/")
def index():
    page = ""

    f = open("templates/index.html", "r")
    page = f.read()
    f.close()

    return page


@app.route("/signup")
def signupPage():

    if session.get("logIn"):
        return redirect("/home")
    else:
        page = ""

        f = open("templates/signup.html", "r")
        page = f.read()
        f.close()

        return page


@app.route("/signup", methods=["POST"])
def signUp():
    form = request.form

    if form["user"] not in db.keys():
        # This "salt" thing is just for add an extra security to the password
        salt = random.randint(1000, 10000000000)
        newPass = f"{form['password']}{salt}"
        # Encrypting the password
        newPass = hashlib.sha256(newPass.encode("utf-8")).hexdigest()

        db[form["user"]] = {
            "name": form["name"], "password": newPass, "salt": salt}
        # Update the csv file with the new user
        mrcdb.dict2DToCsv(db, "clients.csv", "user")
        return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/login")
def loginPage():
    if session.get("logIn"):
        return redirect("/home")
    else:
        page = ""

        f = open("templates/login.html", "r")
        page = f.read()
        f.close()

        return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    if form["user"] in db.keys():

        salt = db[form["user"]]["salt"]
        formPassword = f"{form['password']}{salt}"
        formPassword = hashlib.sha256(formPassword.encode("utf-8")).hexdigest()

        if formPassword == db[form["user"]]["password"]:
            session["logIn"] = form["user"]
            print("Session iniciada")
            return redirect("/home")
        else:
            return redirect("/login")
    else:
        return redirect("/signup")


@app.route("/home")
def home():
    if session.get("logIn"):
        page = ""

        f = open("templates/home.html", "r")
        page = f.read()
        f.close()

        page = page.replace("{name}", db[session["logIn"]]["name"])
        return page
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    if session.get("logIn"):
        session.clear()
        return redirect("/")
    else:
        return redirect("/login")


app.run(host="0.0.0.0", port=81)
