'''
	main.py - Advent of Code 2017 Day 2 - burnsnoss

	http://adventofcode.com/2017/day/2
'''

import sys

def parseCmdArgs(argv):
	''' Parses arguments from command line '''
	if len(argv) != 3:
		print 'Error: improper command line args'
		exit()

	filename = argv[1]

	if argv[2] == '-part1':
		part = 1
	elif argv[2] == '-part2':
		part = 2
	else:
		print 'Error: improper command line args'

	return filename, part



def readSpreadsheet(filename):
	''' Reads input spreadsheet tsv file, converts to int '''
	filestream = open(filename)
	if not filestream:
		print 'Error: no file exists with this filename:', filename
		exit()

	# Read it all in
	spreadsheet_txt = filestream.read()
	# Split sheet into rows
	spreadsheet_txt = spreadsheet_txt.split('\n')

	# Now split those rows into cols, 
	#  add each element to spreadsheet, 
	#   convert to int
	spreadsheet = []
	for i in range(len(spreadsheet_txt)):
		row = spreadsheet_txt[i].split('\t')
		spreadsheet.append([])
		for number in row:
			if not number.isdigit():
				print 'Error: Input file contains non-digit characters.'
				exit()
			spreadsheet[i].append(int(number))

	return spreadsheet


def getChecksum(spreadsheet, part):
	''' 
		Gets checksum by differencing maximum value and minimum
	     value in each row of spreadsheet, then summing the differences.
	'''

	checksum = 0

	for row in spreadsheet:
		if part == 1:
			# Part 1 - simple stuff
			maximum = max(row)
			minimum = min(row)
			difference = maximum - minimum
			checksum += difference
		else:
			# Part 2 - must do a row compare
			found = False
			for i in range(len(row)):
				for j in range(len(row)):
					if i == j:
						continue
					if row[i] % row[j] == 0:
						# We've got divisibility
						checksum += row[i] / row[j]
						found = True
						break
				if found:
					break

	return checksum


if __name__ == '__main__':
	filename, part = parseCmdArgs(sys.argv)
	spreadsheet = readSpreadsheet(filename)
	checksum = getChecksum(spreadsheet, part)

	print checksum

	exit()

exit()