def main():
	n = 0
	total = 0

	for i in range (1, 625):
		n = 1 / ((i ** 0.5) + ((i + 1) ** 0.5))
		total += n

	print (total)
main()