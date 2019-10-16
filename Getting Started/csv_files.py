import csv
# csv = "comma separated value"
# each value is a cell in an excel/datasheet file
with open ('my_file.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['one','two','three'])  # writerow accepts lists as parameter
    spamwriter.writerow(['four','five','six'])

with open ('my_file.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(','.join(row))  # connects the values in the list with whatever is in the quotes preceding .join