import csv

inputfile = open('players200910.csv', 'rU')
csv_reader = csv.reader(inputfile)

outputfile = open('players2009100.csv', 'wb')
csv_writer = csv.writer(outputfile)

header = csv_reader.next()
csv_writer.writerow(header)

conversion = set(['-'])

for row in csv_reader:
	row = [x.replace('-', '0') if x == '-' else x for x in row]
	csv_writer.writerow(row)
	