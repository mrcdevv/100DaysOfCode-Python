# Day 57 on Replit: "What Is Recursion?"

# Challenge section

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print("Factorial finder!")
print()

while True:
    try:
        number = int(input("Input a number > "))
        if number < 1:
            print("You must input a natural number  (1,2,3,4...)")
            print()
            continue
        print()
        break
    except:
        print("You must input a natural number  (1,2,3,4...)")
        print()


print(factorial(number))
