import schedule
import time
import config
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

quotes = []

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = eval(f.read())

print(random.choice(quotes))

username = config.username
password = config.password


def sendEmail():
    email = random.choice(quotes)
    s = smtplib.SMTP(host="smtp.gmail.com", port=587)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Random Quot"
    msg.attach(MIMEText(email, "html"))

    s.send_message(msg)
    del msg


def sendingEmail():
    print("Sending...")
    sendEmail()


schedule.every(24).hours.do(sendingEmail)

while True:
    schedule.run_pending()
    time.sleep(1)
