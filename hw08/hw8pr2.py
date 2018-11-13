#
# hw8pr2.py
#
# Name: Brian Richardson & Courtney Gutherie
#
class matrix():
	def __init__(self):
		self.a = [[2.0, 4.0, 5.0, 34.0], [2.0, 7.0, 4.0, 36.0], [3.0, 5.0, 4.0, 35.0]]
		while(True):
			self.menu()
	def menu(self):
		options = {
		1:self.enterA,
		2:self.printA,
		3:self.multiplyRow,
		4:self.addSourceRowToDestinationRow,
		5:self.addMultipleOfSourceRowToDestRow,
		6:self.transpose,
		9:quit
		}
		out = '''
	(1) Enter a 2D array as list of lists
	(2) Print the array in rectangular form
	(3) Multiply an array row by a constant
	(4) Add one row into another
	(5) Add a multiple of one row to another
	(6) Transpose the 2D array
	(9) Quit
'''
		print(out)
		choice = options[int(input("Enter a number: "))]
		choice()
	def enterA(self):
		try:
			inp = eval(input("Enter 2D: "))
			self.a = inp
		except:
			print("Not valid List format...")

	def printA(self):
		for row in self.a:
			out = ''
			for e in row:
				out += "{:8.3f}".format(e)
			print(out)
	def multiplyRow(self):
		row = int(input("Enter row: "))
		m = float(input("Enter multiplier: "))
		for i,e in enumerate(self.a[row]):
			self.a[row][i] = e * m
	def addSourceRowToDestinationRow(self):
		src = int(input("Ente source row: "))
		dest = int(input("Enter destination Row: "))
		for i,e in enumerate(self.a[src]):
			self.a[dest][i] += e

	def addMultipleOfSourceRowToDestRow(self):
		src = int(input("Ente source row: "))
		dest = int(input("Enter destination Row: "))
		m = float(input("Enter multiplier: "))
		for i,e in enumerate(self.a[src]):
			self.a[dest][i] += e * m
	def transpose(self):
		h = len(self.a) #height of self.a
		w = len(self.a[0]) #width of self.a
		b = [[0 for _ in range(h)] for _ in range(w)] #b = transpose(a)
		for y,row in enumerate(self.a):
			for x,e in enumerate(row):
				b[x][y] = self.a[y][x]
		self.a = b
matrix()