# Day 59 on Replit: "Challenge: Palindromes"

word = input("Input a word: ").strip().lower()
index = 0


def isPalindrome(wrd, index):
    lenght = len(wrd)
    middle = lenght // 2

    if index == middle:
        return True
    elif wrd[0 + index] == wrd[-1 - index]:
        return isPalindrome(wrd, index+1)
    else:
        return False


if isPalindrome(word, index):
    print("True")
else:
    print("False")
