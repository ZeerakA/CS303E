#  File: CreditCard.py

#  Description: Checks credit card to see if it's valid or not

#  Student Name: Murray Lee

#  Student UT EID: mwl647

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 04/03/2017

#  Date Last Modified: 04/06/2017

# This function checks if a credit card number is 15 or 16 digits
def check_digits(cc_num):
	if (cc_num >= 100000000000000) and (cc_num <= 9999999999999999):
		return is_valid(cc_num)
	else:
		return "Not a 15 or 16-digit number"

# This function checks if a credit card number is valid
def is_valid(cc_num):
	total_sum = is_validHelper(cc_num, 0)

	if total_sum % 10 == 0:
		return "Valid" + cc_type(cc_num) + "credit card number"
	else:
		return "Invalid credit card number"

# This helper function adds up the digits of the credit card
def is_validHelper(cc_num, index):
	if cc_num == 0:
		return 0
	else:
		index_num = cc_num % 10
		cc_num = cc_num // 10

		if index % 2 == 0:
			return index_num + is_validHelper(cc_num, index + 1)
		else:
			return sumDigits(index_num) + is_validHelper(cc_num, index + 1)

# This function sums up the digits o
def sumDigits(cc_num):
	cc_num = cc_num * 2
	if cc_num > 9:
		cc_num = cc_num % 10 + 1
	return cc_num

# This function returns the type of credit card
def cc_type(num):
	digit1 = forward_counter(num, 1)
	digit2 = forward_counter(num, 2)
	digit3 = forward_counter(num, 3)
	digit4 = forward_counter(num, 4)

	ae_option1 = digit1 == 3 and digit2 == 4
	ae_option2 = digit1 == 3 and digit2 == 7

	discover_option1 = digit1 == 6 and digit2 == 0 and digit3 == 1 and digit4 == 1
	discover_option2 = digit1 == 6 and digit2 == 4 and digit3 == 4
	discover_option3 = digit1 == 6 and digit2 == 5

	master_option1 = digit1 == 5 and digit2 >=  0 and digit2 <= 5

	visa_option1 = digit1 == 4

	if ae_option1 or ae_option2:
		return " American Express "
	elif discover_option1 or discover_option2 or discover_option3:
		return " Discover "
	elif master_option1:
		return " MasterCard "
	elif visa_option1:
		return " Visa "
	else:
		return " "


# This function returns the digit of the credit card counting from the left hand side
def forward_counter(number, index):
	digit = forward_counterHelper(number, number, index, 0)

	return digit

# This helper function does the counting
def forward_counterHelper(num, new, index, count):
	len_left = int_len_counter(num, 0) - count
	if index == len_left:
		return new % 10
	else:
		new = new // 10
		return forward_counterHelper(num, new, index, count + 1)

# This function returns the length of the credit card read as an integer
def int_len_counter(num, count):
	if num == 0:
		return count
	else:
		num = num // 10
		return int_len_counter(num, count + 1)


def main():
	entered_number = int(input("Enter 15 or 16-digit credit card number: "))

	print(check_digits(entered_number))

main()

