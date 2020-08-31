import csv
with open('D:\Data\Python-poc\DevOps\emp.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)