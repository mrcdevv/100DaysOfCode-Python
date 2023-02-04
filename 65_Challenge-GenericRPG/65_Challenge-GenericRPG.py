# Day 65 on Replit: "Challenge: Generic RPG"

class character:
    name = None
    health = 100
    magicPoints = 100

    def __init__(self, name):
        self.name = name

    def print(self):
        print(
            f"""Name = {self.name}\nHealth = {self.health}\nMagic Points = {self.magicPoints}""")

    def setStats(self, health, xp):
        self.health = health
        self.magicPoints = xp


class player(character):
    name = "Player"
    nickname = None
    lives = None

    def __init__(self, nickname, lives):
        self.nickname = nickname
        self.lives = lives

    def print(self):
        print(f"""{self.name}\nNickname = {self.nickname}\nHealth = {self.health}\nMagic Points = {self.magicPoints}\nLives = {self.lives}""")

    def isAlive(self):
        if self.lives > 0:
            print("Alive? Yes")
        else:
            print("Alive? No")


class enemy(character):
    type = None
    strenght = None

    def __init__(self, name, type, strenght):
        self.name = name
        self.type = type
        self.strenght = strenght

    def print(self):
        print(f"""{self.name}\nHealth = {self.health}\nMagic Points = {self.magicPoints}\nLives = {self.lives}\nType = {self.type}\nStrength = {self.strenght}""")


class orc(enemy):
    speed = None
    type = "Orc"
    strenght = 200

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def print(self):
        print(f"""{self.name}\nHealth = {self.health}\nMagic Points = {self.magicPoints}\nType = {self.type}\nStrength = {self.strenght}\nSpeed = {self.speed}""")


class vampire(enemy):
    type = "Vampire"
    day = True
    strenght = 110

    def __init__(self, name, day):
        self.name = name
        self.day = day

    def print(self):
        print(f"""{self.name}\nHealth = {self.health}\nMagic Points = {self.magicPoints}\nType = {self.type}\nStrength = {self.strenght}""")

        if self.day:
            print("Day/Night? Day")
        else:
            print("Day/Night? Nigth")


print("Generic RPG")
print()

david = player("David", 2)
david.setStats(100, 50)
david.print()
print()

boris = vampire("Boris", False)
boris.setStats(45, 70)
boris.print()
print()

rishi = vampire("Rishi", True)
rishi.setStats(70, 10)
rishi.print()
print()

bill = orc("Orc", 23)
bill.setStats(60, 5)
bill.print()
print()

ted = orc("Ted", 46)
ted.setStats(75, 40)
ted.print()
print()
