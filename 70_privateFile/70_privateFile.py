# Read the Readme.md for more information

import csv
import os

myDictPrivate = []

# if "privateCSV.csv" not in os.listdir():
#     f = open("privateCSV.csv", "w")
#     f.close()


def loadCSV():
    with open("privateCSV.csv", "a+") as csvfile:
        headers = ["username", "password"]
        write = csv.DictWriter(csvfile, headers)

        write.writeheader()
        while True:
            print("Add an acces")
            user = input("User > ")
            password = input("Password > ")
            write.writerow({"username": user, "password": password})
            print()
            print("User added")
            print()

            choice = input("Add another? y/n: ").strip().lower()
            if choice == "y":
                continue
            else:
                break


def readCSV():
    with open("privateCSV.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            myDictPrivate.append(row)
            print(row)


# loadCSV()
readCSV()

while True:
    user = input("Username > ")
    passw = input("Password > ")

    for i in myDictPrivate:
        if myDictPrivate["username"] == user and myDictPrivate["password"] == passw:
            print("Welcome")
            break
        else:
            print("Try again")
            print()


# user = input("blalala")
# passw = input("bllbla")


# # MMMMMMMMMMM
# if user == "Admin" and passw == myDictPrivate[user]["password"]:
#     print("Welcome")
