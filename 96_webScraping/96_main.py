import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

myTitles = soup.find_all("span", class_="titleline")
words_to_search = ["replit", "python", "w3c"]

for title in myTitles:
    a_tag = title.find_all("a")
    text = a_tag[0].text.lower()

    # I dont like this solution because I don't know how effective it is
    for word in words_to_search:
        if word in text:
            print(text)

print("-")
