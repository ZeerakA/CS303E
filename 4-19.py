def main():
	a, b, c = eval(input("Enter three edges: "))

	if (abs(a-b) > c or abs(a-c) > b or abs(b-c) > a):
		print ("The input is invalid")

	else:
		print ("The perimeter is", a + b + c)
main()