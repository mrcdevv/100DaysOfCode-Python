from flask import Flask, redirect, request

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=["GET"])
def index():
    page = ""

    f = open("templates/index.html", "r")
    page = f.read()
    f.close()

    form = request.args

    if form == {} or form["theme"] == "dark":
        theme = "dark"
        themeMod = "dark-mod"
    elif form["theme"] == "light":
        theme = "light"
        themeMod = "light-mod"
    elif form["theme"] == "green":
        theme = "green"
        themeMod = "green-mod"
    else:
        theme = "pink"
        themeMod = "pink-mod"

    page = page.replace("{theme}", theme)
    page = page.replace("{theme-mod}", themeMod)

    return page


@app.route("/blog/day1")
def reDayOne():
    return redirect("/day1")


@app.route("/blog/day2")
def reDayTwo():
    return redirect("/day2")


@app.route("/day1", methods=["GET"])
def dayOne():
    title = "Hello World. This is my Blog"
    text = "This is my first entry"

    page = ""

    f = open("templates/blog.html", "r")
    page = f.read()
    f.close()

    form = request.args

    if form == {} or form["theme"] == "dark":
        theme = "dark"
        themeMod = "dark-mod"
    elif form["theme"] == "light":
        theme = "light"
        themeMod = "light-mod"
    elif form["theme"] == "green":
        theme = "green"
        themeMod = "green-mod"
    else:
        theme = "pink"
        themeMod = "pink-mod"

    page = page.replace("{title}", title)
    page = page.replace("{date}", "January 10")
    page = page.replace("{entry}", text)
    page = page.replace("{theme}", theme)
    page = page.replace("{theme-mod}", themeMod)

    return page


@app.route("/day2", methods=["GET"])
def dayTwo():
    title = "Hello World. This is my Blog"
    text = "This is my second entry"

    page = ""

    f = open("templates/blog.html", "r")
    page = f.read()
    f.close()

    form = request.args

    if form == {} or form["theme"] == "dark":
        theme = "dark"
        themeMod = "dark-mod"
    elif form["theme"] == "light":
        theme = "light"
        themeMod = "light-mod"
    elif form["theme"] == "green":
        theme = "green"
        themeMod = "green-mod"
    else:
        theme = "pink"
        themeMod = "pink-mod"

    page = page.replace("{title}", title)
    page = page.replace("{date}", "January 11")
    page = page.replace("{entry}", text)
    page = page.replace("{theme}", theme)
    page = page.replace("{theme-mod}", themeMod)

    return page


app.run(host='0.0.0.0', port=81)
