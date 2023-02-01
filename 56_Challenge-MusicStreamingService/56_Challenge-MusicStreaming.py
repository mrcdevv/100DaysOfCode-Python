# Day 56 on Replit: "Challenge: Music Streaming Service"

# This program work well on Replit, but in my pc donesn´t. I don't know if it is because of "\xa0" inside the csv file or wath.

import os
import csv

with open("100MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file)
    for song in reader:
        if song["Artist(s)"] not in os.listdir():
            os.mkdir(song["Artist(s)"])

        filename = os.path.join(f"{song['Artist(s)']}/", f"{song['Song']}.txt")
        f = open(filename, "w")
        f.close()
