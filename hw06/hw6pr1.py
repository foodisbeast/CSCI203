def hasUniqueElements(a):
    if len(a) == 0:
        return True
    elif a[0] in a[1:]:
        return False
    else:
        return hasUniqueElements(a[1:])

def listFromFile(fileName): 
    """ Takes a string containing a file name as input. 
    The file should contain numbers, with one number
    on each line. The output is a list of those 
    numbers. """ 
    numbersFile = open(fileName)   # open the file 
    allText = numbersFile.read()   # get all the text from the file 
    numbersFile.close()            # close the file 
    
    justNums = allText.strip()     # just the numbers, still as a string 
    listOfLines = justNums.split() # into a list of strings
    listOfInts = [int(s) for s in listOfLines] # convert each line to an int 
    return listOfInts
