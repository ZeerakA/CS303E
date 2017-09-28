def parseString(st):
	return parseStringHelper(st, "")

def parseStringHelper(st, parsed_st):
	if len(st) == 0:
		return parsed_st
	elif st[0].isalpha():
		parsed_st += st[0].lower()
	elif st[0] == "'" and len(st) > 1:
		if st[1] == "s":
			parsed_st += "  "
		else:
			parsed_st += st[:2]
		return parseStringHelper(st[2:], parsed_st)
	else:
		parsed_st += " "
	return parseStringHelper(st[1:], parsed_st)

def main():
	print(parseString("Hello's helAVl'kd-'"))
main()