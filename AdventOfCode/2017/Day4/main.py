'''
	main.py - Advent of Code 2017 Day 4

	http://adventofcode.com/2017/day/4
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

	text = filestream.read()
	text = text.split('\n')

	codes = []

	for line in text:
		codes.append(line.split(' '))

	return codes


def generateAlphabetDict():
	alphabet = {}
	for letter in range(97,123):
		alphabet[chr(letter)] = 0
	return alphabet


def generateHistogram(word):
	alphabet = generateAlphabetDict()
	for letter in word:
		alphabet[letter] += 1
	return alphabet


def checkForAnagrams(a, b):
	histogram_a = generateHistogram(a)
	histogram_b = generateHistogram(b)
	return histogram_a == histogram_b


def getValidCodeCount(codes, part):
	''' Gets total number of codes in code array that are valid '''
	total = 0

	for code in codes:
		valid = True
		for i in range(len(code)):
			for j in range(len(code)):
				if i == j:
					continue
				if part == 1:
					if code[i] == code[j]:
						valid = False
						break
				else:
					if checkForAnagrams(code[i], code[j]):
						valid = False
						break

			if not valid:
				break

		if valid:
			total += 1

	return total



if __name__ == '__main__':
	filename, part = parseCmdArgs(sys.argv)
	codes = readFile(filename)
	validCodes = getValidCodeCount(codes, part)
	print validCodes

	exit()

exit()
