# File: Goldbach's Conjecture

# Description: Calculate all pairs of prime numbers that add up to a range of even input integers

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
	primecheck = True
	while (divisor < limit):
		if (n % divisor == 0):
			primecheck = False
			break
		divisor += 1

	return (primecheck)

def main():
	a = eval(input("Enter the lower limit: "))
	b = eval(input("Enter the upper limit: "))

	while ((a < 4) or (a % 2 != 0) or (b % 2 != 0) or (a >= b)):
		a = eval(input("Enter the lower limit: "))
		b = eval(input("Enter the upper limit: "))

	for i in range(a, b + 1, 2):

		count = 0

		for j in range(2, i // 2 + 1):
			if is_prime(j) and is_prime(i - j):
				count += 1

				if (count > 1):
					print(" =", j, "+", i-j, end="")
				else:
					print(i, "=", j, "+", i-j, end="")
		print()
main()

