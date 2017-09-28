# File: Hailstone Sequence

# Description: Calculate the longest hailstone sequence cycle length in a range of numbers

# Student Name: Murray Lee

# Student UT EID: mwl647

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 02/25/2017

# Date Last Modified: 02/25/2017

def main():
	start_num = int(input("Enter starting number of the range: "))
	end_num = int(input("Enter ending number of the range: "))

	while start_num <= 0 or end_num <= 0 or start_num > end_num:
		start_num = int(input("Enter starting number of the range: "))
		end_num = int(input("Enter ending number of the range: "))	

	cycle_length = 0
	longest_num = 0
	for n in range(start_num, end_num + 1):
		count = 0
		number = n
		print(n, end='')

		while n > 1:
			if n % 2 == 0:
				n = n // 2
				print (" ", n, end='')
			else:
				n = 3 * n + 1
				print (" ", n, end='')
			count += 1

		if count > cycle_length:
			cycle_length = count
			longest_num = number


		print("      ", count)
	
	print()
	print("The number", longest_num, "has the longest cycle length of", cycle_length)	
main()