import sys
import string


def generateLCD(w, h):
	lcd = []
	row = []

	for i in range (h):
		row = []
		for i in range(w):
			row.append('.')

		lcd.append(row)

	return lcd


def rotateRow(y, offset, lcd, w):
	offset = offset % w
	temp1 = ''
	temp2 = ''
	for o in range(offset):
		for n in range(w):
			if n == 0:
				# need to switch very last column pixel with this first pixel
				temp1 = lcd[y][n]
				lcd[y][n] = lcd[y][w-1]
				continue

			# now, store next pixel down in temp2, and put temp1 into next pixel slot
			temp2 = lcd[y][n]
			lcd[y][n] = temp1
			temp1 = temp2

	return lcd


def rotateColumn(x, offset, lcd, h):
	offset = offset % h
	temp1 = ''
	temp2 = ''
	for o in range(offset):
		for n in range(h):
			if n == 0:
				# need to switch very last column pixel with this first pixel
				temp1 = lcd[n][x]
				lcd[n][x] = lcd[h-1][x]
				continue

			# now, store next pixel down in temp2, and put temp1 into next pixel slot
			temp2 = lcd[n][x]
			lcd[n][x] = temp1
			temp1 = temp2

	return lcd
	

def rectangle(x, y, lcd):
	for i in range(y):
		for j in range(x):
			lcd[i][j] = '#'

	return lcd


def printLCD(lcd):
	for row in lcd:
		rowString = ''
		for item in row:
			rowString += item

		print rowString


def countLCD(lcd):
	count = 0
	for row in lcd:
		for pixel in row:
			if pixel == '#':
				count = count + 1

	print count


def getInstructions(filename):
	filestream = open(filename, 'r')

	instructionSet = []
	instruction = []

	for line in filestream:
		strippedLine = line.strip('\n')
		splitLine = strippedLine.split(' ')
		if splitLine[0] == 'rect':
			instruction.append('rect')
			coords = splitLine[1].split('x')
			instruction.append(int(coords[0]))
			instruction.append(int(coords[1]))
			# print instruction
		elif splitLine[0] == 'rotate':
			if splitLine[1] == 'column':
				instruction.append('rc')
				coords = splitLine[2].split('=')
				instruction.append(int(coords[1]))
				instruction.append(int(splitLine[4]))
				# print instruction
			elif splitLine[1]  == 'row':
				instruction.append('rr')
				coords = splitLine[2].split('=')
				instruction.append(int(coords[1]))
				instruction.append(int(splitLine[4]))
				# print instruction

		instructionSet.append(instruction)
		instruction = []
		coords = []

	return instructionSet


if __name__ == '__main__':

	w = 50
	h = 6

	lcd = generateLCD(w, h)
	instructions = getInstructions('input.txt')
	
	for line in instructions:
		if line[0] == 'rect':
			lcd = rectangle(line[1], line[2], lcd)
		elif line[0] == 'rr':
			lcd = rotateRow(line[1], line[2], lcd, w)
		elif line[0] == 'rc':
			lcd = rotateColumn(line[1], line[2], lcd, h)

	printLCD(lcd)
	countLCD(lcd)
	