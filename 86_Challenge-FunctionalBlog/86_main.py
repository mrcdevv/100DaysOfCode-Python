# Day 86 on Replit: "Challenge: Functional blog engine"

from flask import Flask, redirect, request, session
import mrcdb


app = Flask(__name__, static_url_path='/static')
app.secret_key = "JKLSJKLSDujiosjaklJKLSDJKLajfiodaujiO890AJklfjdlkJFIOJAM<IDK.j"


try:
    # Load the blogs on a dictionary
    db = mrcdb.cvsTo2DDict("blogs.csv", "title")
except:
    db = {}


@app.route('/', methods=["POST", "GET"])
def index():
    page = ""

    # Load the main page
    main = open("templates/blog.html", "r")
    page = main.read()
    main.close()

    # If the admin is logged in
    if session.get("logedIn"):
        page = page.replace("{log}", "Logout")

        # Load the "admin panel"
        admin = open("templates/adminBlog.html", "r")
        page += admin.read()
        admin.close()

        # If something is submited through the form
        if request.method == 'POST':
            form = request.form

            # Check if the title already exist and if not...
            if form["title"] not in db.keys():
                # Load it in the db
                db[form["title"]] = {
                    "date": form["date"], "body": form["body"]}
                # Save every single blog
                mrcdb.dict2DToCsv("blogs.csv", "title", db)

            else:
                return redirect("/")

    # If the admin isn't logged in
    else:
        page = page.replace("{log}", "Login")

    # Check if exist at least one blog
    if db.keys() != {}:

        # Sort all the blogs from newest to oldest
        keys = list(db.keys())
        keys.reverse()

        for key in keys:
            # Load the basic template for each blog
            posts = open("templates/post.html", "r")
            page += posts.read()
            posts.close()

            page = page.replace("{title}", key)
            page = page.replace("{date}", db[key]["date"])
            page = page.replace("{text}", db[key]["body"])

    return page


@app.route("/login")
def loginPage():

    # If the admin is already logged in, don't let em login again
    if session.get("logedIn"):
        return redirect("/")
    else:
        page = ""

        f = open("templates/login.html", "r")
        page = f.read()
        f.close()

        return page


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    # Check credentials inputted
    if form["user"] == "admin" and form["password"] == "admin1":
        session["logedIn"] = "admin"
        return redirect("/")
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
    if session.get("logedIn"):
        session.clear()
        return redirect("/")
    else:
        return redirect("/login")


app.run(host='0.0.0.0', port=81)
