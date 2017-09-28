def maxSpan(nums):
	for i in range(len(nums), 0, -1):
		for j in range(0, len(nums) - i + 1):
			if nums[j] == nums[j + i - 1]:
				return i
	return 0

def fix34(nums):
	for i in range(len(nums)):
		if nums[i] == 3:
			temp = nums[i + 1]
			nums[i + 1] = 4
			for j in range(i + 2, len(nums)):
				if nums[j] == 4:
					nums[j] = temp
	return nums

def linearIn(outer, inner):
	for i in inner:
		if i not in outer:
			return False
	return True

def squareUp(n):
	s = ""
	for i in range(1, n + 1):
		for k in range(i, n):
			s += "0"
		for j in range(i, 0, -1):
			s += str(j)
	a = list(s)
	for i in range(len(a)):
		a[i] = int(a[i])
	return a

def seriesUp(n):
	a = []
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			a.append(j)
	return a

def maxMirror(nums):
	size = len(nums) // 2 + 1
	for i in range(size, 0 , -1):
		for j in range(size):
			if nums[j: j + i] == nums[j + i:]:
				return (j + i)
				#fix
def countClumps(nums):
	clumpmax = 0
	for i in range(len(nums)):
		clumpsize = 0
		for j in range(i, len(nums)):
			if nums[j] == nums[i]:
				clumpsize += 1
			else:
				break
		if clumpsize > clumpmax:
			clumpmax = clumpsize
	return clumpmax

def main():
	print(countClumps([1, 1, 2, 1, 1]))

main()