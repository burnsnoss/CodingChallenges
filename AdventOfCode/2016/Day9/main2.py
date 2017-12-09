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
	end = len(instructions)
	i = 0

	nm_list = []

	while True:
		if i == end:
 			break

 		elif instructions[i] == '(':
 			# Read n and m
 			n, m = readMultiplier(instructions[i])
 			# Adjust i to know when the multiplier ended, also store it for later
 			i += len(n) + len(m) + 3
 			j  = i
 			# Append to nm list
 			nm_list.append((n, m))

 		else:
 			# If we are n away from j and j isn't zero
 			if (i - j) == n and not (j == 0):
 				# Then we have a section of just letters to repeat
 				section = n * m
 				nm_list.pop()
 				if not (len(nm_list) == 0):
 					n, m = nm_list[-1]

 				else:



''' BETTER IDEA : RECRUSIVE FUNCTION THAT LOOKS AT EACH MULTIPLIER'S N-LENGTH SECTION.

iterate over this string:
i = 0
(12X3)(1X2)A(1X2)B
^
we find an instruction immediately. Read the instruction. n = 12, m = 3

n = 12; m = 3; i = 6
(12X3)(1X2)A(1X2)B
      ^
      find another instruction.

nm = [(12,3),(1,2)]; i = 11; j = 10
(12X3)(1X2)A(1X2)B
		   ^
		   here we'd find that the length of i - j = n (most recent n)
		   and we'd want to repeat this guy.
		   # characters total = n[-1] * m[-1] * m[-2]
		   pop (1,2) from nm

nm = [(12,3)]; i = 12; j = 

'''


# def decompress(instructions):

# 	# Init some counters and markers
# 	i = 0
# 	end = len(instructions)

# 	# Init result variable
# 	result = ''

# 	while True:
# 		if i == end:
# 			break

# 		elif instructions[i] == '(':
# 			# We have found a multiplier. Three things:
# 			#  1. Read the multiplier 
# 			#  2. Apply multiplier to instructions and append to result
# 			#  3. Adjust i

# 			# Read Multiplier
# 			n, m = readMultiplier(instructions[i+1:])

# 			print n, m

# 			# Adjust i to account for multiplier
# 			i = i + len(n) + len(m) + 3

# 			# Apply multiplier to instructions
# 			result = result + multiply(instructions[i:], int(n), int(m))

# 			# Adjust i to account for n (length of multiplied section)
# 			i = i + int(n)

# 		else:
# 			result = result + instructions[i]
# 			i = i + 1

# 	return result
		


if __name__ == '__main__':

	instructions = readInput('input.txt')

	print len(instructions)

	# result = decompress(instructions)

	# f = open('output.txt', 'w')
	# f.write(result)

	result = decompress

	# print result

	# readChar(instructions[0])

	# for char in instructions:
	# 	if char == '(':
	# 		restOfFile, multiplier = readMultiplier(restOfFile)
	# 		answer += multiplier
	# 	else:
	# 		answer += char

