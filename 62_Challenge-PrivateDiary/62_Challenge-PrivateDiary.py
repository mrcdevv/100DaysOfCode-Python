# Day 62 on Replit: "Challenge: Private Diary"

# For use the replit db u have to install the Replit package (pip install replit)
from replit import Database
import datetime
import os

# Here you need your db url (on replit's shell: echo $REPLIT_DB_URL)
db = Database(db_url="")


def showMenu():
    while True:
        try:
            menu = int(input("1. Add\n2. View\n3. Exit\n> "))
            return menu
        except:
            print("Option not found")
            print()


def addEntry():
    timestamp = datetime.datetime.now()
    entry = input(f"Diary entry for {timestamp}\n> ")

    db[f"entry{timestamp}"] = entry


def viewEntry():
    os.system("cls")
    keys = db.prefix("entry")
    keys = keys[::-1]

    for key in keys:
        os.system("cls")
        print(f"{key[5:]}\n\t{db[key]}")
        print()
        choice = input("Show another? y/n: ").strip().lower()
        if choice == "y":
            continue
        else:
            break


# Empty db
# keys = db.keys()
# for key in keys:
#  del db[key]


print("Private Diary")
print()

password = input("Password: ")

while password != "123":
    print("Wrong password")
    print()
    password = input("Password: ")


while True:
    os.system("cls")
    print("Welcome MRC")
    print()

    menu = showMenu()

    if menu == 1:
        addEntry()
    elif menu == 2:
        viewEntry()
    else:
        break
