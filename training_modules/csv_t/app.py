import csv

with open('file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for i in csvreader:
        print(' '.join(i))
