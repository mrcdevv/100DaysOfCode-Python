# Day 9 on Replit

# Fix my code section

# score = input("What was your score on the test?"))
# if score >= 80
#   print("Not too shabby")
# elif score > "70":
#   print("Acceptable.")
# else:
# print("Dude, you need to study more!")

score = int(input("What was your score on the test?"))
if score >= 80:
  print("Not too shabby")
elif score > "70":
  print("Acceptable.")
else:
  print("Dude, you need to study more!")


# Day 9 challenge

print("Generation Identifier")
print("")

date = int(input("Which year were you born?"))

if date >= 1883 and date < 1901:
  print("Lost generation")
elif date >= 1901 and date < 1928:
  print("Greatest generation")
elif date >= 1928 and date < 1946:
  print("Silent generation")
elif date >= 1946 and date < 1965:
  print("Baby Boomers")
elif date >= 1965 and date < 1981:
  print("Generation X")
elif date >= 1981 and date < 1997:
  print("Millenials")
elif date >= 1997 and date < 2012:
  print("Generation Z")
elif date >= 2012 and date <= 2023:
  print("Generation alpha")
else:
  print("Did you come from the past or the future?")
