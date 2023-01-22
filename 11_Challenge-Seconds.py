print("How many seconds are in a year?")
print("")
year = int(input("Enter a year: "))

monthsWith28 = 1
monthsWith30 = 4
monthsWith31 = 7
days = 365

secondsPerMinute = 60 
secondsPerHour = secondsPerMinute * 60
secondsPerDay = secondsPerHour * 24

secondsPerYear = (secondsPerDay * monthsWith28 * 28) + (secondsPerDay * monthsWith30 * 30) + (secondsPerDay * monthsWith31 * 31)

# Leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            days = 366
            print("WOW! Leap year")
            print("")
        else:
            print("Normal year")
            print("")
    else:
        days = 366
        print("WOW! Leap year")
        print("")
else:
    print("Normal year")
    print("")


if days == 366:
    secondsPerYear += secondsPerDay

print("There are ", secondsPerYear, " in the year ", year)





