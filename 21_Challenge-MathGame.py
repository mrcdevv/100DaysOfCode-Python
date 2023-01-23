# Day 21 on Replit: "Challenge: Math Game"

print("Math Game!")

table = int(input("Choose a multiplication table: "))
points = 0

for i in range(1, 11):
  print(i, "x", table, "= ")
  multiplication = int(input(">"))
  
  if multiplication == (i * table):
    print("Great work!")
    print()
    points += 1
  else:
    print("Nope. The answer was", i * table)
    print()

print("You scored", points, "out of 10.")
