# Day 20 on Replit: "What can range really do?"

# Fix my code section

# while i in range (20, 40, -1):
#   print(i)

while i in range (20, 40, 1):
  print(i)

# Challenge section

print("List generator")

start = int(input("Start at: "))
increment = int(input("Increment between values: "))
end = int(input("End at:"))

for i in range(start, end+1, increment):
  print(i)