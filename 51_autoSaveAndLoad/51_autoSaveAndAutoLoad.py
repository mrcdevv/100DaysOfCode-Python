# Day 51 on Replit: "Save to and Load From Files"

# Fix my code section

# myEvents = []

# f = open("calendar.txt","r")
# myEvents = eval(f.read())
# f.close()

# def prettyPrint():
#   print()
#   for row in myEvents:
#     print(f"{row[0] :^15} {row[1] :^15}")
#   print()

# while True:
#   menu = input("1: Add, 2: Remove\n")

#   if menu == "1":
#     event = input("What event?: ").capitalize()
#     date = input("What date?: ")
#     row = [event,date]
#     myEvents.append(row)
#     prettyPrint()

#   else:
#     criteria = input("What event do you want to remove?: ").title()
#     for row in myEvents:
#       if criteria in row:
#         myevents.remove(row)

# f = open("calendar.txt", "w") 
# f.write(str(myEvents)) 
# f.close()

myEvents = []

# This has to be commented before run the program for the first time
# f = open("calendar.txt","r")
# myEvents = eval(f.read())
# f.close()

def prettyPrint():
    print()
    for row in myEvents:
        print(f"{row[0] :^15} {row[1] :^15}")
    print()

while True:
    menu = input("1: Add, 2: Remove\n")

    if menu == "1":
        event = input("What event?: ").capitalize()
        date = input("What date?: ")
        row = [event,date]
        myEvents.append(row)
        prettyPrint()

    else:
        criteria = input("What event do you want to remove?: ").title()
        for row in myEvents:
            if criteria in row:
                myEvents.remove(row)


    f = open("calendar.txt", "w") 
    f.write(str(myEvents)) 
    f.close()


# Challenge section 

# ToDo List but saving the list in a file and then reading it, so when the cache is cleared and then, executed the program again, the list will be stored

import os, time
myList = []

# Load the list BUT if the list doesn´t exit, the program will crash
f = open("mytodo.list", "r")
myList = eval(f.read())
f.close()

print("ToDo List Manager")

def showMenu():
  print("What do you want to do?\n1. View\n2. Add\n3. Remove\n4. Edit")
  option = int(input("> "))
  return option

def clearConsole(sec):
  time.sleep(sec)
  os.system("cls")

# View all the list
def prettyPrint():
  print()
  for row in myList:
    for item in row:
      print(f"{item: ^15}", end = " | ")
    print()
  print()

# View per priority
def printPerPriority(option):
  print()
  for row in myList:
    if option in row:
      for item in row:
        print(f"{item: ^15}", end = " | ")
    print()

def view():
  print("VIEW")
  print()
  option = int(input("1. View all\n2. View Prority\n>"))

  if option == 1:
    prettyPrint()
  elif option == 2:
    print()
    print("Choose a priority")
    priority = int(input("1. High\n2. Medium\n3. Low\n>"))
    if priority == 1:
      printPerPriority("High")
    elif priority == 2:
      printPerPriority("Medium")
    elif priority == 3:
      printPerPriority("Low")
    else:
      print("Option not found!")

def add():
  print("ADD")
  print()
  task = input("What is it? ").strip().capitalize()
  date = input("When is it due by? ").strip().capitalize()
  priority = input("What is the priority? (High | Medium | Low) ").strip().capitalize()

  row = [task, date, priority]

  myList.append(row)
  print("Task added")

def remove():
  item = input("What do you want to remove? ").strip().capitalize()
  for row in myList:
    if item in row:
      print()
      choice = input(f"Are you sure you want to remove {item}? ").strip().lower()
      if choice == "yes":
        myList.remove(row)
        print()
        print("Item removed")
    elif item == "Everything":
      myList.clear()
      print()
      print("ToDo erased")
    else:
      print()
      print(f"{item} doesn´t exist")

def edit():
  print("EDIT")
  item = input("What do you want to edit? ").strip().capitalize()
  for row in myList:
    if item in row:
      print()
      task = input("What is it? ").strip().capitalize()
      date = input("When is it due by? ").strip().capitalize()
      priority = input("What is the priority? (High | Medium | Low")
      print()
      choice = input("You´re about to edit your ToDo. Continue? (y/n)").strip().lower()
      if choice[0] == "y" :
        newItem = [task, date, priority]
        print()
        myList.remove(row)
        myList.append(newItem)
        
        print("Item edited")
      else:
        print()
        print("Operation canceled")
    else:
      print("Item dont found!")
  

while True:
  clearConsole(1)
  choice = showMenu()

  if choice == 1:
    clearConsole(0.5)
    view()
    clearConsole(5)
  elif choice == 2:
    clearConsole(0.5)
    add()
  elif choice == 3:
    clearConsole(0.5)
    remove()
  elif choice == 4:
    clearConsole(0.5)
    edit()
  else:
    print("I don´t get it. Bye")
    break
  
  # Save the list in the file
  f = open("mytodo.list", "w")
  f.write(str(myList))
  f.close()