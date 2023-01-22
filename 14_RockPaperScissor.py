#Day 14 on Replit: "2 player 🪨📄✂️"

from getpass import getpass as input

print("ROCK - PAPER - SCISSORS")
print("""
----------------------------
""")

print("Select your move (R, P or S)")
player1 = input("Player 1: ")
player2 = input("Player 2: ")

if player1 == "R" and player2 == "S":
  winner = "Rock smashes scissors! Player 1 win!"
elif player1 == "P" and player2 == "R":
  winner = "Paper covers rock! Player 1 win!"
elif player1 == "S" and player2 == "P":
  winner = "Scissors cut paper! Player 1 win!"
elif player2 == "R" and player1 == "S":
  winner = "Rock smashes scissors! Player 2 win!"
elif player2 == "P" and player1 == "R":
  winner = "Paper covers rock! Player 2 win!"
elif player2 == "S" and player1 == "P":
  winner = "Scissors cut paper! Player 2 win!"
else:
  winner = "Draw"

print(winner)