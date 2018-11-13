import matplotlib
def readFile(fileName):
    inFile = open(fileName,'r')
    text = inFile.read()
    inFile.close()
    return text
