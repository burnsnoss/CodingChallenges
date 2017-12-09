import sys
import string


def readInput(filename):
	filestream = open(filename, 'r')

	current_string = ''
	IP = []
	IP_list = []

	for line in filestream:
		for letter in line:
			if letter == '[' or letter == ']':
				IP.append(current_string)
				current_string = ''
			elif letter == '\n':
				IP.append(current_string)
				IP_list.append(IP)
				IP = []
				current_string = ''
			else:
				current_string += letter

	return IP_list


def isABBA(code):
	for i in range(len(code)):
		if (len(code) - i) < 4:
			break
		else:
			if checkFour(code[i:i+4]):
				return True

	return False


def checkFour(letters):
	return (letters[0] == letters[3]) and (letters[1] == letters[2]) and (letters[0] != letters[1])


if __name__ == '__main__':
	input_array = readInput('input.txt')

	counter = 0
	supports_TLS = False
	TLS_counter = 0

	for line in input_array:
		if len(line) % 2 == 0:
			print 'ASSFUCk'
		for portion in line:
			if counter % 2 == 0:
				# This is an even numbered portion of the address, therefore we want there to be a ABBA here.
				if isABBA(portion):
					supports_TLS = True

				counter += 1

			else:
				# This is an odd portion, cannot be ABBA here, break if so.
				if isABBA(portion):
					supports_TLS = False
					counter = 0
					# print line
					break
					

			counter += 1

		if supports_TLS:
			TLS_counter += 1
			#supports_TLS = False
			# print line

		counter = 0

	
	print TLS_counter
