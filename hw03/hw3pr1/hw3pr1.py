''' Courtney Guthrie and Brian Richardson
hw3pr1.py- Lab Problem: "Lights On!"
Lab Instructor: Darakhshan Mir
9/18/18
CSCI 203: 3 pm Tuesday  
Lab 3 - Designing functions and working with lists
'''

# Most of your Lab 3 code will go here:
import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(100000) # 100,000 deep - in theory

def runGenerations(aList):
    """ runGenerations keeps running the evolve function...
    """
    print(aList)            # display the list, aList
    time.sleep(0.5)         # pause a bit
    newList = evolve(aList) # evolve aList into newList
    if isAllOnes(newList) == False:
        return 1 + runGenerations(newList) # recur
    print(newList)
    return 1

def evolve(aList):
    """ evolve takes in a list of integers, aList,
          and returns a new list of integers
          considered to be the "next generation"
    """
    n = len(aList)  # n now holds the length of the list aList
    newList = [setNewElement(aList, i) for i in range(n)]
    return newList

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
         input aList: any list of integers
         input i: the index of the new element to return
         input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return aList[i] + 1

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
         input aList: any list of integers
         input i: the index of the new element to return
         input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return aList[i] *2

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
         input aList: any list of integers
         input i: the index of the new element to return
         input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return aList[i] ** 2

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
         input aList: any list of integers
         input i: the index of the new element to return
         input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return aList[i-1]

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
         input aList: any list of integers
         input i: the index of the new element to return
         input x: an extra, optional input for future use
    """
    # this returns the ith element of the new list! That is, newList[i]
    return choice([0,1])
def isAllOnes(aList):
    for x in aList:
        if x == 0:
            return False
    return True
def evolve(aList):
    """ evolve takes in a list of integers, aList,
          and returns a new list of integers
          considered to be the "next generation"
    """
    n = len(aList)  # n now holds the size of the list aList
    x = randint(0,len(aList))
    return [setNewElement(aList, i, x) for i in range(n)]

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element
          input aList: any list of integers
          input i: the index of the new element to return
          input x: the user's chosen column
    """
    if i == x or i == x-1 or i == x+1:  # if it's the user's chosen column,
        if aList[i] == 0: #Toggle between 0 and 1
            return 1
        else:
            return 0
    else:                        # otherwise,
        return aList[i]          # return the original

def randomBinaryList(n):
    return [choice([0,1]) for i in range(n)]

##### GRAPHICS ######
from turtle import *
import csgrid; from csgrid import *
from random import *

setColor(0,"gray")
setColor(1,"yellow")
def runGraphicsGen(aList, col):
    """ aList is the list last displayed
        evolve aList first
    """
    print("col is", col)
    aList = evolve(aList, col)
    show(aList)             # display
    if isAllOnes(aList):
        print("Hooray!")
        return

    # We finish here!

    # When the mouse is clicked,
    # this will be called again!

    # aList is "remembered" by show (in a "global"
    # variable) and is later passed in by the
    # graphics system. Global variables are
    # best avoided, but sometimes are required.

def evolve(aList, x):
    """ evolve takes in a list of integers, aList,
          and returns a new list of integers
          considered to be the "next generation"
    """
    N = len(aList)  # N now holds the size of the list aList
    return [setNewElement(aList, i, x) for i in range(N)]

def setNewElement(aList, i, x):
    """ setNewElement returns the NEW list's ith element
          input aList: any list of integers
          input i: the index of the new element to return
          input x: an extra, optional input for future use
    """
    if abs(i-x)<=1:  # if it's the user's chosen column,
        return 1-aList[i]            # toggle the one clicked
    else:                        # otherwise,
        return aList[i]              # return the original



# set the mouse handler...
def mouseHandler(x, y):
    """ This function is called with each mouse click.

        Its inputs are the pixel location of the
        next mouse click: (x, y)

        It computes the column (within the list)
        where the click occurred with getCol.

        The overall list is shared between turtle graphics
        and the other parts of your program as a global
        variable named currentL. In general, global variables
        make software more complex, but sometimes they are
        necessary.

        Then, this function calls the next generation via
        runGraphicsGen(aList, col) - note that the col is available!
    """
    col = getCol(x, y)
    aList = csgrid.currentL  # get from the graphics module
    runGraphicsGen(aList, col)

onscreenclick(mouseHandler)

# here is where your starting conditions go...
# when it runs, it will be ready to play
# however, you'll need to change the setNewElement function, above
# in order to play according to the "Lights out" rules...

startingList = randomBinaryList(12)
show(startingList)

done()  # your system may need this line uncommented...
