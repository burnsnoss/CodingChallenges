'''
	main.py - Advent of Code 2017 Day 5

	http://adventofcode.com/2017/day/5
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


def readFile(filename):
	''' Reads filename '''
	filestream = open(filename)
	if not filestream:
		print 'Error: no file exists with this filename:', filename
		exit()

	offsets = filestream.read()
	offsets = offsets.split('\n')

	for i in range(len(offsets)):
		offsets[i] = int(offsets[i])

	return offsets


def navigateOffsets(offsets):
	''' Gets number of turns/jumps it takes to navigate out of offset list '''
	index = 0
	jumps = 0
	while index >= 0 and index < len(offsets):
		# Get current length to move
		current_offset = offsets[index]
		# Increase current offset by 1
		if part == 2 and offsets[index] >= 3:
			offsets[index] -= 1
		else:
			offsets[index] += 1
		# Add offset to index
		index += current_offset
		# Increment number of jumps
		jumps += 1

	return jumps


if __name__ == '__main__':
	filename, part = parseCmdArgs(sys.argv)
	offsets = readFile(filename)
	jumps = navigateOffsets(offsets)
	print 'Number of jumps:', jumps

	exit()

exit()
