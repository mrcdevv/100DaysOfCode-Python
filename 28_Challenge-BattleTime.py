# Day 28 on Replit: "Challenge: Battle Time"

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

def damage(strength1, strength2):
  if strength1 > strength2:
    punch = (strength1 - strength2) + 1
  else:
    punch = (strength2 - strength1) + 1
  return punch

def showStats(name, type, health, strength):
  print(name, "the", type)
  print("Health:", health)
  print("Strength:", strength)

print("Battle time")
print()
# first warrior
name1 = input("Name your warrior: ")
type1 = input("Character type (Human, Elf, Wizard, Orc): ")
health1 = health()
strength1 = strength()

print("""
  --------------------------
  """)

# second warrior
name2 = input("Name your oponent: ")
type2 = input("Character type (Human, Elf, Wizard, Orc): ")
health2 = health()
strength2 = strength()
  
clearConsole(1)
print("Generating characters...")
clearConsole(1)

# show stats
showStats(name1, type1, health1, strength1)
print()
showStats(name2, type2, health2, strength2)

print()
print("The battle is about to begin...")
clearConsole(8)

# Battle
print("Battle time!")
round = 1

while True:
  luck1 = rollDice(6)
  luck2 = rollDice(6)

  # who hit who
  if luck1 > luck2:
    print(name1, "wins the round", round)
    print(name2, "takes a hit, with", damage(strength1, strength2), "damage")
    health2 -= damage(strength1, strength2)
    print()
  elif luck1 < luck2: 
    print(name2, "wins the round", round)
    print(name1, "takes a hit, with", damage(strength1, strength2), "damage")
    health1 -= damage(strength1, strength2)
    print()
  else:
    print("Draw")
    print()

  # show stats
  showStats(name1, type1, health1, strength1)
  print()
  showStats(name2, type2, health2, strength2)

  # someone die?
  if health1 <= 0:
    print()
    print(name1, "the", type1, "loose.", name2, "the", type2, "win")
    clearConsole(8)
    break
  elif health2 <= 0:
    print()
    print(name2, "the", type2, "loose.", name1, "the", type1, "win")
    clearConsole(8)
    break
  else:
    print()
    print("They´re both standing for the next round!")
    clearConsole(8)
    round += 1
    continue

print("The battle lasted", round, "rounds")