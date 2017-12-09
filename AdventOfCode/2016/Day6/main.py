import sys
import string

def readInput(filename):
	filestream = open(filename, 'r')

	i = 0
	j = 0
	histogram_array = []

	for line in filestream:
		for letter in line:

			if j == 0 and letter != '\n':
				histogram_array.append(dict.fromkeys(string.ascii_lowercase, 0))

			if letter == '\n':
				i = 0
			else:
				histogram_array[i][letter] += 1
				i += 1

		j += 1

	return histogram_array

def getMaxs(hist_arr):
	max_arr = []
	for histogram in hist_arr:
		current_max = 0
		for letter in histogram:
			if histogram[letter] > current_max:
				current_max_letter = letter
				current_max = histogram[letter]

		max_arr.append(current_max_letter)

	return max_arr

def getMins(hist_arr):
	min_arr =[]
	for histogram in hist_arr:
		current_min = 9999999999
		for letter in histogram:
			if histogram[letter] < current_min and histogram[letter] != 0:
				current_min_letter = letter
				current_min = histogram[letter]

		min_arr.append(current_min_letter)

	return min_arr


if __name__ == '__main__':

	input_array = readInput('realinput.txt')
	maxs = getMins(input_array)
	print maxs