# Day 90 on Replit: "JSON"

import requests
import json

response = requests.get("https://randomuser.me/api/")

if response.status_code == 200:
    user = response.json()
    print(json.dumps(user, indent=2))

for i in range(10):
    response = requests.get("https://randomuser.me/api/")

    if response.status_code == 200:
        user = response.json()

        image = f'{user["results"][0]["picture"]["large"]}'

        name = f'{user["results"][0]["name"]["first"]}'
        last_name = f'{user["results"][0]["name"]["last"]}'
        fullname = f'{name}{last_name}'

        picture = requests.get(image)

        with open(f"{fullname}.jpg", "wb") as f:
            f.write(picture.content)
