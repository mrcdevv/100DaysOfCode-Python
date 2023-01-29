# Day 47 on Replit: "Challenge: Stats Battling game"

raikkonen = {"experiencie":99 ,"racecraft":92 ,"awareness":84 ,"pace":86}
gasly = {"experiencie":59 ,"racecraft":91 ,"awareness":99 ,"pace":89}
russell = {"experiencie":59 ,"racecraft":73 ,"awareness":99 ,"pace":82}
tsunoda = {"experiencie":43 ,"racecraft":88 ,"awareness":78 ,"pace":81}

racers = {"Kimi Raikkonen": raikkonen, "Pierre Gasly": gasly, "George Russell": russell, "Yuki Tsunoda": tsunoda}


def findRacer(choice):
  if choice == 1:
    return "Kimi Raikkonen"
  elif choice == 2:
    return "Pierre Gasly"
  elif choice == 3:
    return "George Russell"
  elif choice == 4:
    return "Yuki Tsunoda"

  
def findStat(choice):
  if choice == 1:
    return "experiencie"
  elif choice == 2:
    return "racecraft"
  elif choice == 3:
    return "awareness"
  elif choice == 4:
    return "pece"
    

print("Welcome to the Top Trumps 'Racers' Simulator")
print()

while True:
  print("Choose your card:\n1. Kimi Raikkonen\n2. Pierre Gasly\n3. George Russell\n4. Yuki Tsunoda")
  print()
  racer1 = int(input("Player 1 > "))
  racer2 = int(input("Player 2 > "))
  print()

  player1Racer = findRacer(racer1)
  player2Racer = findRacer(racer2)
  
  print("Choose your stat:\n1. Experiencie\n2. Racecraft\n3. Awareness\n4. Pace")
  print()
  stat = int(input("Choose one stat: "))
  print()
  
  playerStat = findStat(stat)

  print()

  print(f"{player1Racer} has a {playerStat} stat of {racers[player1Racer][playerStat]}")
  print(f"{player2Racer} has a {playerStat} stat of {racers[player2Racer][playerStat]}")
  print()

  if racers[player1Racer][playerStat] > racers[player2Racer][playerStat]:
    print(f"{player1Racer} 1 wins")
  elif racers[player1Racer][playerStat] < racers[player2Racer][playerStat]:
    print(f"{player2Racer} 1 wins")
  else:
    print("draw")

  print()
  again = input("Again? y/n: ").strip().lower()[0]

  if again == "y":
    continue
  elif again == "n":
    break
  else:
    print("I don´t get it. Bye")
    break
  