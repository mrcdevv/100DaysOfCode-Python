# Day 40 on Replit: "Dictionaries"

# Fix my code section

# myUser = {name:"Andy", "age":128, "age" = 129}
# print(myUser{"name"})

myUser = {"name" : "Andy", "age": 128, "age" : 129}
print(myUser["name"])

# Challenge section

print("Contact Card")

name = input("Name: ").strip().capitalize()
dob = input("Date of Birth:").strip()
tel = int(input("Telephone number:")).strip()
email = input("Email: ").strip()
address = input("Address: ").strip()

myContacts = {"name":name, "dob":dob, "tel":tel, "email":email, "address":address}

print()
print("-------------------------------")
print()

print(f"""Hi {myContacts['name']}. Our dictionary says that you were born on {myContacts['dob']}, we can call you on {myContacts['tel']}, email {myContacts['email']}, or write to {myContacts['address']}.""")
