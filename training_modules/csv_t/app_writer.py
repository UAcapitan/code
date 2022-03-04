import csv

with open('file.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
    csvwriter.writerow(['Test1', 'Test2', 'Test3'])
    csvwriter.writerow(['Test4', 'Test5', 'Test6'])
    csvwriter.writerow(['Test7', 'Test8', 'Test9'])