#  File: DNA.py

#  Description:

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 03/05/2017

#  Date Last Modified: 03/05/2017

import string

def main():
	inFile = open ("dna.txt", "r")
	line1 = inFile.readline()
	number_of_comparisons = int(line1)

	total_seq = []

	for strand in range(number_of_comparisons):
		#need to make sure to convert all to uppercase
		s1 = inFile.readline()
		s2 = inFile.readline()
		strand_first = s1.upper()
		strand_second = s2.upper()

		count = 0
		maxcount = 0
		seq = ""
		minlength = 0
		maxlength = 0

		if len(strand_first) > len(strand_second):
			maxlength = len(strand_second)
		else:
			maxlength = len(strand_first)

		for i in range(len(strand_first)):
			for j in range(len(strand_second)):

				count = 0
				same_length_count = 0

				if i > j:
					minlength = maxlength - (i+1)
				else:
					minlength = maxlength - (j+1)

				for k in range(minlength):
					if strand_first[i+k] == strand_second[j+k]:
						count +=1
					else:
						count = 0
						break
					if count >= maxcount:
						maxcount = count
						seq = strand_first[i:i+k+1]



			if seq == "":
				seq = "No Common Sequence Found"
							
		total_seq.append(seq)

	inFile.close()

	print("Longest Common Sequences")

	for i in range(len(total_seq)):
		print("Pair", i+1, ":", total_seq[i])


	


main()