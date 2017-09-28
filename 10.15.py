def main():

	s = input("Enter a list: ")
	items = s.split()
	list1 = [eval(x) for x in items]
	
	if isSorted(list1):
		print("The list is already sorted")
	else:
		print("The list is not sorted")

def isSorted(lst):
	lstCopy = list(lst)
	lst.sort()

	if lstCopy == lst:
		return True
	else:
		return False


main() 