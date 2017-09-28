def main():
	dim = int(input("Enter odd number of rows/columns: "))
	while dim % 2 != 1:
		dim = int(input("Enter odd number of rows/columns: "))

	# create rows
	grid = []
	for i in range(dim):
		row = []
		for j in range(dim):
			row.append(0)
		grid.append(row)

	count = dim ** 2
	grid[dim // 2][dim // 2] = 1

	for i in range(dim // 2 + 1):
		# starting index
		x = i
		y = dim - 1 - i
		for j in range(dim - 1 - i * 2):
			grid[x][y - j] = count
			count -= 1

		# x = i
		y = i
		for j in range(dim - 1 - i * 2):
			grid[x + j][y] = count
			count -= 1

		x = dim - 1 - i
		# y = i
		for j in range(dim - 1 - i * 2):
			grid[x][y + j] = count
			count -= 1

		# x = dim - 1 = i
		y = dim - 1 - i
		for j in range(dim - 1 - i * 2):
			grid[x - j][y] = count
			count -= 1

	# print the result	
	for row in grid:
		for i in row:
			print('%02d' % i, end=" ")
		print()
main()
	