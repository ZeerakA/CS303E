# knight two move capture pawn
# reverse key and value pair

import random

def d1(st):
	dict1 = {}
	for s in st:
		if s != " ":
			if s in dict1:
				dict1[s] += 1
			else:
				dict1[s] = 1
	return dict1

# coem back
def d2(dic):
	new_dict = {}
	for key in dic:
		if dic[key] in new_dict:
			new_dict[dic[key]] = [new_dict[dic[key]], key]
		else:
			new_dict[dic[key]] = key
	return new_dict

def set1(l1, l2):
	s1 = set(l1)
	s2 = set(l2)
	return s1 & s2

def list1():
	list1 = []
	for row in range(3):
		list2 = []
		for col in range(5):
			list2.append(random.randint(1,100))
		list1.append(list2)
		print(list2)

def listsCheck(list1, list2):
	if len(list1) == len(list2) and len(list1[0]) == len(list2[0]):
		for row in range(len(list1)):
			if list1[row] != list2[row]:
				return False
	return True

def listCheck1(l1, l2):
	if l1 == l2:
		return True
	return False

def sumList(l1, l2):
	list_sum = []
	for row in range(len(l1)):
		list_row = []
		for el in range(len(l1[0])):
			list_row.append(l1[row][el] + l2[row][el])
		list_sum.append(list_row)
	return list_sum

def rev_row(l1):
	for row in l1:
		row.reverse()
	return l1

def rev_col(l1):
	new_list = []
	for i in range(1, len(l1) + 1):
		new_list.append(l1[-i])
	return new_list

def add_lists(l1, l2):
	total = 0
	for i in range(len(l1)):
		total += l1[i] * l2[i]
	return total

def is_sorted(l1):
	for i in range(len(l1) - 1):
		if l1[i] > l1[i + 1]:
			return False
	return True

def twodsum(l1):
	rows = []
	for i in range(len(l1)):
		row_sum = 0
		for j in range(len(l1[0])):
			row_sum += l1[i][j]
		rows.append(row_sum)
	print(rows)

	cols = []
	for i in range(len(l1[0])):
		col_sum = 0
		for j in range(len(l1)):
			col_sum += l1[j][i]
		cols.append(col_sum)
	print(cols)

	l_diag = 0
	for i in range(len(l1)):
		l_diag += l1[i][i]
	print(l_diag)

	r_diag = 0
	for i in range(len(l1)):
		r_diag += l1[i][len(l1) - i - 1]
	print(r_diag)

def sort_fnc(l1):
	for i in range(len(l1)):
		for j in range(i + 1, len(l1)):
			if l1[j] < l1[i]:
				l1[i], l1[j] = l1[j], l1[i]
	return l1

def shuffle(l1):
	random.shuffle(l1)
	return l1

def anagrams(s1, s2):
	list1 = []
	list2 = []
	for i in range(len(s1)):
		if s1[i].isalpha():
			list1.append(str.lower(s1[i]))
	for i in range(len(s2)):
		if s2[i].isalpha():
			list2.append(str.lower(s2[i]))

	list1.sort()
	list2.sort()

	if list1 == list2:
		return True
	return False

def password(user, pw):
	in_file = open("passwd.txt", "r")

	for line in in_file:
		line = line.strip()
		if user + ":" + pw == line:
			return True
	return False
	in_file.close()
	

def main():
	#print(d1("helloooox..d adf"))

	phone_book = {'Texas':'Austin', 'New York':'NYC', 'California':'Sacramento', 'New Mexico':'Sacramento', 'Texas':'Dallas', 'Texas':'Houston', 'Texas':'Sacramento'}
	users = {'user1':'pass1', 'user2':'pass2', 'user3':'pass1'}
	#print(d2(phone_book))

	#print(set1(['a', 'b','c'], ['c', 'd', 'e']))

	#list1()

	l1 = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]
	l2 = [[3,2,1], [4,5,6],[7,8,10]]
	l2 = [[1,2,3], [4,5,6],[7,8,9],[10,11,12]]
	#print(listsCheck(l1, l2))
	#print(rev_row(l1))
	#print(sumList(l1, l2))
	#print(rev_col(l1))
	l3 = [3, 2, 1, 5, 1, -3, 2, 3]
	l4 = [4, 5, 6]
	#print(add_lists(l3, l4))
	#print(is_sorted(l3))

	#twodsum(l2)

	#print(sort_fnc(l3))

	#print(password("murray", "leee"))
	#print(shuffle(l3))

	#print(anagrams("ccA.-Bc", "abC0cc"))
	#print(users.keys())

	print(listCheck1(l1, l2))

main()