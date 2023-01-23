# Day 19 on Replit: "For Loop"

# Fix my code section

# total = 10
# while counter in range 100:
#   total += 10
#   print("total")

total = 10
while counter in range(100):
  total += 10
  print("total:", total)

# Challenge section

print("Loan calculator")
print()

money = 1000

for i in range(10):
  money = (money * 0.05) + money
  print("Year", i, "is", round(money, 2))