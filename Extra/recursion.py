def Factorial(n):
	"""Returns factorial of number n
	ex. Factorial(4) = 4*3*2*1 = 24"""
	if (n<2):
		return 1
	else:
		return n * Factorial(n-1)
		
def NtoPower(n,power):
	"""Returns n^power
	ex. NtoPower(2,3) = 2^3 = 8"""
	if (power<1):
		return 1
	else:
		return n * NtoPower(n, power-1)

def test(x,y):
	return 2*(x+y)

