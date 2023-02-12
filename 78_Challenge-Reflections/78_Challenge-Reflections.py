# Day 78 on Replit: "Challenge: Reflections store"

from flask import Flask
import mrcdb

app = Flask(__name__, static_url_path="/static")

reflections = {}

reflections = mrcdb.cvsTo2DDict("reflections.csv", "day")


@app.route("/")
def home():
    page = ""
    return page


@app.route("/<dayNumber>")
def index(dayNumber):
    page = ""

    f = open("templates/day.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{day}", dayNumber)
    page = page.replace("{link}", reflections[dayNumber]["link"])
    page = page.replace("{reflection}", reflections[dayNumber]["reflection"])

    page = page.replace("{prevDay}", f"/{int(dayNumber)-1}")
    page = page.replace("{nextDay}", f"/{int(dayNumber)+1}")

    return page


@app.route("/77")
def day77():
    page = ""

    text = "This project started on day 78"
    link = "/78"

    f = open("templates/out.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{text}", text)
    page = page.replace("{link}", link)

    return page


@app.route("/101")
def day101():
    page = ""

    text = "This project finished on day 100"
    link = "/100"

    f = open("templates/out.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{text}", text)
    page = page.replace("{link}", link)

    return page


app.run(host="0.0.0.0", port=81)
