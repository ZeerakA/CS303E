#  File: Benford.py

#  Description: 

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/23/2017

#  Date Last Modified: 04/24/2017

def main():
	# create an empty dictionary
	pop_freq = {}

	# initialize the dictionary
	for i in range(1, 10):
		pop_freq [str(i)] = 0

	# open file for reading
	in_file = open("./Census_2009.txt", "r")

	# read the header and ignore
	header = in_file.readline()

	count = 0 

	# read subsequent lines
	for line in in_file:
		line = line.strip()
		pop_data = line.split()
		# get the last element that is the population number
		pop_num = pop_data[-1]

		# make entries in the dictionary
		pop_freq[pop_num[0]] += 1
		count += 1

	# close the file
	in_file.close()

	# write out the result
	print("Digit\tCount\t%")
	for i in range(1, 10):
		print(str(i), end="")
		print("\t", end="")
		print(pop_freq[str(i)], end="")
		print("\t", end="")
		print(round(pop_freq[str(i)]/count * 100, 1))
main()