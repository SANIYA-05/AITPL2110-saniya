import csv
with open("states.csv") as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    for row in readcsv:
        next(readcsv)
        print(row)