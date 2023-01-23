# Day 16 on Replit: "while True Loop"

# Fix my code section

# while true:
#   color = input("Enter a color: ")
#   if color = "red":
#   break
#   else:
#     print("Cool color!")
# print("I don't like red")

while True:
  color = input("Enter a color: ")
  if color == "red":
    break
  else:
    print("Cool color!")

print("I don't like red")


# Challenge section
print("Fill in the blank lyrics!")
counter = 0

while True:
    print("It´s your golden ____.")
    word = input("")
    if word == "hour":
        print("You get it! Beautiful song. You need", counter, "attemps")
        break
    else:
        print("Nope")
        print("")
        counter += 1



