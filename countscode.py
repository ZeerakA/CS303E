import random

def main():
	nums = []
	for i in range(10):
		nums.append(random.randint(0,9))

	nums.sort()
	print(nums)
	
	for j in range(0, 10):
		print("The number", j, "has a count of", nums.count(j))


main()