import sys
import string

def readInput(filename):
	file_input = []

	with open(filename) as f:
		while True:
			char = f.read(1)
			if not char:
				print 'OH FUCK TITTIES FILES DUN BOYS'
				break
			elif char == ' ' or char == '\n':
				continue
			else:
				file_input.append(char)

	return file_input


def readMultiplier(instructions):

	# Set this boolean True while reading first number. If it's false, it will save letters in second number
	reading_n = True

	n = ''
	m = ''

	# Read until closed parentheses
	for letter in instructions:
		if letter == 'x':
			reading_n = False
		elif letter == ')':
			break
		else:
			if reading_n:
				n = n + letter
			else:
				m = m + letter

	return n, m


def multiply(instructions, n, m):
	section = ''
	result = ''

	for i in range(n):
		section = section + instructions[i]

	for j in range(m):
		result = result + section

	return result


def decompress(instructions):

	# Init some counters and markers
	i = 0
	end = len(instructions)

	# Init result variable
	result = ''

	while True:
		if i == end:
			break

		elif instructions[i] == '(':
			# We have found a multiplier. Three things:
			#  1. Read the multiplier 
			#  2. Apply multiplier to instructions and append to result
			#  3. Adjust i

			# Read Multiplier
			n, m = readMultiplier(instructions[i+1:])

			print n, m

			# Adjust i to account for multiplier
			i = i + len(n) + len(m) + 3

			# Apply multiplier to instructions
			result = result + multiply(instructions[i:], int(n), int(m))

			# Adjust i to account for n (length of multiplied section)
			i = i + int(n)

		else:
			result = result + instructions[i]
			i = i + 1

	return result
		


if __name__ == '__main__':

	instructions = readInput('input.txt')

	print len(instructions)

	result = decompress(instructions)

	# f = open('output.txt', 'w')
	# f.write(result)

	print len(result)

	# readChar(instructions[0])

	# for char in instructions:
	# 	if char == '(':
	# 		restOfFile, multiplier = readMultiplier(restOfFile)
	# 		answer += multiplier
	# 	else:
	# 		answer += char

