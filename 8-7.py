import string

def main():
	n = input("Enter a string: ")

	for i in range(len(n)):
		if n[i] == "-":
			print("-", end='')
		elif "0" <= n[i] <= "9":
			print(n[i], end='')
		elif "a" <= n[i] <= "c" or "A" <= n[i] <= "C":
			print("2", end='')
		elif "d" <= n[i] <= "f" or "D" <= n[i] <= "F":
			print("3", end='')
		elif "g" <= n[i] <= "i" or "G" <= n[i] <= "I":
			print("4", end='')
		elif "j" <= n[i] <= "l" or "J" <= n[i] <= "L":
			print("5", end='')
		elif "m" <= n[i] <= "o" or "M" <= n[i] <= "O":
			print("6", end='')
		elif "p" <= n[i] <= "s" or "P" <= n[i] <= "S":
			print("7", end='')
		elif "t" <= n[i] <= "v" or "T" <= n[i] <= "V":
			print("8", end='')
		elif "w" <= n[i] <= "z" or "W" <= n[i] <= "Z":
			print("9", end='')

main()