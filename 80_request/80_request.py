# Day 80 on Replit: "Incoming!"

from flask import Flask, request

credentials = {}

credentials["mrc"] = {"email": "mrc@gmail.com", "password": "123456789"}
credentials["admin"] = {"email": "admin@gmail.com", "password": "admin"}
credentials["admin"] = {"email": "admin@gmail.com", "password": "admin"}
credentials["maria"] = {
    "email": "maria21@hotmail.com", "password": "marthebest"}

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():
    page = ""

    f = open("templates/login.html", "r")
    page = f.read()
    f.close

    return page


@app.route("/home", methods=["POST"])
def home():
    page = ""

    f = open("templates/home.html", "r")
    page = f.read()
    f.close

    details = {}

    form = request.form

    try:
        details = credentials[form["username"]]
    except:
        tittle = "Something gone wrong"
        text = "Are you trying to hack me? Or dont remember your username/email/password"

        page = page.replace("{tittle}", tittle)
        page = page.replace("{text}", text)

        return page

    if details["email"] == form["email"] and details["password"] == form["password"]:
        tittle = f'Welcome {form["username"]}'
        text = tittle

        page = page.replace("{tittle}", tittle)
        page = page.replace("{text}", text)

        return page

    else:
        tittle = "Something gone wrong"
        text = "Are you trying to hack me? Or dont remember your username/email/password"

        page = page.replace("{tittle}", tittle)
        page = page.replace("{text}", text)

        return page


app.run(host='0.0.0.0', port=81)
