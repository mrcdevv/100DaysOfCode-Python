# Day 27 on Replit: "Challenge: Character Builder"
# is the same than day 25 but with enhancements

import random, time, os

def rollDice(maxSides):
  return random.randint(1, maxSides)

def health():
  hp = (rollDice(6) * rollDice(8)) / 2 + 10
  return hp

def strength():
  s = (rollDice(6) * rollDice(8)) / 2 + 12
  return s

def clearConsole(seconds):
  time.sleep(seconds)
  os.system("clear")

while True:
  print("CHARACTER STATS GENERATOR")
  print()
  name = input("Name your warrior: ")
  type = input("Character type (Human, Elf, Wizard, Orc): ")
  
  clearConsole(1)
  print("Generating character...")
  clearConsole(1)

  print(name, "the", type)
  print("Health:", health())
  print("Strength:", strength())
  print()
  print()

  choice = input("Again? ")

  if choice == "Yes" or choice == "yes":
    clearConsole(0.5)
    continue
  else:
    break


