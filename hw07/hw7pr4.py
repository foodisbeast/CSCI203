'''hw7pr4 EXTRA CREDIT
Brian Richardson
'''
def printRect(width,height,symbol):
    output = ''
    for y in range(height):
        for x in range(width):
            output += symbol
        output += "\n"
    print(output)
#printRect(4, 6, '%')

def printTriangle(width,symbol,rightUp):
    rng = range(width)
    if rightUp:
        rng = reversed(rng)
    output = ''
    for y in rng:
        for x in range(width-y):
            output += symbol
        print(output)
        output = ''
#printTriangle(3, '@', True)
#printTriangle(3, '@', False)
        
def printBumps(num,symbol1,symbol2):
    output = ''
    for height in range(1,num+1):
        printTriangle(height,symbol1,True)
        printTriangle(height,symbol2,False)
    print(output)
#printBumps(4, '%', '#')

def print2D(output):
	#Prints square 2d arrays
	sideLength = len(output)
	for y in range(sideLength):
		out = ''
		for x in range(sideLength):
			out += str(output[x][y])
		print(out)
def printDiamond(width, symbol):
	sideLength = width * 2 - 1
	output = [[0 for i in range(sideLength)] for i in range(sideLength)]
	edgeSpace = (sideLength-1)/2
	for y in range(sideLength):
		edge = ' ' * abs(edgeSpace)
		writeLength = sideLength - (abs(edgeSpace) * 2)
		out = edge
		for i in range(writeLength):
			if i % 2 == 0:
				out += symbol
			else:
				out += ' '
		out += edge
		for x in range(sideLength):
			output[x][y] = out[x]
		edgeSpace -= 1

	#Print out
	print2D(output)
#printDiamond(3, '+') 

def printStripedDiamond(width, symbol1, symbol2):
	sideLength = width * 2 - 1
	output = [[' ' for i in range(sideLength)] for i in range(sideLength)]
	edgeSpace = (sideLength-1)/2
	symbols = [symbol1,symbol2]
	symbolIndex = 0
	for stripe in range(width):
		y = width -1 + stripe
		for x in range(width):
			x += stripe
			output[x][y] = symbols[symbolIndex]
			y += -1
		symbolIndex += 1
		if symbolIndex >= len(symbols):
			symbolIndex = symbolIndex % len(symbols)

	#Print output
	print2D(output)
#printStripedDiamond(7,'.','%')

def printCrazyStripedDiamond(width, symbol1, symbol2, numSym1, numSym2):
	sideLength = width * 2 - 1
	output = [[' ' for i in range(sideLength)] for i in range(sideLength)]
	edgeSpace = (sideLength-1)/2
	symbols = []
	for i in range(numSym1):
		symbols.append(symbol1)
	for i in range(numSym2):
		symbols.append(symbol2)

	symbolIndex = 0
	for stripe in range(width):
		y = width -1 + stripe
		for x in range(width):
			x += stripe
			output[x][y] = symbols[symbolIndex]
			y += -1
		symbolIndex += 1
		if symbolIndex >= len(symbols):
			symbolIndex = symbolIndex % len(symbols)

	#Print output
	print2D(output)
#printCrazyStripedDiamond(7,'.','%',2,1)