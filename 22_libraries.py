# Day 22 on Replit: "Libraries"

import random

# Fix my code section

# myNumber = .randint(1, 10)
# for i in range(10):
#   print(myNumber)

for i in range(10):
    myNumber = random.randint(1, 10)
    print(myNumber)

# Challenge section

print("Guess the Number ( 1 - 100 ) v2")
print("")

correctNumber = random.randint(1, 100)
choice = int(input("What is your guess? (1-100) "))
dontFollowRules = 1
wrong = 1

while choice != correctNumber:
  if choice < 1 or choice > 100:
    if dontFollowRules == 3:
      print("I´m done")
      exit()
    
    dontFollowRules += 1
    print("A number between 1 and 100")
    print("")
    continue

  if choice == correctNumber:
    print("Correct!")
    print("")
    break
  elif choice < correctNumber:
    print("My number is higher")
    print("")
  else:
    print("My number is lower")
    print("")

  wrong += 1
  choice = int(input("What is your guess? (1-100) "))
  

print("You need", wrong, "attempls to guess my number")