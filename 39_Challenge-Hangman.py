# Day 39 on Replit: "Challenge Hangman"

import random, os, time

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

def clearConsole(sec):
  time.sleep(sec)
  os.system("clear")

word = random.choice(listOfWords)

wordLen = len(word)
wordBlank = "_" * wordLen

mylist = list(wordBlank)


lives = 6

while True:
  letter = input("Choose a letter: ").strip().lower()

  if letter in word:
    position = word.index(letter)

    mylist[position] = letter
    result = ''.join(mylist)
    
    print()
    print("Correct!")
    print()
    print(result)
    clearConsole(3)
  else:
    result = ''.join(mylist)
    print()
    print(result)
    print()
    print("Nope, not in there")
    lives -=1
    print("You have {lives} left".format(lives = lives))
    clearConsole(3)
  

  if lives < 1:
    print()
    print("You are dead!")
    break