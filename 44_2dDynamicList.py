# Day 44 on Replit: "2D Dynamic Lists"

# Fix my code section

# listOfShame = [] 

# while True: 
#   menu = input("Add or Remove?") 

#   if(menu.strip().lower()[0]=="a"): 
    
#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")
    
#     row = [name, age, pref] 
  
#     listOfShame.append(row)    

#   else: 
#     name = input("What is the name of the record to delete?") 
    
#     if name in listOfShame: 
#       listOfShame.remove(name) # remove the whole row if name is in it

#   print(listOfShame)

  
listOfShame = [] 

while True: 
  menu = input("Add or Remove?") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 

  else: 
    name = input("What is the name of the record to delete?") 
    
    for row in listOfShame:
        if name in row: 
            listOfShame.remove(row) # remove the whole row if name is in it

  print(listOfShame)

# Challenge section

import random, time, os

print("Bingo Card Game!")
print()

rows, cols = 3, 3
bingo = [[None for i in range(cols)] for j in range(rows)]

def prettyPrint():
  print()
  for row in bingo:
    for item in row:
      print(f"{item: ^15}", end =" | ")
    print()
  print()

def clearConsole(sec):
  time.sleep(sec)
  os.system("clear")

numbers = []
index = 0

# Ordenar los numeros
for i in range(8):
  ran = random.randint(1, 90)
  numbers.append(ran)
numbers.sort()

# Rellenar el bingo con los numeros ordenados
for i in range(3):
  for j in range(3):
    if i == 1 and j == 1:
      bingo[i][j] = "BINGO"
    else:
      bingo[i][j] = numbers[index]
      index += 1

prettyPrint()
x = 1

while True:
  number = int(input("What number was called? "))
  print()

  if x == 8:
    print()
    print("You have won!")
    break
  else: 
    for row in range(3):
      for item in range(3):
        if number == bingo[row][item]:
          bingo[row][item] = "X"
          x += 1
        clearConsole(0)
  prettyPrint()
  
      