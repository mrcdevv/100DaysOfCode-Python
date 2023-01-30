# Day 48 on Replit: "File Writing"

# Fix my code section
# f = open("savedFoal.", "a")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close
# whatText = input("> ")
# f.write(f"{whatText}\n")

f = open("savedFile.txt", "a+")
whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")

f.close()

# Challenge section

print("HIGH SCORE TABLE")
print()

while True:
  initials = input("Input your initials > ").strip().upper()
  score = int(input("Input your score > "))
  print()

  f = open("high.score", "a+")
  f.write(f"{initials}\t{score}\n")
  f.close()

  again = input("Add another? y/n: ").strip().lower()[0]
  print()

  if again == "y":
    continue
  else:
    break