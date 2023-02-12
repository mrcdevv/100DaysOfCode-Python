import csv


# Create a file
def createDb(filename):
    f = open(filename, "w")
    f.close()


# Convert a dictionary (nested in a list) to a csv file.
def dictInListToCsv(lst, filename):
    with open(filename, "w", newline="") as f:
        header = lst[0].keys()
        f = csv.DictWriter(f, header)
        f.writeheader()

        for row in lst:
            f.writerow(row)


# Convert a csv file to dictionary (nested in a list)
def csvToDictInList(filename):
    with open(filename, "r") as f:
        f = csv.DictReader(f)
        return list(f)


# Convert a 2d dictionary to a csv file. The 'firstKeyName' parameter is used to represent the name that should have all the keys inside the dictionary,e.g.
# {"david" : {"password": 14564564561, "email": "david149@gmail.com"}, "marc" : {"password": 727198125, "email": "marc756@hotmail.com"}}. In this case, all the keys are names.
def dict2DToCsv(dic, filename, firstKeyName):
    # Get headers
    header = [firstKeyName]
    for key, value in dic.items():
        for subKey in value:
            if subKey not in header:
                header.append(subKey)

    # Write and create the csv file
    with open(filename, "w", newline="") as f:
        f = csv.DictWriter(f, header)
        f.writeheader()
        row = {}
        for key, value in dic.items():
            row[firstKeyName] = key
            for subKey, subValue in value.items():
                row[subKey] = subValue
            f.writerow(row)


# Convert a csv file to a 2d dictionary
def cvsTo2DDict(filename, firstKeyName):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        records = {}
        for row in reader:
            firstValue = row[firstKeyName]
            innerDict = {}
            for key in row.keys():
                if key != firstKeyName:
                    innerDict[key] = row[key]
            records[firstValue] = innerDict
        return records


# Convert 1d dictionary to a csv file
def dictToCsv(dct, filename):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=dct.keys())
        writer.writeheader()
        writer.writerow(dct)


# Convert a csv file to a 1d dictionary
def csvToDict(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            return row
