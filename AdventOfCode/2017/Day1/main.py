'''
	main.py - Advent of Code 2017 Day 1

	http://adventofcode.com/2017/day/1
'''

import sys

def parseCmdArgs(argv):
	''' Parses arguments from command line '''
	if len(argv) != 3:
		print 'Error: improper command line args'

	filename = argv[1]

	if argv[2] == '-part1':
		part = 1
	elif argv[2] == '-part2':
		part = 2
	else:
		print 'Error: improper command line args'

	return filename, part

def getNumbers(filename):
	''' Reads filename for list of numbers '''
	filestream = open(filename)
	if not filestream:
		print 'Error: no file exists with this filename'

	numbers = filestream.read()
	numbers = numbers.strip(' ')
	numbers = numbers.strip('\n')
	return numbers

def sumNumbers(numbers, part):
	''' 
		Sums all digits in the numbers sequence that match 
		 the following digit in the sequence.
		The sequence is circular and if the final digit matches
		 the initial digit, add it to the sum.

		params:
			numbers - a string of digits

		returns:
			total - sum of the digits in the string that follow
			 the above rules
	'''

	length = len(numbers)
	total = 0

	# Append the numbers list to itself to make it 'circular'
	numbers = numbers + numbers

	if part == 1:
		offset = 1
	else:
		offset = length / 2

	for i in range(length):
		if not numbers[i].isdigit():
			# Houston we have a problem
			print 'Error: input file contains non-digit characters.'
			exit()

		if numbers[i] == numbers[i + offset]:
			total += int(numbers[i])

	return total



if __name__ == '__main__':
	filename, part = parseCmdArgs(sys.argv)
	numbers = getNumbers(filename)
	total = sumNumbers(numbers, part)
	print 'Sum:', total
	