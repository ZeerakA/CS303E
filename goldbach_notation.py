# File: Goldbach's Conjecture

# Description: Calculate all pairs of prime numbers that add up to lower_limit range of even input integers

# Student Name: Murray Lee

# Student UT EID: mwl647

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 03/05/2017

# Date Last Modified: 03/052017

def is_prime(n):
	limit = int(n ** 0.5) + 1

	if n == 1:
		return False

	divisor = 2
	prime_check = True
	while (divisor < limit):
		if (n % divisor == 0):
			prime_check = False
			break
		divisor += 1

	return (prime_check)

def main():
	lower_limit = eval(input("Enter the lower limit: "))
	upper_limit = eval(input("Enter the upper limit: "))

	while ((lower_limit < 4) or (lower_limit % 2 != 0) or (upper_limit % 2 != 0) or (lower_limit >= upper_limit)):
		lower_limit = eval(input("Enter the lower limit: "))
		upper_limit = eval(input("Enter the upper limit: "))

	for input_num in range(lower_limit, upper_limit + 1, 2):

		count = 0

		for test_prime in range(2, input_num // 2 + 1):
			if is_prime(test_prime) and is_prime(input_num - test_prime):
				count += 1

				if (count > 1):
					print(" =", test_prime, "+", input_num-test_prime, end="")
				else:
					print(input_num, "=", test_prime, "+", input_num-test_prime, end="")
		print()
main()

