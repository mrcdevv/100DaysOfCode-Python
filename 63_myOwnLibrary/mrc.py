# My own library
import os
import time


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def clearConsole(sec):
    time.sleep(sec)
    os.system("cls")


# View all items in a 2d list
def prettyPrint2D(lst):
    print()
    for row in lst:
        for item in row:
            print(f"{item: ^15}", end=" | ")
        print()
    print()


# View all items in a 1d list enumerated
def prettyPrint1D(lst):
    print()
    for i in range(len(lst)):
        print(f"{i + 1}: {lst[i]}")
    print()


# Add an item to a list
def addItem(lst):
    item = input("Item to add > ")
    lst.append(item)
    print("Added")


# Remove an item in a list
def removeItem(lst):
    item = input("Item to remove > ")
    lst.remove(item)
    print("Removed")


# Generate an empty 2D List
def emptyList2D(rows, cols):
    return [[None for i in range(cols)] for j in range(rows)]


# View al items in a 1D Dictionary
def printDictionary1D(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")


# View al items in a 2D Dictionary
def printDictionary2D(dict):
    print()
    for key, value in dict.items():
        print(key, end=" | ")
        for subKey, subValue in value.items():
            print(subValue, end=" | ")
    print()


# Both functions are used like "data base", so when u execute a program, it has the data that u already used
# Write the content in a list into a file (used for save a list into a file)
def autoSave(file, lst):
    f = open(file, "w")
    f.write(str(lst))
    f.close()


# Read a file and load it in a list (used for load a list using a file)
def autoLoad(file, lst):
    try:
        f = open(file, "r")
        lst = eval(f.read())
        f.close
    except:
        print("File not found. Starting with an empty file")
        print()
