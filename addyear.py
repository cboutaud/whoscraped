import csv

inputfile = open('players2.csv', 'rU')
csv_reader = csv.reader(inputfile)

outputfile = open('players200910.csv', 'wb')
csv_writer = csv.writer(outputfile)

header = csv_reader.next()
header.append("season")
csv_writer.writerow(header)

for row in csv_reader:
	row.append("2009-10")
	csv_writer.writerow(row)

