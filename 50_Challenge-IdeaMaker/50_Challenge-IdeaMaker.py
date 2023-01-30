# Day 50 on Replit: "Challenge: Idea Maker..."

import random

def addIdea():
  idea = input("Input your idea.\n> ")
  print()
  
  f = open("my.ideas", "a+")
  f.write(f"{idea}\n")
  f.close()
  
  print("Nice! Your idea has been stored.")
  print()

def showIdea():
  f = open("my.ideas", "r")
  ideas = f.read()
  f.close()

  ideas = ideas.split("\n")
  ideas.remove("")
  print(random.choice(ideas))

  
print("Ideas Storage")
print()

while True:
  choice = input("Add an idea or see a random idea? a/r.\n> ").strip().lower()
  print()
  if choice == "a" or choice == "r":
    break
  else:
    continue

if choice == "a":
  addIdea()
  
else:
  showIdea()
  
  