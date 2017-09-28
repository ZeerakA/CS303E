# File: Hailstone Sequence

# Description: Calculate the longest hailstone sequence cycle length in a range of numbers

# Student Name: Murray Lee

# Student UT EID: mwl647

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 02/25/2017

# Date Last Modified: 02/25/2017

def main():
	#user input of starting and ending values
	start_num = int(input("Enter starting number of the range: "))
	end_num = int(input("Enter ending number of the range: "))

	#checking to make sure input values are positive and starting number is less than ending number
	while start_num <= 0 or end_num <= 0 or start_num > end_num:
		start_num = int(input("Enter starting number of the range: "))
		end_num = int(input("Enter ending number of the range: "))	

	#variables set to later calculate for the input number that has longest cycle length
	longest_cycle = 0
	longest_num = 0

	#cycle_lengths up the number of numbers in a hailstone sequence using cycle_length variable
	for n in range(start_num, end_num + 1):
		cycle_length = 0
		#sets a number variable so that the inputted number remains unchanged when used to compare to other input numbers
		input_number = n

		#changes value of input number to follow hailstone sequence and adds to cycle_length 
		while n > 1:
			if n % 2 == 0:
				n = n // 2
			else:
				n = 3 * n + 1
			cycle_length += 1

		#sets longest cycle length and number of it if the inputted number has larger cycle_length than previous number
		if cycle_length >= longest_cycle:
			longest_cycle = cycle_length
			longest_num = input_number

	print("The number", longest_num, "has the longest cycle length of", longest_cycle)	
main()