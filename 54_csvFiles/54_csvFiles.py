# Day 54 on Replit: "Comma-Separated Values"

# Fix my code section

import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
  
#   for row in reader: 
#     print (", ".join(row["Net Total"]))
#     total += row["Net Total"] 

# print(f"Total: {total}")

import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) 
  
  total = 0
  for row in reader: 
    print (row["Net Total"])
    total += float(row["Net Total"]) 

print(f"Total: {total}")

# Challenge section

import csv

print("Shop $$ Tracker")

total = 0

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for i in reader:
    total += float(i["Cost"]) * int(i["Quantity"])  

print(f"Your shop took £{round(total, 2)} pounds today.")
