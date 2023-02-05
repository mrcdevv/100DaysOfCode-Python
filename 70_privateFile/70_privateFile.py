# Today, on Replit, I learn about a feature called "Secrets" which are like a private db; And because it is private, I can´t use it here in VSC.
# That is why I created a kind of replica using csv files. The first part of the proyect is a "Admin Panel", where you can add new credentials or even remove credential. And the second part is a "User Panel", where the user can login using the right credentials

import csv
import os
import time

myDictPrivate = []


# Load the list using the csv file
def autoLoad():
    with open("privateCSV.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            myDictPrivate.append(
                {"username": row["username"], "password": row["password"]})


try:
    autoLoad()
except:
    pass


# Add a user to the list
def addUser():
    print("Add an acces")
    user = input("User > ")
    password = input("Password > ")

    for item in myDictPrivate:
        if user in item["username"]:
            print("Cannot add")
            return

    row = {"username": user, "password": password}
    myDictPrivate.append(row)


# Remove a user from the list
def removeUser():
    print("Remove an acces")
    user = input("User > ")

    for row in myDictPrivate:
        if user in row["username"]:
            myDictPrivate.remove(row)
            print("User removed")
            return
    print("User don't found")


# Update the csv file with the info inside the list
def autoSave():
    with open("privateCSV.csv", "w") as csvfile:
        headers = ["username", "password"]
        write = csv.DictWriter(csvfile, headers)
        write.writeheader()
        for row in myDictPrivate:
            write.writerow(
                {"username": row["username"], "password": row["password"]})


# Check for the credentials
def login(username, passw):
    for user in myDictPrivate:
        if user["username"] == username and user["password"] == passw:
            print("Welcome")
            return True
    print("Try again")
    return False


# Admin Panel (add/remove credentials)
def adminPanel():
    while True:
        time.sleep(1)
        os.system("cls")

        print("Admin Panel")
        print()

        menu = input("Want to add, remove or exit? ").strip().lower()
        if menu == "add":
            print()
            addUser()

        elif menu == "remove":
            if "privateCSV.csv" not in os.listdir():
                print("No one has permissions. You need to add at least one person")
                time.sleep(2)
                os.system("cls")
                addUser()

            else:
                removeUser()

        elif menu == "exit":
            break
        else:
            print("Option not found")
            time.sleep(1)
            os.system("cls")

    # At the end, when the admin exit the panel, all the data added or removed will be add to the csv file. For more security, this function could be called when the functions "addUser" and "removeUser" end, so no data is lost.
    autoSave()


# User Panel (login)
def userPanel():
    time.sleep(1)
    os.system("cls")
    print("User panel")
    print()

    username = input("Username > ").strip()
    password = input("Password > ").strip()

    # check for the right credentials
    while not login(username, password):
        print()
        username = input("Username > ").strip()
        password = input("Password > ").strip()

        login(username, password)


# Main program
while True:
    time.sleep(1)
    os.system("cls")
    menu = input("1. Admin Panel\n2. User panel\nAny other key to exit\n> ")

    if menu == "1":
        adminPanel()
    elif menu == "2":
        if myDictPrivate == []:
            print("You can´t acces to the User Panel because no one has permissions")
            print("Opening Admin Panel...")
            time.sleep(1)
            os.system("cls")
            adminPanel()
        else:
            userPanel()
            break
    else:
        break
