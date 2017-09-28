import string

def main():
	s1 = input("Enter the first string: ")
	s2 = input("Enter the second string: ")

	count = 0

	for i in range(len(s1)):
		if s2[i] == s1[i]:
			print(s1[i], end='')
			count +=1
	if count == 0:
		print("No common prefix")
main()