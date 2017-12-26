'''
	main.py - Advent of Code 2017 Day 6

	http://adventofcode.com/2017/day/6
'''

import sys
import Banks

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


def readFile(filename):
	''' Reads filename '''
	filestream = open(filename)
	if not filestream:
		print 'Error: no file exists with this filename:', filename
		exit()

	banks = filestream.read()
	banks = banks.split('\t')

	for i in range(len(banks)):
		banks[i] = int(banks[i])

	return banks




if __name__ == '__main__':
	filename, part = parseCmdArgs(sys.argv)
	banks_input = readFile(filename)
	banks = Banks.Banks(banks_input)

	configs = []
	reallocations = 0

	first_found = False

	while True:
		temp_config = banks.getConfiguration()
		configs.append(temp_config[:])

		index = banks.getMaxBankIndex()
		banks.redistribute(index)

		reallocations += 1

		if banks.getConfiguration() in configs:
			cycles = reallocations - configs.index(banks.getConfiguration())
			break
				

			# if first_found and banks.getConfiguration() in configs:
			# 	break
			# elif not first_found and banks.getConfiguration() in configs:
			# 	first_found = True
			# 	cycles_init = reallocation
			# 	temp_config = banks.getConfiguration()
			# 	first_found_config = temp_config[:]

		

	print 'Total reallocations:', reallocations
	print 'Cycles until repeat:', cycles

	exit()

exit()
