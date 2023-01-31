# Day 52 on Replit: "Avoiding Crashes"

# Fix my code section
# try:  
# f.open("Stuff.mine","r")
# myStuff = eval(f.read())
# f.close()

# for row in myStuff:
#   print(row)

try:  
    f = open("Stuff.mine","r")
    myStuff = eval(f.read())
    f.close()
except Exception as err:
    print(err)

for row in myStuff:
    print(row)

# Challenge section

import os, time

pizzas = []

# Load the file
try:
  f = open("pizza.txt", "r")
  pizzas = eval(f.read())
  f.close
except:
  print("File not found. Starting with an empty file")
  print()

def addPizza():
  time.sleep(1)
  os.system("clear")

  name = input("Name: ")
  size = input("Size (s/m/l): ").strip().lower()
  while True:
    try: 
      quantity = int(input("Quantity: "))
      break
    except:
      print("The quantity must be an integer")

  if size == "s":
    price = 5
  elif size == "m":
    price = 10
  else:
    price = 20

  price = round(price * quantity, 2)
  row = [name, size, quantity, price]
  pizzas.append(row)
  
  time.sleep(1)
  os.system("clear")

def viewPizzas():
  time.sleep(1)
  os.system("clear")
  name = "Name"
  size = "Size"
  quantity = "Quantity"
  total = "Total"

  # Make the header of the table
  print(f"{name:^15}|{size:^15}|{quantity:^15}|{total:^15}|")
  
  for order in pizzas:
    for item in order:
      print(f"{item:^15}", end= "|")
    print()

  time.sleep(3)
  os.system("clear")
  

while True:
  print("Rominos Pizza")
  print()

  menu = input("1. Add Pizza\n2. View Pizzas\n> ")

  if menu == "1":
    addPizza()
  else:
    viewPizzas()

  # Save in the file
  f = open("pizza.txt", "w")
  f.write(str(pizzas))
  f.close()