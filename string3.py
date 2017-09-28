def countYZ(st):
	count = 0
	st = st + " "
	for i in range(len(st) - 1):
		if (st[i] == "y" or st[i] == "z") and not st[i + 1].isalpha():
			count += 1
	return count

def withoutString(s1, s2):
	s1 = s1.replace(s2, "")
	return s1

def equalIsNot(s):
	return s.count("is") == s.count("not")

def gHappy(s):
	s = " " + s + " "
	for i in range(len(s) - 1):
		if s[i] == "g" and s[i-1] != "g" and s[i+1] != "g":
			return False
	return True

def countTriple(s):
	count = 0
	for i in range(len(s) - 2):
		if s[i] == s[i + 1] == s[i + 2]:
			count += 1
	return count

def sumDigits(s):
	total = 0
	for i in s:
		if i.isdigit():
			total += int(i)
	return total

def sameEnds(s):
	count = 0
	for i in range(len(s) // 2, 0, -1):
		if s[:i] == s[-i:]:
			return s[:i]
	return ""

def mirrorEnds(s):
	s1 = ""
	for i in range(len(s)):
		if s[i] == s[-(i+1)]:
			s1 += s[i]
		else:
			break
	return s1

def maxBlock(s):
	s = s + " "
	maxblock = 0
	size = 1
	for i in range(len(s) - 1):
		if s[i] == s[i + 1]:
			size += 1
			if size > maxblock:
				maxblock = size
		else:
			size = 1
	return maxblock

def sumNumbers(s):
	a = ""
	for i in range(len(s)):
		if s[i].isdigit():
			a += s[i]
		else:
			a += " "
	a = a.split()

	total = 0
	for i in a:
		total += int(i)
	return total

def notReplace(s):
	s = " " + s + " "
	new = ""
	i = 1
	while i < len(s):
		if s[i:i+2] == "is" and not s[i-1].isalpha() and not s[i + 2].isalpha():
			new += "is not"
			i += 2
		else:
			new += s[i]
			i += 1
	return new

def main():
	#print(countYZ('day fyyyz'))
	#print(withoutString("Hello there", "e"))
	#print(equalIsNot("This is not"))
	#print(countTriple("xxxabyyyycd"))
	#print(sumDigits("aa11b33"))

	#print(sameEnds("x"))
	#print(mirrorEnds('abXYZba'))
	#print(maxBlock("abbCCCddBBBxx"))

	#print(sumNumbers("7 11"))
	print(notReplace("This is right"))
main()