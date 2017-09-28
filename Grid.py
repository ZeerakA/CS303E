#  File: Grid.py

#  Description: Open grid file to find maximum product of adjacent 4 numers

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/17/2017

#  Date Last Modified: 04/17/2017

def main():
	# Open file for reading
	in_file = open("./grid.txt", "r")

	# Read the dimension of the grid
	dim = in_file.readline()
	dim = dim.strip()
	dim = int(dim)

	# Create an empty grid
	grid = []

	# Populate the grid
	for line in range(dim):
		line = in_file.readline()
		line = line.strip()
		row = line.split()

		for j in range(dim):
			row[j] = int(row[j])
		grid.append(row)

	# Close the file
	in_file.close()

	# Maximum product of row sums
	row_max = 0
	prod_all = []

	# Read and multiply in blocks of four along rows
	for row in grid:
		for i in range(dim - 3):
			prod = 1
			for j in range(i, i + 4):
				prod = prod * row[j]
			if prod > row_max:
				row_max = prod
			prod_all.append(prod)
	#print(max(prod_all))
	#print(row_max)

	# Find maximum of column sums
	col_max = 0
	col_sums = []

	# Read and multiply in blocks of four along columns
	for j in range(dim):
		for i in range(dim - 3):
			prod = 1
			for k in range(i, i + 4):
				prod = prod * grid[k][j]
			if prod > col_max:
				col_max = prod
			col_sums.append(prod)
	#print(col_max)
	#print(max(col_sums))

	# Find maximum of left diagonal sums
	left_diagonal_max = 0
	left_diagonal_sums = []

	# Read and multiply in blocks of four along left diagonal
	for i in range(dim - 3):
		for j in range(dim - 3):
			prod = 1
			for k in range(4):
				prod = prod * grid[k + i][k + j]
			if prod > left_diagonal_max:
				left_diagonal_max = prod
			left_diagonal_sums.append(prod)
	#print(left_diagonal_max)
	#print(max(left_diagonal_sums))

	# Find maximum of right diagonal sums
	right_diagonal_max = 0
	right_diagonal_sums = []

	# Read and multiply blocks of four along right diagonal
	for i in range(dim - 3):
		for j in range(dim - 3):
			prod = 1
			for k in range(3, -1, -1):
				prod = prod * grid[i + 3 - k][k + j]
			if prod > right_diagonal_max:
				right_diagonal_max = prod
			right_diagonal_sums.append(prod)
	#print(right_diagonal_max)
	#print(max(right_diagonal_sums))

	# Calculate greatest max of row, columnn, and diagonal sums
	greatest_product = max(row_max, col_max, left_diagonal_max, right_diagonal_max)

	print("The greatest product is", greatest_product)
				

main()

