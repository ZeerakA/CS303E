import string

def main():
	s = input("Enter a string for SSN: ")
	s1 = s[:3]
	s2 = s[3]
	s3 = s[4:6]
	s4 = s[6]
	s5 = s[7:]

	if s1.isdigit() and s3.isdigit() and s5.isdigit() and s2 == '-' and s4 == '-':
		print("Valid")
	else:
		print("Invalid")
main()