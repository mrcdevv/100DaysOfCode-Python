# Day 81 on Replit: "Challenge: I'm not a robot"

from flask import Flask, request

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    page = ""

    f = open("templates/index.html", "r")
    page = f.read()
    f.close()

    return page


@app.route("/out", methods=["POST"])
def home():
    form = request.form
    page = ""

    f = open("templates/out.html", "r")
    page = f.read()
    f.close()

    if form["metal"] == "no" and "error" not in form["text"].lower() and form["food"] == "human":

        page = page.replace("{tittle}", "Human")
        page = page.replace("{text}", "Fellow Human")

    else:
        page = page.replace("{tittle}", "Robot")
        page = page.replace("{text}", "Robot")

    return page


app.run(host="0.0.0.0", port=81)
