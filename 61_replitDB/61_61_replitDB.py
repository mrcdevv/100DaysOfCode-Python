# For use the replit db u have to install the Replit package (pip install replit)
from replit import Database
import datetime
import os
import time

db = Database(db_url="https://kv.replit.com/v0/eyJhbGciOiJIUzUxMiIsImlzcyI6ImNvbm1hbiIsImtpZCI6InByb2Q6MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb25tYW4iLCJleHAiOjE2NzU0MDY1NDEsImlhdCI6MTY3NTI5NDk0MSwiZGF0YWJhc2VfaWQiOiJmMjE3N2IyMy1kYmQyLTRmZWMtODEwZC1mZDY3MjdhNmM2ZDQiLCJ1c2VyIjoibWFyY29kZUFyZyIsInNsdWciOiJEYXk2MTEwMERheXMifQ.qvMF5bAvZhyZWY_gjboz2qwfWOT63DbhfgG5tJsOihvTGJGz0xCXy3C-iAK3wIPXRju3klt-5Y0pOxLP8GmUhw")  # Here you need your db url (on replit's shell: echo $REPLIT_DB_URL)


def addTweet():
    timestamp = datetime.datetime.now()
    tweet = input("🐥> ")

    key = f"mes{timestamp}"
    db[key] = tweet
    print("Tweet added!")


def viewTweets():
    count = 0
    keys = db.prefix("mes")
    keys = keys[::-1]

    for key in keys:
        count += 1
        print(f"{key}: {db[key]}")
        if count == 10:
            choice = input("Show 10 more? y/n")
            if choice == "y":
                count = 0
                continue
            else:
                break


while True:
    print("Tweeter")
    print()

    while True:
        try:
            menu = int(input("1. Add Tweet\n2. View Tweets\n3. Exit\n> "))
            if menu == 1 or menu == 2 or menu == 3:
                break
            else:
                print("Option not found")
        except:
            print("Option not found")

    os.system("cls")

    if menu == 1:
        addTweet()
        time.sleep(1)
        os.system("cls")
    elif menu == 2:
        viewTweets()
        time.sleep(4)
        os.system("cls")
    else:
        break
