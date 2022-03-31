import csv

with open('file.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ')
    for i in csvreader:
        if i != []:
            print(' - '.join(i))
