# Day 71 on Replit: "It's Called Hashing"

# Fix my code section

# from replit import db

# ans = input("Password >")
# salt = db["david"]["salt"]
# newPassword = f"{ans}{salt}"
# newPassword = hash(newPassword)

# if ans == db["david"]["password"]:
#   print("Login successful")

import time
import os
import random
from replit import Database, db

ans = input("Password >")
salt = db["david"]["salt"]
newPassword = f"{ans}{salt}"
newPassword = hash(newPassword)

if newPassword == db["david"]["password"]:
    print("Login successful")


# Challenge section

# Here you need your db url (on replit's shell: echo $REPLIT_DB_URL)
db = Database(db_url="")

# Delete everything
# keys = db.keys()
# for key in keys:
#   del db[key]


def addUser():
    print()

    username = input("Username > ")
    password = input("Password > ")
    salt = random.randint(1000, 10000000)
    newPassword = f"{password}{salt}"
    newPassword = hash(newPassword)

    db[username] = {"password": newPassword, "salt": salt}


def login():
    username = input("Username > ")
    password = input("Password > ")

    keys = db.keys()

    for key in keys:
        if username == key:
            salt = db[key]["salt"]
            newPassword = f"{password}{salt}"
            newPassword = hash(newPassword)

            if newPassword == db[key]["password"]:
                print()
                print("Welcome")
                return
            else:
                print()
                print("Password Wrong")
                return
    print()
    print("Username not found")


while True:
    time.sleep(1)
    os.system("clear")
    print("Login System")
    print()

    menu = input("1. Add user\n2. Login\n> ").strip()
    if menu == "1":
        time.sleep(1)
        os.system("clear")
        addUser()
    elif menu == "2":
        time.sleep(1)
        os.system("clear")
        login()
