def is_magic(b):
	#sum the first row
	canon_sum = 0
	for j in range(len(b[0])):
		canon_sum += b[0][j]

	#sum each row and compare with canon_sum
	for i in range(len(b)):
		sum_n = 0
		for j in range(len(b[i])):
			sum_n += b[i][j]
		if sum_n != canon_sum:
			return False

	#sum each column and compare with canon_sum
	for j in range(len(b[0])):
		sum_n = 0
		for i in range(len(b)):
			sum_n += b[i][j]
		if sum_n != canon_sum:
			return False

	#sum each diagonal and compare with canon_sum
	
def main():
	b = [[4,9,2], [3,5,7], [8,1,6]]
	print(is_magic(b))
main()