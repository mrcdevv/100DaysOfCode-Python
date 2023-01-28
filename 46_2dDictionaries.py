# Day 46 on Replit: "2D Dictionaries"

# Fix my code section

# john = {"daysCompleted": 46, "streak": 22}
# janet = {"daysCompleted": 21, "streak": 21}
# erica = {"daysCompleted": 75, "streak": 6}

# courseProgress = {"John":john, "Janet":janet, "Erica":erica}

# print(courseProgress["erica"]["daysCompleted"])
# print(courseProgress["Janet"]["Streak"])

john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
print(courseProgress["Janet"]["streak"])

# Challenge section

print("MokéDex")

mokeDex = {}

def prettyPrint():
  print()
  print("NAME | TYPE | MOVMENT | HP | MP")
  for key, value in mokeDex.items():
    print(key, end =" | ")
    for subKey, subValue in value.items():
      print(subValue, end = " | ")

while True:
  name = input("Input the beast name: ").strip().capitalize()
  type = input("Input the beast element: ").strip().capitalize()
  movment = input("Input the beast special move: ").strip().capitalize()
  HP = input("Input the beast starting HP: ").strip()
  MP = input("Input the beast starting MP: ").strip()

  print("-"*10)

  mokeDex[name] = {"type": type, "movment": movment, "hp": HP, "mp": MP}

  prettyPrint()

  print()
  again = input("Again? y/n").strip().lower()

  if again == "y":
    continue
  elif again == "n":
    break
  else:
    print("I don´t get it. Bye")
    break
    

  