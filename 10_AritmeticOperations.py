# Day 10 on Replit

# Fix my code section

# Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
# 3.4 * 6.8
print("Multiplication: ", round(3.4 * 6.8, 2))

# division
# 2467 / 4673
print("Division: ", round(2467 / 4673, 2))

#raise 10 to the power of 2
print("Squared: ", 10 ** 2)

# print the remainder when 343 is divided by 4
# print("343 // 100")
print("Reminder: ", 343 % 4) 



# Day 10 challenge 
print("Tip calculator")

myBill = float(input("How much did you spend? "))
tipPercentage = int(input("What percentage do you want to tip? "))
numberOfPeople = int(input("How many people in your group"))

tipMoney = ( tipPercentage * myBill ) / 100
totalPerPerson = round((tipMoney + myBill) / numberOfPeople, 2)


print("")
print("You each owe $", totalPerPerson)