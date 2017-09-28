#  File: Grid.py

#  Description: Open grid file to find maximum product of adjacent 4 numers

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/17/2017

#  Date Last Modified: 04/19/2017

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

	# Max product is the maximum product of whole grid
	max_prod = 1

	for i in range(dim):
		for j in range(dim):
			# Row Product
			row_prod = 1
			# Column Product
			col_prod = 1
			# Left Diagonal Product
			L_diag = 1 
			# Right Diagonal Product
			R_diag = 1

			for k in range(4):
				if i < dim and j < (dim - 3):
					row_prod = row_prod * grid[i][j + k]
				if i < (dim - 3) and j < dim:
					col_prod = col_prod * grid[i + k][j]
				if i < (dim - 3) and j < (dim - 3):
					L_diag = L_diag * grid[i + k][j + k]
					R_diag = R_diag * grid[i + k][j + 3 - k]

			# Calculates maximum product
			current_max = max(row_prod, col_prod, L_diag, R_diag)
			if current_max > max_prod:
				max_prod = current_max

	print("The greatest product is", max_prod)

main()