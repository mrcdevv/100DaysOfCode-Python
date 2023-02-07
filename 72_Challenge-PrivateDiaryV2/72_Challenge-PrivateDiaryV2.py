# https://replit.com/@marcodeArg/Day72100Days#main.py


import mrcdb


import os
import time
import datetime
import random


def showMenu():
    while True:
        try:
            menu = int(input("1. Add\n2. View\n3. Exit\n> "))
            return menu
        except:
            print("Option not found")
            print()


def addEntry():
    os.system("clear")
    timestamp = datetime.datetime.now()
    entry = input(f"Diary entry for {timestamp}\n> ")

    db[f"entry{timestamp}"] = entry


def viewEntry():
    os.system("clear")
    keys = db.prefix("entry")
    keys = keys[::-1]

    for key in keys:
        os.system("clear")
        print(f"{key[5:]}\n\t{db[key]}")
        print()
        choice = input("Show another? y/n: ").strip().lower()
        if choice == "y":
            continue
        else:
            break


def startUp():
    keys = db.keys()

    if len(keys) < 1:
        print("Register")
        print()
        username = input("Username > ").strip()
        password = input("Password > ").strip()
        salt = random.randint(1000, 10000000)

        newPassword = f"{password}{salt}"
        newPassword = hash(newPassword)

        db[username] = {"password": newPassword, "salt": salt}

    else:
        time.sleep(1)
        os.system("clear")
        print("Login")
        print()
        username = input("Username > ").strip()
        password = input("Password > ").strip()

        if username in keys:
            salt = db[username]["salt"]

            newPassword = f"{password}{salt}"
            newPassword = hash(newPassword)

            if newPassword == db[username]["password"]:
                os.system("clear")
                print("Welcome")
                print()
                return True
            else:
                print("Wrong password")
                startUp()
        else:
            print("User not found")
            startUp()


print("Private Diary")
print()

startUp()

menu = showMenu()

while menu == 1 or menu == 2:
    if menu == 1:
        addEntry()
    else:
        viewEntry()

    menu = showMenu()
