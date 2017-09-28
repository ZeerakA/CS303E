def main():
	loan_amount = eval(input("Enter loan amount: "))
	loan_period = eval(input("Enter loan period: "))

	print(format("Interest Rate", "20s"), end="")
	print(format("Monthly Payment", "20s"), end="")
	print(format("Total Payment", "20s"))
	print()

	x = 0
	n = 5.000
	while (x <= 24):
		n_string = str(n) + "%"
		print(format(n_string, "20s"), end="")
		month = ((loan_amount * (n/100) / 12 / (1-((n/1200)+1)**(12*loan_period*-1))))
		print(format(format(month, "0.2f"), "20s"), end="")
		print(format(loan_period*12*month, "0.2f"))
		x += 1
		n += 0.125

main()