def sumList(l1, l2):
	newlist = []
	for i in range(len(l1)):
		row = []
		for j in range(len(l1[0])):
			row.append(l1[i][j] + l2[i][j])
		newlist.append(row)
	return newlist

def rowrev(l1):
	for row in l1:
		row.reverse()
	return l1

def colrev(l1):
	newlist = []
	for i in range(1, len(l1) + 1):
		newlist.append(l1[-i])
	return newlist

def add(l1, l2):
	total = 0
	for i in range(len(l1)):
		total += l1[i] * l2[i]
	return total

def issorted(l1):
	for i in range(len(l1) - 1):
		if l1[i] > l1[i + 1]:
			return False
	return True

def ezsort(l1):
	for i in range(len(l1)):
		for j in range(i + 1, len(l1)):
			if l1[j] > l1[i]:
				l1[j], l1[i] = l1[i], l1[j]
	return l1

def matrix(l1):
	row_sum = []
	for row in l1:
		row_sum.append(sum(row))
	#return row_sum

	coll = []
	for col in range(len(l1)):
		col_sum = 0
		for row in range(len(l1[0])):
			col_sum += l1[row][col]
		coll.append(col_sum)
	return coll




def main():
	l1 = [[1,2,3],[4,5,6],[7,8,9]]
	l2 = [[9,8,7],[6,5,4],[3,2,1]]
	#print(sumList(l1, l2))
	#print(rowrev(l1))
	#print(colrev(l1))
	print(matrix(l1))

main()