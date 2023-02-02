# For use the replit db u have to install the Replit package (pip install replit)
from replit import Database
import datetime
import os
import time

# Here you need your db url (on replit's shell: echo $REPLIT_DB_URL)
db = Database(db_url="")


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
