from flask import Flask, request, redirect
import mrcdb
import random
import os


absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
db = mrcdb.cvsTo2DDict(f"{path}/clients.csv", "user")

if "clients.csv" in os.listdir():
    print("Encontrado")
else:
    print("Ni idea")

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

        salt = random.randint(1000, 10000000000)
        newPass = f"{form['password']}{salt}"
        newPass = hash(newPass)

        db[form["user"]] = {
            "name": form["name"], "password": newPass, "salt": salt}
        # Update the csv file with the new user
        mrcdb.dict2DToCsv(db, "clients.csv", "user")
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

    if form["user"] in db.keys():

        salt = db[form["user"]]["salt"]
        formPassword = f"{form['password']}{salt}"
        formPassword = hash(formPassword)

        if formPassword == db[form["user"]]["password"]:
            return f"Welcome {db[form['user']]['name']}"
        else:
            return redirect("/login")
    else:
        return redirect("/signup")


app.run(host="0.0.0.0", port=81)
