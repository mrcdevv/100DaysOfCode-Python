import os, time
myList = []

print("ToDo List Manager")

def showMenu():
  print("What do you want to do?\n1. View\n2. Add\n3. Remove\n4. Edit")
  option = int(input("> "))
  return option

def clearConsole(sec):
  time.sleep(sec)
  os.system("clear")

def showList():
  print()
  count = 1
  for item in myList:
    print(f"{count}: {item}")
    count += 1
  print()

def add():
  item = input("What do you want to add? ")
  if item in myList:
    print()
    print("This item already exist!")
  else:
    print()
    myList.append(item)
    print("Item added")

def remove():
  item = input("What do you want to remove? ")
  if item in myList:
    print()
    choice = input(f"Are you sure you want to remove {item}? ")
    if choice == "yes" or choice == "Yes":
      myList.remove(item)
      print()
      print("Item removed")
  elif item == "everything" or item == "Everything":
    myList.clear()
    print()
    print("ToDo erased")
  else:
    print()
    print(f"{item} doesn´t exist")

def edit():
  item = input("What do you want to edit? ")
  if item in myList:
    print()
    newItem = input("What do you want to change to it? ")
    print()
    choice = input(f"Are you sure you want to edit {item}? ")
    if choice == "yes" or choice == "Yes":
      print()
      myList[myList.index(item)] = newItem
      print("Item edited")
    else:
      print()
      print("Operation canceled")
  

while True:
  clearConsole(1)
  choice = showMenu()

  if choice == 1:
    clearConsole(0.5)
    showList()
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
  