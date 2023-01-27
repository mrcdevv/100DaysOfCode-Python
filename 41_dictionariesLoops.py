# Day 41 on Replit: "Dictionaries With Loops"

# Fix my code section

# myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

# for name in myDictionary.items():
#   print(f"{name}:{value}")

#   if (name == "strength"):
#   if value > 100:
#     print("Whoa, SO STRONG")
#   else:
#     print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")

myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

for name, value in myDictionary.items():
  print(f"{name}:{value}")

  if (name == "strength"):
    if value > 100:
        print("Whoa, SO STRONG")
    else:
        print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")

# Challenge section

myDictionary = {"Name" : None, "URL": None, "Description" : None, "Rating": None}

for key in myDictionary:
  myDictionary[key] = input(f"{key}: ")

print()
print("-------------------")
print()

for key, value in myDictionary.items():
  print(f"{key}: {value}")