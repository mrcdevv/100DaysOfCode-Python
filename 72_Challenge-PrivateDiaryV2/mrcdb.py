import csv
# Create a file


# Transform a dictionary (nested in a list) to a csv file
def dictToCsv(lst, filename):
    with open(filename, "w") as f:
        header = lst[0].keys()
        f = csv.DictWriter(f, header)
        f.writeheader()

        for row in lst:
            f.writerow(row)


# Tranform a csv file to dictionary (nested in a list)
def csvToDict(filename):
    with open(filename, "r") as f:
        f = csv.DictReader(filename)
        return list(f)
