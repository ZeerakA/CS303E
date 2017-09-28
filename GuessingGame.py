#  File: GuessingGame.py

#  Description: Guesses a user inputted number between 1 and 100 using binary search

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/09/2017

#  Date Last Modified: 04/10/2017

def main():
	# Prints beginning information
	print("Guessing Game")
	print()
	print("Think of a number between 1 and 100 inclusive.")
	print("And I will guess what it is in 7 tries or less.")
	print()
	
	yes_no = input("Are you ready? (y/n): ")
	
	# Asks user to re-input answer if it's not "y" or "n"
	while yes_no != "y" and yes_no != "n":
		yes_no = input("Are you ready? (y/n): ")

	# Checks if input is yes or no, and then finds number in mind
	if yes_no == "n":
		print("Bye")
	elif yes_no == "y":
		# Binary search algorithm for numbers between 1 and 100
		lo = 1
		hi = 100
		mid = (lo + hi) // 2
		i = 1

		# Repeats process for each guess up to 7 guesses
		while i <= 7:
			print()

			print("Guess  " + str(i) + " :  The number you thought was " + str(mid))
			guess = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
			
			while (guess != 1) and (guess != -1) and (guess != 0):
				guess = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

			if guess == 1:
				hi = mid - 1
			elif guess == -1:
				lo = mid + 1
			elif guess == 0:
				print()
				print("Thank you for playing the Guessing Game")
				break
	
			mid = (lo + hi) // 2
			i += 1

		# User made a mistake or inputted incorrectly 
		if i > 7:
			print()
			print("Either you guessed a number out of range or you had an incorrect entry.")
			 
main()