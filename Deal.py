# File: Deal.py

# Description: Calculate the probability of winning in the Monty Hall Problem from Let's Make a Deal

# Student Name: Murray Lee

# Student UT EID: mwl647

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 02/24/2017

# Date Last Modified: 02/25/2017

import random

def main():
	#number of rounds for game
	num_rounds = eval (input ("Enter the number of times you want to play: "))

	#formatting header for trials
	print()
	print(format("Prize", "12s"), end='')
	print(format("Guess", "12s"), end='')
	print(format("View", "12s"), end='')
	print(format("New Guess", "12s"))

	#number of wins
	switching_wins = 0

	#loop to calculate number of wins in inputted number of rounds
	for n in range(num_rounds):
		#randomly assigns number to prize door and to the door guessed
		prize = random.randint(1,3)
		guess = random.randint(1,3)

		#calculates the door that is opened up that is neither the prize nor the guessed door
		view = random.randint(1,3)
		while view == prize or view == guess:
			view = random.randint(1,3)

		#assigns new guess to the door that is neither the guessed door nor the viewed door
		newGuess = random.randint(1,3)
		while newGuess == guess or newGuess == view:
			newGuess = random.randint(1,3)

		#format to print each trial of door number of prize, guess, view, newGuess
		print(format(prize, "3d"), end='')
		print(format(guess, "12d"), end='')
		print(format(view, "11d"), end='')
		print(format(newGuess, "15d"))

		#counter for number of wins when switched
		if newGuess == prize:
			switching_wins += 1

	print()

	#calculates probability that you win when you switch doors and probability when you don't
	probability_switch = round(switching_wins / num_rounds, 2)
	probability_stay = 1 - probability_switch

	print("Probability of winning if you switch =", format(probability_switch, ".2f"))
	print("Probability of winning if you do not switch =", format(probability_stay, ".2f"))

main()