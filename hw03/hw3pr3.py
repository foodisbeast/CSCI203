''' Courtney Guthrie and Brian Richardson
hw3pr3.py- Lab Problem: "Lights On!"
Lab Instructor: Darakhshan Mir
9/18/18
CSCI 203: 3 pm Tuesday  
Lab 3 - Designing functions and working with lists
'''
def swapElem(aList, i0, i1):
    '''Swaps the elements at given indexes i0 and i1
    then returns the new list with the swapped elements
    '''
    newList = aList
    newList[i0] = aList[i1]
    newList[i1] = aList[i0]
    print(newList)
    return newList

def binaryListSort(aList):
    if len(aList) <= 0:
        return []
    if aList[0] == 0:
        return [aList[0]] + binaryListSort(aList[1:])
    else:
        return binaryListSort(aList[1:]) + [aList[0]]
    
def insertOne(element, aList):
    ''' Inserts element into its proper place in a sorted list aList.
    input: element is an item to be inserted.  aList is a sorted list.
    output: A sorted list.
    '''
    if len(aList) == 0:
        return [element]
    elif element < aList[0]:
        return [element] + aList
    else:
        return aList[0:1] + insertOne(element, aList[1:])

def sort(aList):
    if len(aList) == 0:
        return []
    else:
        return insertOne(aList[0],sort(aList[1:]))
                
def jottoScore(s1,s2):
    if len(s1) == 0:
        return 0
    else:
        shared = 0
        for char in s2:
            if s1[0] == char:
                shared = 1
                s2 = list(s2)
                s2.remove(char)
                break
        return shared + jottoScore(s1[1:], ''.join(s2))
