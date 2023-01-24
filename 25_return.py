# Day 23 on Replit: "Return Command"

# Fix my code section

#def area_square(side1 side2):
#   area = side1 * side2
#   return area_square

# area_square(4, 12)
# print(area)

def area_square(side1, side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)

# Challenge section

import random

print("CHARACTER STATS GENERATOR")

def rollDice(maxSides):
  return random.randint(1, maxSides)

def health():
  hp = rollDice(6) * rollDice(8)
  return hp

name = input("Name your warrior: ")
print("Their health is", health(), "hp")

