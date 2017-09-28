'''
def main():
	n = eval(input("Enter an integer from 1 to 15: "))

	for i in range (1, n+1):
		for l in range (n-i, 0, -1):
			print(" ", end=" ")
		for k in range (i, 1, -1):
			print(k, end=" ")
		for j in range (1, i+1):
			print (j, end=" ")
		print()

main()
'''

import math
import random

def main():
	x = True
	y = True
	return (x or y)
	print ()
main()

