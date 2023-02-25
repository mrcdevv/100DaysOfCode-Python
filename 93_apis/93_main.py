# Day 93 on Replit: "API? Spotify? Verify!"

import requests
import random
from requests.auth import HTTPBasicAuth
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    content = ""

    if request.method == "POST":
        form = request.form

        print(form)
        year = form["year"]

        # Here u need to place your own Client ID and Client Secret or the app will not work
        user = 'CLIENT_ID'
        password = 'CLIENT_SECRET'

        url = "https://accounts.spotify.com/api/token"
        data = {"grant_type": "client_credentials"}
        auth = HTTPBasicAuth(user, password)

        response = requests.post(url, data=data, auth=auth)
        accessToken = response.json()["access_token"]

        offset = random.randint(0, 200)

        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {accessToken}"}
        search_query = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"

        response = requests.get(f"{url}{search_query}", headers=headers)
        data = response.json()

        for track in data["tracks"]["items"]:
            with open("templates/song.html", "r") as f:
                content += f.read()

            song_name = track["name"]
            song_url = track["preview_url"]
            song_link = track["external_urls"]["spotify"]

            content = content.replace("{song_name}", song_name)
            content = content.replace("{song_url}", song_url)
            content = content.replace("{song_link}", song_link)

    home = ""
    with open("templates/home.html", "r") as f:
        home = f.read()

    if content != "":
        home = home.replace("{content}", content)
    else:
        home = home.replace("{content}", "")

    return home


app.run(host="0.0.0.0", port=81)
