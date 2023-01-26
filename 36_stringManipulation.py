# Day 36 on Replit: "String Manipulation"

# Fix my code section

# whatToEat = input("What do you fancy for dinner? ")
# if whatToEat.strip = "pasta": 
#   print("Get out the pasta maker.")
# elif whatToEatlower() == "TACOS":
#   print("Let's do Taco Tuesday!")
# else: 
#   print("Go search the fridge.")

whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip().lower() == "pasta": 
  print("Get out the pasta maker.")
elif whatToEat.strip().lower() == "tacos":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")


# Challenge section
names = []

def show():
  print()
  for i in names:
    print(i)
  print()

while True:
  name = input("First name: ").strip().capitalize()
  surname = input("Last name: ").strip().capitalize()
  fullname = name + " " + surname

  if fullname not in names:
    names.append(fullname)
  else:
    print("Error: Duplicate name!")

  show()
  
