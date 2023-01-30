# Day 49 on Replit: "Reading from a file"

# Fix my code section

# while True:
#   contents = f.readline().strip()
  
#   print(contents)

f = open("file.txt", "r")
while True:
  contents = f.readline().strip()
  if contents == "":
    break
  print(contents)
f.close()

# Challenge section

print("HIGH SCORE TABLE")
print()

f = open("high.score", "r")
scores = f.read()
scores = scores.split("\n")
f.close()

name = ""
higher = 0

for item in scores:
  player = item.split()

  if item != "":
    if higher < int(player[1]):
      higher = int(player[1])
      name = player[0]
  
print(f"{name} have the highest score whit {higher} points")