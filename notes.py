'''
list a = [1, 2, 3] only store one type of variable
call list by using index, starts at 0, a[0] = 1, a[-1] = 3
len(a) = 5
a[1:2] = [2]
a[3:5] = []
a.remove(2) 
a = [1, 3]

def main():
	a = [1, 2, 3, 4, 5, 6, 7]
	b = [2,3,4,4,7,4,7]
	ans = []
	for i in range(len(a)):
		if (a[i] == b[i]):
			ans.append(i)
		print(i, a[i])

	return (ans)

	for j in a:
		print(j)
main()
'''
'''
def main():
	idx1 = 0
	idx2 = 0

	for i in range(len(a)):
		for j in range(i+1, len(a)):
			if (a[i]*a[j] > maxprod):
				maxprod = a[i] * a[j]
				idx1 = i
				idx2 = j
main()

def main():
	s = 'aabcddeeeaa'
	st = ''

	for i in range(len(s)-1):
		if (s[i] != s[i+1]):
			st += s[i]
	print(st+s[-1])
main()

asks to return - return, print - print
no system.input
takes an input to list - don't ask input - do def func(a, b):
can return inside loop, false outside the loop (make sure you return something outside loop)
check all possible scenarios
'''

def main():
	ifile = open('input.txt', 'r')
	st = ifile.read()
	while(ifile):
		st = ifile.readline()
		st-st.strip()

	l = []

	for st in ifile:
		st = st.strip()
		if st not in l:
			l.append(st)

	ofile = open('out.txt', 'w')
	for a in l:
		ofile.write(a+'\n')
		#write is same as print but doesn't have \n at end of each line

	ifile.close()
	ofile.close()
main()

def main():
	ifile = open('input.txt', 'r')
	st  = ifile.read()

	while(ifile):
		st1 = ifile.readline()
		st2 = ifile.readline()
		if (st1 == st2):
			ofile.write(st1)
		else:
			ofile.write(st1)
			ofile.write(st1)
