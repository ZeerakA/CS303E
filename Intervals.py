#  File: Intervals.py

#  Description: Read file and find non-intersecting intervals

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/17/2017

#  Date Last Modified: 04/17/2017

# Collapses intervals in list1 into non-intersecting intervals outputted to list2
def collapse_rec(list1, list2):
	# If we have reached the end of the sorted list
	if len(list1) == 1:
		list2.append(list1[0])
		return list2
	else:
		if list1[1][0] <= list1[0][1]:
			# |-----|
			#    |-----| 2nd interval ends past first
			if list1[1][1] > list1[0][1]:
				list1[0] = (list1[0][0], list1[1][1])
			# |-----|
			#   |--| 2nd interval ends inside first
			list1.remove(list1[1])
			return collapse_rec(list1, list2)

		# |-----|
		#         |-----| 2nd interval starts outside of first
		else:
			list2.append(list1[0])
			return collapse_rec(list1[1:], list2)
'''
# Use sorted list, and idx = 0
def length_sort(list1, idx):
	if idx == len(list1) - 1:
		return list1
	else:
		for i in range(1, len(list1[idx:])):
			distance = list1[idx + i][1] - list1[idx + i][0]
			if (list1[idx][1] - list1[idx][0]) < distance:
				list1[idx], list1[i + idx] = list1[i + idx], list1[idx]
		return length_sort(list1, idx + 1)
'''

# Sorts intervals in order of size
# list1 = sorted list, idx = 0, idx2 = 1
def length_sort(list1, idx, idx2):
	if idx == len(list1) - 1:
		return list1
	else:
		if idx2 < (len(list1) - idx):
			if (list1[idx][1] - list1[idx][0]) > (list1[idx + idx2][1] - list1[idx + idx2][0]):
				list1[idx], list1[idx + idx2] = list1[idx + idx2], list1[idx]
			return length_sort(list1, idx, idx2 + 1)
		return length_sort(list1, idx + 1, 1)

# Could have better way to strip brackets [] from interval
def lazy_print(a):
	for i in range(len(a)):
		print(a[i])

def main():
	in_file = open("./intervals.txt", "r")

	total = []

	for line in in_file:
		line = line.strip()
		line = line.split()
		for x in line:
			interval_tuple = (int(line[0]), int(line[1]))
		total.append(interval_tuple)
	in_file.close()

	total.sort()
	
	# Solution for non-intersecting intervals
	non_intersecting_intervals = collapse_rec(total, [])

	# Solution for extra credit (intervals ordered by size)
	intervals_by_size = length_sort(collapse_rec(total, []), 0, 1)

	print()
	print("Non-intersecting Intervals:")
	lazy_print(non_intersecting_intervals)
	print()
	print("Non-intersecting Intervals in order of size:")
	lazy_print(intervals_by_size)

main()

