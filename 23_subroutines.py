# Day 23 on Replit: "Subroutine"

# Fix my code section

# def print favorite color:
#   print("My favorite color is red.)

#   print favorite color()

def favoriteColor():
  print("My favorite color is red.")

favoriteColor()


# Challenge section

print("Login system")

def login():
  correctUsername = "MRC"
  correctPassword = "@mrcdevOnYT"
  
  while True:
    username = input("What is your username: ")
    password = input("Waht is your password: ")
  
    if username != correctUsername or password != correctPassword:
      print("I don´t recognise that username or password, try again")
      print()
      continue
    else:
      print("Welcome MRC!")
      break

login()