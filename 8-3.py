import string

def main():
	password = input("Enter a password: ")

	num_count = 0
	alpha_count = 0

	for i in range(len(password)):
		if "0" <= password[i] <= "9":
			num_count +=1
		elif "a" <= password[i] <= "z" or "A" <= password[i] <= "Z":
			alpha_count +=1

	if password.isalnum() and alpha_count >= 8 and num_count >=2:
		print("Valid Password")
	else:
		print("Invalid Password")

main()
