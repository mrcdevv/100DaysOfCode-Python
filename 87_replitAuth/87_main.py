# Day 87 on Replit: "Authentication"
# Today I learned about "Authentication" tool on Replit. So if u want to see the project working, u must enter: https://replit.com/@marcodeArg/Day87100Days#main.py

from flask import Flask, redirect, request, session
import os
from replit import db

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ['sessionKey']


@app.route('/', methods=["POST", "GET"])
def index():
    page = ""

    main = open("templates/blog.html", "r")
    page = main.read()
    main.close()

    username = request.headers["X-Replit-User-Name"]

    if username == "marcodeArg":

        admin = open("templates/blogAdmin.html", "r")
        page += admin.read()
        admin.close()

        if request.method == 'POST':
            form = request.form

            if form["title"] not in db.keys():
                db[form["title"]] = {
                    "date": form["date"], "body": form["body"]}

            else:
                return redirect("/")

    if db.keys() != {}:
        keys = list(db.keys())
        keys.reverse()

        for key in keys:
            posts = open("templates/post.html", "r")
            page += posts.read()
            posts.close()

            page = page.replace("{title}", key)
            page = page.replace("{date}", db[key]["date"])
            page = page.replace("{text}", db[key]["body"])

    return page


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


app.run(host='0.0.0.0', port=81)
