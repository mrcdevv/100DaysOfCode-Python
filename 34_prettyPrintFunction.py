# Day 34 on Replit: "Pretty print Functions"

# Fix my code section

# import os, time
# listOfFood = []

# def prettyPrint():
#   os.system("clear") 
#   print("listofFood") 
#   print()
#   counter = 1 
#   for order in listOfFood: 
#     print(f"[counter]: {order}") 
#     counter + 1 
#   time.sleep(1)
# while True:
#   print("Yummy Food Restaurant")
#   menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#   if menu == "1":
#     order = input("order > ")
#     listOfFood.append(order)
#   elif menu =="2":
#     order = input ("delete order> ")
#     if order in listOfFood:
#       listOfFood.remove(order)
#   elif menu == "3": 
#   prettyPrint() 
#   time.sleep(1)
#   os.system("clear")

import os, time
listOfFood = []

def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter + 1 
  time.sleep(1)

while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu == "2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint() 
  time.sleep(1)
  os.system("clear")


# Challenge section

import os, time

listOfEmail = []
randomSpam = """It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
Ian Spammington III"""

def prettyPrint():
  os.system("clear")
  print("Email list")
  print()
  for i in range(len(listOfEmail)):
    print(f"{i + 1}: {listOfEmail[i]}")
    
  time.sleep(3)
  os.system("clear")

def clearConsole(sec):
  time.sleep(sec)
  os.system("clear")

def spam():
  if len(listOfEmail) < 10:
    emailCount = len(listOfEmail)
  else:
    emailCount = 10

  for i in range(0, emailCount):
    print(f"Dear {listOfEmail[i]}\n{randomSpam}")
    clearConsole(5)

while True:
  print("SPAMMER Inc.")
  menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n>")
  print()

  if menu == "1":
    email = input("Email: ")
    listOfEmail.append(email)
    clearConsole(0.5)
  elif menu == "2":
    email = input("Email: ")
    if email in listOfEmail:
      listOfEmail.remove(email)
      clearConsole(0.5)
    else:
      print("Email not found")
      clearConsole(0.5)
      continue
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    print()
    print("Generating spam...")
    clearConsole(0.5)
    spam()
  else:
    print("This option doesn´t exist")
  
