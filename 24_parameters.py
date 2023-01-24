# Day 23 on Replit: "Parameters"

# Fix my code section

# def pizza_order(topping1 topping2):
#   if topping1 = "pepperoni":
#     print(topping1, "is a great choice")
#   else:
#     print(topping1, "is kinda lame on pizza")
#   print(topping2, "sounds delicious, much better than" topping1)
  
# topping1 =  input("Name a pizza topping. ")
# topping2 = input("Name a second pizza topping. ")

#   pizza_order(topping1, topping2)

def pizza_order(topping1, topping2):
  if topping1 == "pepperoni":
    print(topping1, "is a great choice")
  else:
    print(topping1, "is kinda lame on pizza")
  
  print(topping2, "sounds delicious, much better than", topping1)
  
topping1 =  input("Name a pizza topping. ")
topping2 = input("Name a second pizza topping. ")

pizza_order(topping1, topping2)


# Challenge section

import random

print("Infinity Dice")
print()

def rollDice(sides):
  rolled = random.randint(1, sides)
  print("You rolled", rolled)

sides = int(input("How many sides? "))
rollDice(sides)
  