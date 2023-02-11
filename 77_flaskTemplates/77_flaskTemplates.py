# Day 77 on Relpit: "Too. Much. Code."


# Challenge section

from flask import Flask, redirect

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    page = ""
    return page


@app.route("/blog/day1")
def reDayOne():
    return redirect("/day1")


@app.route("/blog/day2")
def reDayTwo():
    return redirect("/day2")


@app.route("/day1")
def dayOne():
    title = "Hello World. This is my Blog"
    text = "This is my first entry"

    page = ""

    f = open("templates/blog.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{title}", title)
    page = page.replace("{date}", "January 10")
    page = page.replace("{entry}", text)

    return page


@app.route("/day2")
def dayTwo():
    title = "Hello World. This is my Blog"
    text = "This is my second entry"

    page = ""

    f = open("templates/blog.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{title}", title)
    page = page.replace("{date}", "January 11")
    page = page.replace("{entry}", text)

    return page


app.run(host='0.0.0.0', port=81)
