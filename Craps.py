# File: Craps.py

# Description: Calculate the probability of winning at Craps

# Student Name: Murray Lee

# Student UT EID: mwl647

# Course Name: CS 303E

# Unique Number: 51850

# Date Created: 02/18/2017

# Date Last Modified: 02/19/2017

import random

# simulate a single round of craps and
# return 1 if player wins and 0 if he loses
def craps():
	dice1 = random.randint(1,6)
	dice2 = random.randint(1,6)
	# total of first roll of dice
	total_dice1 = dice1 + dice2

	# come out roll
	if (total_dice1 == 7 or total_dice1 == 11):
		return 1
	elif (total_dice1 == 2 or total_dice1 == 3 or total_dice1 == 12):
		return 0
	else:
		# point round
		dice3 = random.randint(1,6)
		dice4 = random.randint(1,6)

		while (dice3 + dice4 != 7):
			if (dice3 + dice4 == total_dice1):
				return 1
			else:
				dice3 = random.randint(1,6)
				dice4 = random.randint(1,6)
		return 0

		
def main():
	# prompt the user to enter the number of rounds
	num_rounds = int (input ("Enter number of rounds: "))

	# compute the number of times he wins
	num_wins = 0
	for n in range(num_rounds):
		num_wins += craps()

	#print the result
	print ("Player wins", num_wins, "out of", num_rounds, "rounds.")

main()


