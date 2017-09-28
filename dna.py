#  File: DNA.py

#  Description: Outputs longest common sequence of two DNA strands in a text file

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 03/05/2017

#  Date Last Modified: 03/05/2017

import string
import math

def main():
	#opens file and reads first line to find how many pairs to count
	inFile = open ("dna.txt", "r")
	line1 = inFile.readline()
	number_of_comparisons = int(line1)


	for s in range(number_of_comparisons):
		#need to make sure to convert all to uppercase
		s1 = inFile.readline()
		s2 = inFile.readline()
		s1_strip = s1.strip()
		s2_strip = s2.strip()

		print("Pair", (s+1), end="")
		print(": ", end="")

		strand_first = s1_strip.upper()
		strand_second = s2_strip.upper()

		#finds shortest strand of dna and sets it
		if len(strand_first) == len(strand_second):
			minlength = strand_first
			maxlength = strand_second
		else:
			minlength = min(strand_first, strand_second, key=len)
			maxlength = max(strand_first, strand_second, key=len) 

		#counter for number of matching pairs
		count = 0
		a = []
		
		#starts from longest possible pair and goes down
		for i in range(len(minlength), 1, -1):

			#ends code when pair is found
			if count > 0:
				break

			#determines how many possible combinations in length of string
			for j in range(0, len(minlength) - i +1):

				#moves window of minlength in order
				if minlength[j:j+i] in maxlength:

					#spacing for multiple common sequences
					if count > 0:
						#removes identical sequences
						if minlength[j:j+i] in a:
							continue
						else:
							print("       ", minlength[j:j+i])
							a.append(minlength[j:j+i])
					#prints first sequence
					else:
						print(minlength[j:j+i])
						a.append(minlength[j:j+i])
						
					count += 1
		
		#prints no common sequence if no pairs are found
		if count == 0:
			print("No Common Sequence Found")

		print()

	inFile.close()

main()