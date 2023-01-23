# Day 17 on Replit: "Another Cheat"

# Fix my code section

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit
# print("The game is over, you've failed!")

while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")

# Challenge Section

print("ROCK - PAPER - SCISSORS v2")
print("""
----------------------------
""")

pointsPlayer1 = 0
pointsPlayer2 = 0

while True:
  print("Select your move (R, P or S)")
  player1 = input("Player 1: ")
  player2 = input("Player 2: ")
  
  if player1 == "R" and player2 == "S":
    print("Rock smashes scissors! Player 1 win a point!")
    pointsPlayer1 += 1
  elif player1 == "P" and player2 == "R":
    print("Paper covers rock! Player 1 win a point!")
    pointsPlayer1 +1
  elif player1 == "S" and player2 == "P":
    print("Scissors cut paper! Player 1 win a point!")
    pointsPlayer1 +1
  elif player2 == "R" and player1 == "S":
    print("Rock smashes scissors! Player 2 win a point!")
    pointsPlayer2 +1
  elif player2 == "P" and player1 == "R":
    print("Paper covers rock! Player 2 win a point!")
    pointsPlayer2 +1
  elif player2 == "S" and player1 == "P":
    print("Scissors cut paper! Player 2 win a point!")
    pointsPlayer2 +1
  else:
    print("Draw")

  if pointsPlayer1 == 3:
    winner = "Player 1"
    break
  elif pointsPlayer2 == 3:
    winner = "Player 2"
    break
  else:
    continue

print("")
print(winner, "is the winner!")