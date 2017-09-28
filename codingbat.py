import string

def notReplace(s):
	s_copy = ' ' + s + ' '
	result = ''
	for i in range(1, len(s_copy)-1):
		if s_copy[i:i+2] == 'is':
			if s_copy[i-1].isalpha() or s_copy[i+2].isalpha():
				result += 1
			else:
				result += 'is not'
		result += s_copy[i]
	return result

def countYZ(s):
	s_space = s + " "
	count = 0
	for i in range(len(s)):
		if s_space[i:i+2] == "y " or s_space[i:i+2] == "z ":
			count +=1
	return count

def withoutString(s1, s2):
	s1 = s1.replace(s2, "")
	return s1

def equalIsNot(s):
	return s.count("is") == s.count("not")

def countClumps(a):
	clumpsize = 1
	clumpcount = 0
	for i in range(len(a) - 1):
		if a[i] == a[i+1]:
			clumpsize += 1
		if a[i] != a[i+1] and clumpsize > 1:
			clumpcount += 1
			clumpsize = 1
	if clumpsize > 1:
		clumpcount +=1
	return clumpcount

def gHappy(s):
	happy = False
	for i in range(len(s)-1):
		if s[i:i+2] == 'gg':
			happy = True
	return happy

def countTriple(s):
	count = 0
	for i in range(len(s)-2):
		if s[i] == s[i+1] and s[i+1] == s[i+2]:
			count +=1
	return count

def sumDigits(s):
	sum1 = 0
	for i in s:
		if i.isdigit():
			sum1 += int(i)
	return sum1

def sameEnds(s):
	a = ''
	for i in range(len(s)//2, 0, -1):




		if s[:i] == s[-i:]:
			a = s[:i]
			return a

def mirrorEnds(a):
	s = ''
	for i in range(len(a)//2):
		if a[i] == a[-(i+1)]:
			s += a[i]
		else:
			continue
	return s

def maxBlock(a):
	count = 1
	newstr = ''
	maxcount = 0
	add = ''

	for i in range(len(a) - 1):
		if a[i] == a[i+1]:
			count +=1
			newstr += a[i]
			if count > maxcount:
				maxcount = count
				longeststr = newstr
		else:
			if a[i] == a[i-1] and count == maxcount:
				longeststr += a[i-1]
			count = 1
			newstr = ''
	return maxcount, longeststr
	#fuck this

def sumNumbers(a):
	b = ''
	sum1 = 0
	for i in range(len(a) -1):
		if a[i].isdigit():
			b += a[i]
			if a[i+1].isdigit == False:
				sum1 += int(b)
				b = ''
	return sum1
	#fuck

def seq_search(a, x):
	for i in range(len(a)):
		if (x == a[i]):
			return i
	return -1

def binary_search(a,x):
	lo = 0
	hi = len(a) - 1
	while (lo <= hi):
		mid = (lo + hi) // 2
		if (x < a[mid]):
			hi = mid -1
		elif (x > a[mid]):
			lo = mid + 1
		else:
			return mid
	return -1

def selection_sort(a):
	for i in range(len(a) - 1):
		min = a[i]
		min_idx = i

		for j in range(i+1, len(a)):
			if (a[j] < min):
				min = a[j]
				min_idx = j
		a[i], a[min_idx] = a[min_idx], a[i]
	return a

def max_span(nums):
	for i in range(len(nums), 0, -1):
		for j in range(0, i-len(nums)+1):
			if nums[j] == nums[j+i]:
				return i

def alpha(s):
	new = ''
	for i in range(len(s)):
		if s[i].isalpha():
			new += s[i]
	return new

def main():
	x = 'This is-is cool'
	#print(notReplace(x))
	#print(countYZ('fez day fyyyza yellowy'))
	#print(withoutString("heeello there", "ee"))
	#print(equalIsNot("This is not"))
	#print(gHappy("xxgxxgxg"))
	#print(countTriple("xxxabyyyycd"))
	#print(sumDigits("aaa1bc2d4"))
	#print(sameEnds("xxx"))
	#print(countClumps([1,2,2,3,4,4,1,3,3,4,4]))
	#print(mirrorEnds('aba'))
	#print(maxBlock("abbcccddbbbxx"))
	#print(sumNumbers("7 11"))
	print(alpha("a12xjlkaBkljdaf 20"))
	

main()