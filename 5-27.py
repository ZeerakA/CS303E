def main():
	pi = 0
	for i in range (10001, 100002, 10000):
		for j in range (1, i):
			pi = pi + (4 * ((-1)**(j+1) / (2*j-1)))
		print (pi)
		pi = 0
main()