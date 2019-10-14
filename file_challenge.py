import csv

names = input("Enter names: ")
colors = input("Enter favorite colors: ")

names = names.split(', ')
colors = colors.split(', ')

with open('test_file.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(names)
    csvwriter.writerow(colors)

with open('test_file.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(','.join(row))