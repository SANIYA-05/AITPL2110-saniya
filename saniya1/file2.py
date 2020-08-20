import csv
with open("test.csv") as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    next(readcsv)
    line=csv_file.readlines()
    for row in readcsv:
        next(readcsv)
        print(row)
