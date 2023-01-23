# Day 7 on replit

# Fix my code section

# order = input(What would you like to order: pizza or hamburger? ")
# if order = "hamburger":
# print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#   print("You got it.")
# else: 
#     print("No cheese it is.")
# elif order == pizza:
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings = "yes"
#     print("We will add pepperoni.")
# else:
#   print"Your pizza will not have pepperoni.")

order = input("What would you like to order: pizza or hamburger? ")

if order == "hamburger":
    print("Thank you.")
    cheese = input("Do you want cheese?")
    if cheese == "yes":
        print("You got it.")
    else: 
        print("No cheese it is.")
elif order == "pizza":
    print("Pizza coming up.")
    toppings = input("Do you want pepperoni on that?")
    if toppings == "yes":
        print("We will add pepperoni.")
    else:
        print("Your pizza will not have pepperoni.")

# Day 7 challenge
print("Fake Fan Finder")
print("---------------")

favouriteAnime = input("What is your favourite Anime? ")

if favouriteAnime == "dbz":
  print("Oh wow! I love dbz too")
  favouriteCharacter = input("But wait, what is your favourite character?")
  if favouriteCharacter == "Goku":
    print("Same here")
    randomQuestion = input("What's Goku's wife's name? ")
    if randomQuestion == "Chi Chi":
      print("You´re a real fan")
    else:
      print("You´re a fake fan")
  elif favouriteCharacter == "Vegeta":
    print("It´s a valid option too")
    randomQuestion = "What's the highest Super Saiyan level attained by Vegeta in DBZ? "
    if randomQuestion == "Super Saiyan 2":
      print("You´re a real fan")
    else:
      print("You´re a fake fan")
  else:
    randomQuestion = input("What item is used to restore health? ")
    if randomQuestion == "Senzu bean":
      print("You´re a real fan")
    else:
      print("You´re a fake fan")
   