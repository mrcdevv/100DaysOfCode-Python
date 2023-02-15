# DAYYYYYYYYY


from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    form = request.args

    if form == {}:
        return "Nothing here!"
    elif form["lang"] == "eng":
        return "Hello, and welcome to our wonderful website!"
    else:
        return "I only know english :/"


app.run(host="0.0.0.0", port="81")
