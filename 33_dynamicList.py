# Day 33 on Replit: "Dynamic Lists"

# Fix my code section

# def printList():
#   print() 
#   for item in myPartyList:
#     print(item)
#   print() 

# while True:
#   menu = input("add or remove?: )
#   if menu = "add":
#     item = input("Who should I add to the party list?: ")
#     myPartyList.add(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?: ")
#     if item in myPartyList:
#       myPartyList.remove(list)
#     else:
#       print("{item} was not in the list)
#   printList()

myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 

while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()

# Challenge section

import os, time

myList = []
title = "ToDo List Manager"

def printList():
  for item in myList:
    print(item)
  print()

def cleanConsole(seconds):
  time.sleep(seconds)
  os.system("clear")

while True:
  print(f"{title: ^50}")
  print()

  menu = input("Do you want to view, add, edit or exit the todo list?\n")
  print()

  if menu == "view" or menu == "View":
    printList()
    cleanConsole(5)
  elif menu == "add" or menu == "Add":
    item = input("What item do you want to add?\n")
    myList.append(item)
    cleanConsole(0.5)
  elif menu == "edit" or menu == "Edit":
    item = input("What item did you complete?\n")
    if item in myList:
      myList.remove(item)
      cleanConsole(0.5)
    else:
      print(f"{item} is not in the list")
      cleanConsole(3)
      continue
  else:
    print("Bye!")
    break
      
    

      
    