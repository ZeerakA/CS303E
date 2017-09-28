
def main():
	# Open file for reading
	in_file = open("./grid.txt", "r")

	# Read the dimension of the grid
	dim = in_file.readline()
	dim = dim.strip()
	dim = int(dim)

	# Create an empty grid
	grid = []

	i = 0
	for line in in_file:
		i += 1
	print(i)


main()