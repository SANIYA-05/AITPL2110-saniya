import csv
with open("metropolitan cities.csv") as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    for row in readcsv:
        print(row)