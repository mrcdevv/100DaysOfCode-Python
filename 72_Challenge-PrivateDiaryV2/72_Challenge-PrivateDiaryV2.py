# Day 72 on Replit: "Challenge: Private Diary v2"
# The idea of this project was to make a login system. The user and password (encrypted password), needed to be saved in the Replit db.
# But, as I don´t like the idea of having to instal replit module or what ever it is, I made my own module with some functions to save date in csv files
import mrcdb
import os
import time
import datetime
import random

dbLogin = {}
dbDiary = {}

try:
    dbLogin = mrcdb.cvsTo2DDict("login.csv", "username")
    dbDiary = mrcdb.csvToDictInList("diary.csv")
except:
    pass


def showMenu():
    while True:
        try:
            menu = int(input("1. Add\n2. View\n3. Exit\n> "))
            return menu
        except:
            print("Option not found")
            print()


def addEntry():
    os.system("cls")
    timestamp = datetime.datetime.now()
    entry = input(f"Diary entry for {timestamp}\n> ")

    dbDiary[f"entry{timestamp}"] = entry


def viewEntry():
    os.system("cls")
    keys = list(dbDiary.keys())

    keys.reverse()

    for key in keys:
        os.system("cls")
        print(f"{key[5:]}\n\t{dbDiary[key]}")
        print()
        choice = input("Show another? y/n: ").strip().lower()
        if choice == "y":
            continue
        else:
            break


def startUp():
    keys = dbLogin.keys()

    if len(keys) < 1:
        print("Register")
        print()
        username = input("Username > ").strip()
        password = input("Password > ").strip()
        salt = random.randint(1000, 10000000)

        newPassword = f"{password}{salt}"
        newPassword = hash(newPassword)

        dbLogin[username] = {"password": newPassword, "salt": salt}

    else:
        time.sleep(1)
        os.system("cls")
        print("Login")
        print()
        username = input("Username > ").strip()
        password = input("Password > ").strip()

        if username in keys:
            salt = dbLogin[username]["salt"]

            newPassword = f"{password}{salt}"
            newPassword = hash(newPassword)

            if newPassword == dbLogin[username]["password"]:
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
mrcdb.dict2DToCsv(dbLogin, "login.csv", "username")

menu = showMenu()

while menu == 1 or menu == 2:
    if menu == 1:
        addEntry()
        mrcdb.dictToCsv(dbDiary, "diary.csv")
    else:
        viewEntry()

    menu = showMenu()
