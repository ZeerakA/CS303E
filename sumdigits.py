def sum_digits(n):
	sum_num = 0
	while (n > 0):
		sum_num += (n % 10)
		n = n//10
	return sum_num

def main():
	a = eval(input("Enter number: "))
	b = sum_digits(a)

	while (b > 9):
		b = sum_digits(b)
	print()
	print(b)
main()


'''
def main():
	a = eval(input("Enter number: "))

	while (sum_digits(a) > 9):
		a = sum_digits(a)
	print()
	print(a)
main()
'''