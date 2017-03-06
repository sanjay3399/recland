import sys
import csv

input = open(sys.argv[1], 'rb')
output = open(sys.argv[2], 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if any(row) and row[0] != 'first_name':
        writer.writerow(row)
input.close()
output.close()