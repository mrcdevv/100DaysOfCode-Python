print("Exam Grade Calculator")
print("")

nameExam = input("Name of exam: ")
maxScore = int(input("Max possible score: "))
score = float(input("Your score: "))

scoreToPercentage = (score * 100) / maxScore

if scoreToPercentage <= 100 and scoreToPercentage >= 90:
    grade = "A+"
elif scoreToPercentage <= 89 and scoreToPercentage >= 80:
    grade = "A"
elif scoreToPercentage <= 79 and scoreToPercentage >= 70:
    grade = "B"
elif scoreToPercentage <= 69 and scoreToPercentage >= 60:
    grade = "C"
elif scoreToPercentage <= 59 and scoreToPercentage >= 50:
    grade = "D"
else:
    grade = "U"

print("You got %", scoreToPercentage, "which is a", grade)