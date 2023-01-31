# Day 53 on Replit: "Challenge: Video Game Inventory"

import os,time

inventory = []

# Load the list from a file
try:
  f = open("inventory.txt", "r")
  inventory = eval(f.read())
  f.close()
except:
  print("Starting with an empty inventory")
  
def addItem():
  time.sleep(1)
  os.system("clear")
  
  item = input("Item to add > ")
  inventory.append(item)
  print("Added")

def removeItem():
  time.sleep(1)
  os.system("clear")
  
  item = input("Item to remove > ")
  inventory.remove(item)
  print("Removed")

def viewInventory():
  time.sleep(1)
  os.system("clear")

  print("INVENTORY")
  print("="*9)
  print

  alreadyShowed = []
  
  for item in inventory:
    if item not in alreadyShowed:
      print(f"{item} {inventory.count(item)}")
      alreadyShowed.append(item)

  time.sleep(3)
  os.system("clear")


while True:
  time.sleep(1)
  os.system("clear")
  
  print("INVENTORY")
  print("="*9)
  print()

  menu = input("1. Add\n2. Remove\n3. View\n4. Exit\n> ")

  if menu == "1":
    addItem()
  elif menu == "2":
    removeItem()
  elif menu == "3":
    viewInventory()
  else:
    break

  # Save in a file
  f = open("inventory.txt", "w")
  f.write(str(inventory))
  f.close()
