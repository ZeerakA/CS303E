def knight(k, p, count):
	if count == 2:
		return k == p
	k_pos = list(k)
	x = k_pos[0]
	y = k_pos[1]
	
	cond1 = (x + 1, y + 2)
	cond2 = (x - 1, y + 2)
	cond3 = (x + 1, y - 2)
	cond4 = (x - 1, y - 2)

	cond5 = (x + 2, y + 1)
	cond6 = (x - 2, y + 1)
	cond7 = (x + 2, y - 1)
	cond8 = (x - 2, y - 2)

	return knight(cond1, p, count + 1) or knight(cond2, p, count + 1) or knight(cond3, p, count + 1) or knight(cond4, p, count + 1) or knight(cond5, p, count + 1) or knight(cond6, p, count + 1) or knight(cond7, p, count + 1) or knight(cond8, p, count + 1)

def main():
	print(knight((0,0), (3, 2), 0))
main()