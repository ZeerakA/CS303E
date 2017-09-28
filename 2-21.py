def main():
	n = eval(input("Enter a monthly saving amount: "))
	total = 0

	for i in range(1, 7):
		n = n * 1.00417
		total += n

	print ("Account value after sixth month is: ", total)

main()