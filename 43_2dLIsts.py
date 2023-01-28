# Day 43 on Replit: "Take Your List To A New Dimension"

# Fix my code section

# my2DList =  ["Johnny", 21, "Mac"],
#              ["Sian" 19, "PC"]
#              ["Gethin", 17, "PC"], ]

# print(my2DList[0][1])

my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"], ]

print(my2DList[0][1])


# Challenge section

import random

print("Bingo Card Generator!")
print()

rows, cols = 3, 3
bingo = [[None for i in range(cols)] for j in range(rows)]

def prettyPrint():
  for i in bingo:
    print(i)

numbers = []
index = 0

for i in range(8):
  ran = random.randint(1, 90)
  numbers.append(ran)

numbers.sort()

for i in range(3):
  for j in range(3):
    if i == 1 and j == 1:
      bingo[i][j] = "BINGO"
    else:
      bingo[i][j] = numbers[index]
      index += 1

prettyPrint()
