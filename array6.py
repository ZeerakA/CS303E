def array6(nums, index):
	if len(nums) == 0:
		return False
	elif nums[index] == 6:
		return True
	elif nums[index] == nums[-1]:
		return False
	else:
		return array6(nums, index + 1)

def main():
	print(array6([1,1,6,1], 0))
main()