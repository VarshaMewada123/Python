import csv

with open(r'C:\Users\DELL\OneDrive\Desktop\dataFileHandling\data.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
