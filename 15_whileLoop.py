# Day 15 on Replit: "All About Loops"

# Fix my code section

# counter = 0
# while counter < 25:
#   print(counter)

counter = 0
while counter < 25:
  print(counter)
  counter += 1

# counter = 0
# while counter >= 12:
#   print(counter)
#   counter += 1

counter = 0
while counter <= 12:
  print(counter)
  counter += 1


# Challenge section
exit = "no"

while exit != "yes":
  animal = input("What animal do you want?")

  if animal == "cow" or animal == "Cow":
    print("Moo")
  elif animal == "pig" or animal == "Pig":
    print("Oink")
  elif animal == "dog" or animal == "Dog":
    print("Woof")
  else:
    print("Mmm... Chirp Chirp")

  exit = input("Do you want to exit?: ")