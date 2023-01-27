# Day 38 on Replit: "Strings And Loops"

# Challenge section

def changeColor(color):
  if color == 'red':
    return '\033[31m'
  elif color == "green":
    return '\033[32m'
  elif color == "yellow":
    return '\033[93m'
  elif color == "blue":
    return '\033[34m'
  elif color == "purple":
    return '\033[35m'
  else:
    return '\33[37m'

string = input("What sentence do you want rainbow-ising?\n> ")

for i in string:
  if i.lower() == "r":
    print(f"{changeColor('red')}", end = "")
  elif i.lower() == "b":
    print(f"{changeColor('blue')}", end = "")
  elif i.lower() == "g":
    print(f"{changeColor('green')}", end = "")
  elif i.lower() == "p":
    print(f"{changeColor('purple')}", end = "")
  elif i.lower() == " ":
    print(f"{changeColor('white')}", end = "")
  elif i.lower() == "y":
    print(f"{changeColor('yellow')}", end = "")
    
  print(i, end = "")
