def binarySearch(a, x):
	lo = 0
	hi = len(a) - 1
	while (lo <= hi):
		mid = (lo + hi) // 2
		if (x < a[mid]):
			hi = mid - 1
		elif (x > a[mid]):
			lo = mid + 1
		else:
			return mid
	return -1

def main():
	print(binarySearch([1,2,3,4,5], 6))
main()