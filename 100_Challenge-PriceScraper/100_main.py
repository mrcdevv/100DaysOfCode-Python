import requests
import config
import time
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import schedule

db = []


def page_scraping():
    url = "https://keychron.mitiendanube.com/teclados/"
    target_price = 30000.0

    response = requests.get(url)
    html = response.text

    page_content = BeautifulSoup(html, "html.parser")

    content_container = page_content.find_all(
        "div", class_="span3 item-container m-bottom-half")

    for div in content_container:
        discount = div.find("span", class_="js-offer-percentage").text
        title = div.find(
            "a", class_="js-item-name item-name").text.replace("...", "")
        current_price = div.find("span", class_="js-price-display item-price h6").text.replace(
            "$", "").replace(".", "").replace(",", ".").strip()
        link = div.find("a", class_="js-item-name item-name")["href"]

        product = {"title": title, "discount": int(discount), "current_price": float(
            current_price), "link": link, "target_price": float(target_price)}

        db.append(product)

    email()


def check_prices():
    page = ""

    for item in db:
        if item["current_price"] < item["target_price"] or item["discount"] > 30:
            with open("./content.html", "r") as f:
                page += f.read()

            page = page.replace("{link}", item["link"])
            page = page.replace("{title}", item["title"])
            page = page.replace("{price}", str(item["current_price"]))

    return page


def email():
    email = config.username
    password = config.password

    content = check_prices()

    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(email, password)

    msg = MIMEMultipart()
    msg["To"] = email
    msg["From"] = email
    msg["Subject"] = "Product's Cheaper!"
    msg.attach(MIMEText(content, "html"))

    s.send_message(msg)
    del msg


page_scraping()
schedule.every(24).hours.do(page_scraping)

while True:
    schedule.run_pending()
    time.sleep(1)
