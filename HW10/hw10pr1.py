import matplotlib
def readFile(fileName):
    inFile = open(fileName,'r')
    text = inFile.read()
    inFile.close()
    return text

def readFileFor(fileName):
    inFile = open(fileName, 'r')
    total = 0

    for line in inFile:
        lineList = line.split()
        total = total + int(lineList[2])

    inFile.close()
    return total

def readFileWhile(fileName):
    inFile = open(fileName, 'r')
    total = 0

    while True:
        line = inFile.readLine()
        if not line:
            break
        lineList = line.split()
        total += int(lineList[2])

    inFile.close()
    return total


