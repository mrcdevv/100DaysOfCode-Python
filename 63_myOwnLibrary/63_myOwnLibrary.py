# Day 63 on Replit: "Multiple Files"

# Fix my code section

# ## test.py file ##############
# import random

# num = randint(10,100)

# def countdown():
#   for i in range(num):
#     print(i+1)

# countdown()
# ### main.py file ###############

# import tt

# print("Countdown")
# countdown()

## test.py file ##############
import test as tt
import random

num = random.randint(10, 100)


def countdown():
    for i in range(num):
        print(i+1)


countdown()
### main.py file ###############


print("Countdown")
tt.countdown()
