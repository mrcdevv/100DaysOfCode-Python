from bs4 import BeautifulSoup
import time
import config
import requests
import schedule
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

words = ["python", "replit", "ai", "nvidia", "app"]

text = []
href = []


def clear_lists():
    text.clear()
    href.clear()


def website_posts():
    response = requests.get("https://replit.com/community-hub")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    div_container = soup.find_all("div", class_="css-wi7uht")

    links = 0

    for div in div_container:
        a_links = div.find_all("a")

        for link in a_links:
            if links == 4:
                break
            for word in words:
                if word in link.text.lower():
                    list_span = link.find_all("span", class_="css-1bpqt30")
                    span = list_span[0].text
                    if span not in text:
                        text.append(span)
                        href.append(link["href"])
                        break

            links += 1

    send_email()
    clear_lists()


def load_email():
    page = ""
    for i in range(len(text)):
        with open("email.html", "r") as f:
            page += f.read()

            page = page.replace("{content}", text[i])
            page = page.replace("{link}", href[i])

    return page


def send_email():
    email = config.username
    password = config.password

    content = load_email()

    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(email, password)

    msg = MIMEMultipart()
    msg["To"] = email
    msg["From"] = email
    msg["Subject"] = "New community event"
    msg.attach(MIMEText(content, "html"))

    s.send_message(msg)
    del msg


website_posts()
schedule.every(1).hours.do(website_posts)

while True:
    schedule.run_pending()
    time.sleep(1)
