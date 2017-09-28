def main():
	n = eval(input("Enter fibonnaci: "))

	a = 0
	b = 1
	total = a + b

	if n == 0 or n == 1:
		print (n)
	elif n > 1:
		for i in range(0, n - 1):
			total = a + b
			a = b
			b = total

	print (total)

main()