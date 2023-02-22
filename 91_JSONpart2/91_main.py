import requests
import mrcdb
import os
import time

try:
    db = mrcdb.CSV_to_dict("jokes.csv")
except:
    db = {}


def clear_console(sec):
    time.sleep(sec)
    os.system("cls")


while True:
    response = requests.get("https://icanhazdadjoke.com/",
                            headers={"Accept": "application/json"})

    if response.status_code == 200:
        joke = response.json()

        print(joke["joke"])
        print()

        print("(s)ave joke, (l)oad old jokes, (n)ew joke, (e)xit")
        menu = input("> ")

        if menu == "s":
            key = joke["id"]
            db[key] = joke["joke"]
            mrcdb.dict_to_CSV("jokes.csv", db)

            print()
            print("Joke saved")
            clear_console(1)

        elif menu == "l":
            if db.keys() != ():
                for key in db.keys():
                    print()
                    print(db[key])

                clear_console(5)
            else:
                print("There is no saved joke")

        elif menu == "n":
            clear_console(1)
            continue

        elif menu == "e":
            clear_console(1)
            break

        else:
            print("You must enter a valid option")
            clear_console(1)
