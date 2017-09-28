#  File: Books.py

#  Description: Compare word frequencies of two authors

#  Student Name: Murray Lee and Zakariya Kuzbari

#  Student UT EID: mwl647 and mzk97

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/28/2017

#  Date Last Modified: 05/01/2017

# Create a word dictionary from the comprehensive word list
scrabble_dict = {}
def create_scrabble_dict():
	scrabble = open ("./words.txt", "r")

	for line in scrabble:
		line = line.strip()
		scrabble_dict[line] = 1
	scrabble.close()

# Removes punctuation marks from a string
def parseString(st):
	return parseStringHelper(st, "")

def parseStringHelper(st, parsed_st):
	if len(st) == 0:
		return parsed_st
	elif st[0].isalpha():
		parsed_st += st[0]
	elif st[0] == "'" and len(st) > 1:
		if st[1] == "s":
			parsed_st += "  "
		elif st[1].isalpha():
			parsed_st += st[:2]
		else:
			parsed_st += "  "
		return parseStringHelper(st[2:], parsed_st)
	else:
		parsed_st += " "
	return parseStringHelper(st[1:], parsed_st)

# Creates a dictionary for a book
def create_book_dict(file_name):
	dict_name = {}
	book = open (file_name, "r")
	for line in book:
		line = line.strip()
		line = parseString(line)

		# split the line into words
		word_list = line.split()

		# add each word to the set and to the dictionary
		for word in word_list:
				if word in dict_name:
					dict_name[word] = dict_name[word] + 1
				else:
					dict_name[word] = 1
	book.close()
	return dict_name

# Returns number of distinct words, total words, and ratio between them
def getWordFreq(dict_n):
	# Checks uppercase words
	list1 = []
	for word in dict_n:
		if word[0].isupper():
			list1.append(word)

	for word in list1:
		lowercase_word = str.lower(word)
		# Word begins at sentence and already has key
		if lowercase_word in dict_n:
			dict_n[lowercase_word] += dict_n[word]
		# Word begins at sentence and doesn't have key
		elif lowercase_word in scrabble_dict:
			dict_n[lowercase_word] = dict_n[word]
		# Delete uppercase word
		del dict_n[word]

	# Sorts words from a to z
	sorted_words = list(dict_n.keys())
	sorted_words.sort()

	# Finds number distinct words
	distinct = (len(sorted_words))
	print("Total distinct words =", distinct)

	# Finds total number of words
	total = 0
	for word in dict_n:
		total += dict_n[word]
	print("Total words (including duplicates) =", total)

	# Finds ratio of distinct total words
	ratio = distinct / total * 100
	print("Ratio (% of total distinct words to total words) =", ratio)

def wordComparison(author1, dict1, author2, dict2):
	set1 = set(dict1)
	set2 = set(dict2)

	author1_unique = set1 - set2
	author2_unique = set2 - set1

	freq1 = 0
	for word in author1_unique:
		freq1 += dict1[word]

	freq2 = 0
	for word in author2_unique:
		freq2 += dict2[word]

	author1_total = 0
	for word in dict1:
		author1_total += dict1[word]

	author2_total = 0
	for word in dict2:
		author2_total += dict2[word]

	print(author1, "used", len(author1_unique), "words that", author2, "did not use.")
	print("Relative frequency of words used by", author1, "not in common with", author2, "=", freq1 / author1_total * 100)
	print()
	print(author2, "used", len(author2_unique), "words that", author1, "did not use.")
	print("Relative frequency of words used by", author2, "not in common with", author1, "=", freq2 / author2_total * 100)

def main():
	# Scrabble dictionary
	create_scrabble_dict()

	# Enter names of the two books in electronic form
	book1 = input ("Enter name of the first book: ")
	book2 = input ("Enter name of the second book: ")
	print()

	author1 = input ("Enter name of the first author: ")
	author2 = input ("Enter name of the second author: ")
	print()

	dict1 = create_book_dict(book1)
	dict2 = create_book_dict(book2)
	
	'''
	a = []
	for key in dict2:
		a.append(key)
	a.sort()

	infile = open("sample.txt", "r")

	count = 0
	for i in a:
		line = infile.readline()
		line = line.strip()
		line = line.split()

		if [str(dict2[i]), i] != line:
			print([str(dict2[i]), i])'''
			

	
	print(author1)
	getWordFreq(dict1)
	print()
	print(author2)
	getWordFreq(dict2)

	print()

	wordComparison(author1, dict1, author2, dict2)
	

main()