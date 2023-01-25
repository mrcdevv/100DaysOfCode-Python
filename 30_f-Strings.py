# Day 30 on Replit: "f-strings"

# Fix my code section

# food = pizza"
# location = "beach"
# color = "green"
# friend = "Quinn"

# "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." format(food=food, location=location, color=color,)

# print(response)

food = "pizza"
location = "beach"
color = "green"
friend = "Quinn"

response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame.".format(food=food, location=location, color=color, friend=friend)

print(response)


# Challenge section

print("30 Days Down - What did you think?")
print()

for i in range(1, 31):
  response = input(f"Day {i}:\n")
  print()

  text = f"You thought Day {i} was"

  print(f"{text: ^50}")
  print(f"{response: ^50}")
  print()

