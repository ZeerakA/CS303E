def forward_counter(number, index):
	digit = forward_counterHelper(number, number, index, 0)

	return digit


def forward_counterHelper(num, new, index, count):
	len_left = int_len_counter(num, 0) - count
	if index == len_left:
		return new % 10
	else:
		new = new // 10
		return forward_counterHelper(num, new, index, count + 1)


def int_len_counter(num, count):
	if num == 0:
		return count
	else:
		num = num // 10
		return int_len_counter(num, count + 1)

#backwards counter
#index from 0 at leftmost of number, 469, index 0, 1, 2
'''
def digit_value(num, backward_index, count):
	if count == backward_index:
		return num % 10
	else:
		num = num // 10
		return digit_value(num, backward_index, count + 1)
	'''

def main():
	print(forward_counter(51689, 3))
main()