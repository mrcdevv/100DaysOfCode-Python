mokeBeast = {"Name": None, "Type": None, "Special move": None, "HP": None, "MP": None}

while True:
  print("MokéBeast - The Non-Copyright Generic Beast Battle Game")
  print()

  for key in mokeBeast:
    mokeBeast[key] = input(f"{key}: ")

  print()
  print("-------------------")
  print()

  for key, value in mokeBeast.items():
    print(f"{key}: {value}")
