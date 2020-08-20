import csv
with open("test.csv") as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    next(readcsv)
    for row in readcsv:
        print(row)

