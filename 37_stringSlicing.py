# Day 37 on Replit: "String Slicing"

# Fix my code section

# This code should output 'Hello there'
# myString = "Hello there my friend."
# print(myString[0:10:0])

# This code should output 'Hello there'
myString = "Hello there my friend."
print(myString[0:11:1])

# Challenge section

print("STAR WARS NAME GENERATOR")

firstName = input("Enter your first name: ").strip()
secondName = input("Enter your second name: ").strip()
mumName = input("Enter your Mum´s first name: ").strip()
cityName = input("Enter the city where you were born: ").strip()

print(f"{firstName[:3].capitalize()}{secondName[:3]} {mumName[:2].capitalize()}{cityName[-3:]}")