# Day 60 on Replit: "The Magic of Time...."

# Fix my code section

# import datetime

# today = datetime.today()

# holiday = datetime.date(year = 2022, day = 20)

# if holiday < today:
#   print("Coming soon")
# elif holiday > today:
#   print("Hope you enjoyed it")
# else:
#   print("HOLIDAY TIME!")

import datetime

today = datetime.date.today()

holiday = datetime.date(year=2022, day=20, month=11)

if holiday > today:
    print("Coming soon")
elif holiday < today:
    print("Hope you enjoyed it")
else:
    print("HOLIDAY TIME!")

# Challenge section


print("Event Countdown Timer")
print()
today = datetime.date.today()

name = input("Input the event: ")
year = int(input("Input the year: "))
month = int(input("Input the month: "))
day = int(input("Input the day: "))

event = datetime.date(year, month, day)

difference = event - today

if event > today:
    print(f"Coming soon ({difference.days} days)")
elif event < today:
    print("Did you enjoy it?")
else:
    print("It´s today!!")
