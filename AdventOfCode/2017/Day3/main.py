'''
	main.py - Advent of Code 2017 Day 3

	http://adventofcode.com/2017/day/3
'''

import sys

def parseCmdArgs(argv):
	''' Parses arguments from command line '''
	if len(argv) != 3:
		print 'Error: improper command line args'
		exit()

	number = int(argv[1])

	if argv[2] == '-part1':
		part = 1
	elif argv[2] == '-part2':
		part = 2
	else:
		print 'Error: improper command line args'

	return number, part
	



def findDistance(number):
	'''
		findDistance - finds the Manhattan distance of the cell
			corresponding to the number parameter to the central cell

		number: number of the cell to find distance of 
	'''

	if number < 1:
		print 'Invalid input number!'
		exit()

	if number == 1:
		return 1

	odd = 1
	ring = 0

	while True:
		odd += 2
		ring += 1
		hi = odd ** 2
		lo = ((odd - 2) ** 2) + 1

		if number >= lo and number <= hi:
			even = ring * 2
			break


	# print 'lo:\t', lo
	# print 'hi:\t', hi
	# print 'ring:\t', ring
	# print 'odd:\t', odd
	# print 'even:\t', even

	hi_dist = even
	lo_dist = ring

	current_dist = hi_dist
	n = hi

	distances = {}

	direction = 'decrease'

	while n <= hi and n >= lo:
		if n == number:
			return current_dist

		if direction == 'decrease':
			current_dist -= 1
		elif direction == 'increase':
			current_dist += 1

		if current_dist == lo_dist:
			direction = 'increase'
		if current_dist == hi_dist:
			direction = 'decrease'

		n -= 1

	return 'error :^)'


def addEmptyRing(grid):
	edgeLength = len(grid[0])

	edgeLength += 2

	grid.append([])
	grid.insert(0, [])
	for i in range(edgeLength):
		# Add a zero to the top and bottom rows
		grid[0].append(0)
		grid[len(grid)-1].append(0)
		if i != 0 and i != len(grid)-1:
			# add a cell to beginning and end of each middle row
			grid[i].append(0)
			grid[i].insert(0, 0)

	return grid
	

def getCellValue(grid, y, x, edge):
	'''
		getCellValue - sums up the adjacent cells 

		grid: the grid the cells come from
		y: y coordinate (I am looking at the grid as if the first quadrant
			of the cartesian plane is oriented like the fourth)
		x: x coordinate
		edge: length of the edge of the grid
	'''

	total = 0
	top, bottom, right, left = False, False, False, False
	if y - 1 >= 0:
		top = True
	if y + 1 <= edge - 1:
		bottom = True
	if x - 1 >= 0:
		left = True
	if x + 1 <= edge - 1:
		right = True

	# print top, bottom, left, right

	if top:
	# three cells above
		total += grid[y-1][x]
		if right:
			total += grid[y-1][x+1]
		if left:
			total += grid[y-1][x-1]
	# cell to the right
	if right:
		total += grid[y][x+1]
	# cell to the left
	if left:
		total += grid[y][x-1]
	# three cells below
	if bottom:
		total += grid[y+1][x]
		if right:
			total += grid[y+1][x+1]
		if left:
			total += grid[y+1][x-1]

	return total


def printGrid(grid):
	for line in grid:
		msg = ''
		for num in line:
			msg += str(num) + '\t'
		print msg
	return



def findCellSum(number):
	'''
		findCellSum - finds the first sum in problem sequence that
			is larger than number

		number: number to compare to progression of sums 
	'''
	if number < 1:
		print 'Invalid input number!'
		exit()

	if number == 1:
		return 2

	# Build the ole grid
	grid = [[1]]

	ring = 0

	while True: 
		grid = addEmptyRing(grid)
		ring += 1
		edge = len(grid[0])

		# Right edge
		x = edge - 1
		for y in range(edge-2, 0, -1):
			value = getCellValue(grid, y, x, edge)
			if value > number:
				# printGrid(grid)
				return value
			grid[y][x] = value

		# Top edge
		y = 0 
		for x in range(edge-1, 0, -1):
			value = getCellValue(grid, y, x, edge)
			if value > number:
				# printGrid(grid)
				return value
			grid[y][x] = value

		# Left edge
		x = 0
		for y in range(0, edge-1):
			value = getCellValue(grid, y, x, edge)
			if value > number:
				# printGrid(grid)
				return value
			grid[y][x] = value

		# Bottom edge
		y = edge - 1
		for x in range(0, edge):
			value = getCellValue(grid, y, x, edge)
			if value > number:
				# printGrid(grid)
				return value
			grid[y][x] = value
 

	print 'Error :^)'
	return grid



if __name__ == '__main__':
	number, part = parseCmdArgs(sys.argv)
	if part == 1:
		print ' --- PART 1 --- '
		print 'Input:', number
		distance = findDistance(number)
		print 'Distance:', distance
	elif part == 2: 
		print ' --- PART 2 --- '
		print 'Input:', number
		cellSum = findCellSum(number)
		print 'Cell Sum:', cellSum

	exit()

exit()
