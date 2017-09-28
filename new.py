def main():
	inFile = open("new1.txt", "r")
	line1 = inFile.readline()
	line2 = inFile.readline()
	line3 = inFile.readline()
	print(line1)
	print(line2)
	print(line3)
	print(repr(line1))

	infile.close()
main()