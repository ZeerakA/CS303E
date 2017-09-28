#  File: ISBN.py

#  Description: Opens file of ISBN numbers and creates another file to include if it's valid or not

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/10/2017

#  Date Last Modified: 04/12/2017

# Returns "output" as partial summed list
def partial_sum(original):
	output = []
	output.append(original[0])
	for i in range(len(original) - 1):
		output.append(output[i] + original[i+1])
	return output

def main():
	inFile = open("isbn.txt", "r")
	outFile = open("isbnOut.txt", "w")

	# Makes sure the isbn contains only X, x, -, and digits
	valid_inputs = ['X', 'x', '-']
	for i in range(10):
		valid_inputs.append(str(i))

	for line in inFile:
		isbn_digits = []
		digits_or_x = True

		line = line.rstrip("\n")

		for i in line:
			# Checks to make sure each line contains only digits and X and -
			if i not in valid_inputs:
				digits_or_x = False 
			# Changes value of X to 10
			if i == "X":
				i = "10"
			# Appends all digits of isbn to isbn_digits
			if i.isdigit():
				isbn_digits.append(int(i))

		# Calculates first partial sum
		s1 = partial_sum(isbn_digits)
		# Calculates second partial sum
		s2 = partial_sum(s1)

		# Valid isbn numbers where 2nd partial sum has to be divisble by 11
		# Also has to contain only digits, X, x, or "-"
		# Also contains a total of 9 digits + an X or another digit to equal 10 digits
		valid = (s2[-1] % 11 == 0) and digits_or_x and (len(isbn_digits) == 10)

		# Checks to see if the x is in the middle of the isbn
		#x_in_middle = (10 in isbn_digits[:-1])

		# Isbn is valid when it follows above qualities
		if valid:
			outFile.write(line + " valid \n")
		else:
			outFile.write(line + " invalid \n")

	inFile.close()
	outFile.close()
main()