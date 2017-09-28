#  File: ISBN.py

#  Description: Opens file of ISBN numbers and creates another file to include if it's valid or not

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/10/2017

#  Date Last Modified: 04/10/2017

import string
'''
def find_s1_rec(isbn_digits, s1):
	if len(isbn_digits) == 0:
		return s1
	elif s1 == []:
		s1.append(isbn_digits[0])
		return find_s1_rec(isbn_digits[1:], s1)
	else:
		s1.append(str(int(s1[-1]) + int(isbn_digits[0])))
		return find_s1_rec(isbn_digits[1:], s1)
'''

def partial_sum(original, output):
	output.append(original[0])
	for i in range(len(original) - 1):
		output.append(output[i] + original[i+1])
	return output

def main():
	inFile = open("isbn.txt", "r")
	outFile = open("isbnOut.txt", "w")

	for line in inFile:

		isbn_digits = []
		line = line.rstrip("\n")

		for i in line:
			if i == "X":
				i = "10"
			if i.isdigit():
				isbn_digits.append(int(i))

		s1 = partial_sum(isbn_digits, [])
		s2 = partial_sum(s1, [])

		if s2[-1] % 11 == 0:
			outFile.write(line + " valid \n")
		else:
			outFile.write(line + " invalid \n")

	inFile.close()
	outFile.close()
main()