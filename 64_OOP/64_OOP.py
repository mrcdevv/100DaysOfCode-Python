# Day 64 on Replit: "OOP"

# Fix my code section


# Challenge section

# class animal:
#   species = None
#   name = None
#   sound = None

#   def __init__(name, species, sound):
#     self.name = name
#     self.species = species
#     self.sound = sound

# class bird():

#  def __init__():
#     self.name = "Bird"
#     self.species = "Avian"
#     self.sound = "Tweet"


# cow = animal("Ermintrude", "Bo Taurus", "Moo")
# print(cow.sound)
# print(cow.color)

# polly = bird("Green")
# polly.talk()
# print(polly.color)


class animal:
    species = None
    name = None
    sound = None

    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound


class bird(animal):
    color = None

    def __init__(self, color):
        self.name = "Bird"
        self.species = "Avian"
        self.sound = "Tweet"
        self.color = color

    def talk(self):
        print(f"I'm a {self.name} and I do {self.sound}")


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)

polly = bird("Green")
polly.talk()
print(polly.color)


# Challenge section

class job:
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def printInfo(self):
        print(
            f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}")


class doctor(job):
    experience = None
    speciality = None

    def __init__(self, experience, speciality):
        self.name = "Doctor"
        self.salary = "Doing very nicely thank you"
        self.hoursWorked = "50"
        self.experience = experience
        self.speciality = speciality

    def printInfo(self):
        print(f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}\nSpeciality: {self.speciality}\nYears of experience: {self.experience}")


class teacher(job):
    subject = None
    position = None

    def __init__(self, subject, position):
        self.name = "Teacher"
        self.salary = "Nowhere near enough"
        self.hoursWorked = "All of them"
        self.subject = subject
        self.position = position

    def printInfo(self):
        print(f"Job type: {self.name}\nSalary: ${self.salary}\nHours worked: {self.hoursWorked}\nSubject: {self.subject}\nPosition: {self.position}")


lawyer = job("Lawyer", "Squillions", 60)
lawyer.printInfo()
print()

teacher = teacher("Computer Science", "Classrom Teacher")
teacher.printInfo()
print()

doctor = doctor(7, "Pediatric Consultant")
doctor.printInfo()
print()
