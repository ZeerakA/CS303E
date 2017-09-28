def main():

	word1 = input("Enter first word: ")
	word2 = input("Enter next word: ")

	isAnagram(word1, word2)

def isAnagram(s1, s2):
	list1 = list(s1)
	list2 = list(s2)

	list1.sort()
	list2.sort()

	if list1 == list2:
		print("are anagram")
	else:
		print("not anagram")

main()