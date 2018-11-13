#
# hw8pr3.py
#
# Name: Brian Richardson & Courtney Gutherie
#
def isMagic(a):
	'''
	>>> a = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
	>>> isMagic(a)
	True
	>>> a = [[8,1,6],[3,5,7],[4,9,2]]
	>>> isMagic(a)
	True
	>>> a[0][0] = 0
	>>> isMagic(a)
	False
	>>> a = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
	>>> isMagic(a)
	True
	>>> a[0][0] = 17
	>>> isMagic(a)
	False
	'''
	sum = 0
	for i in range(len(a)):
		sum += a[i][i]
	return diagTest(a,sum) and vertTest(a,sum) and horizTest(a,sum)
def diagTest(a,sum):
	'''
	a)  b)
	*## ##*
	#*#	#*#
	##* *##
	'''
	diagSum = 0
	for i in range(len(a)):
		diagSum += a[i][i]
	for y in range(len(a)):
		x = abs(y-len(a)+1)
		diagSum += a[y][x]
	if diagSum != 2*sum:
		return False
	else:
		return True

def vertTest(a,sum):
	h = len(a)
	w = len(a[0])
	for x in range(w):
		vertSum = 0
		for y in range(h):
			vertSum += a[y][x]
		if vertSum != sum:
			return False
	return True

def horizTest(a,sum):
	h = len(a)
	w = len(a[0])
	for y in range(h):
		horizSum = 0
		for x in range(w):
			horizSum += a[y][x]
		if horizSum != sum:
			return False
	return True

import doctest
doctest.testmod()