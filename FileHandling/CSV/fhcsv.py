import csv

with open(r'C:\Users\DELL\OneDrive\Desktop\dataFileHandling\data.csv', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

for row in data:
    print(row)
