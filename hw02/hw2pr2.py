''' Courtney Guthrie and Brian Richardson 
9/11/18
CSCI 203: 3 pm Tuesday  
Lab 2 - Writing Recursive Functions
'''
import random   # this can go anywhere at the top of 
                     # the file
def randomStep(): 
    """ 
    randomStep chooses a random step to make and returns it. 
    Notice that randomStep() requires parentheses, but takes 
    no inputs at all! 

    """ 
    return random.choice([-1, 1])

def walkerPositionPlain(start,numberSteps):
    if numberSteps == 0:
        return start
    else:
        start = start + randomStep()
        #print("start is " + str(start))
        return walkerPositionPlain(start, numberSteps-1)

def randomWalkSteps(start,low,high):
    if start == low or start == high:
        return 0
    else:
        print (" "*(start-1) + "X")
        newStart = walkerPositionPlain(start,1)
        return 1 + randomWalkSteps(newStart,low,high)

def displacementTest():
"""At all averages the number should be close to 0
Of course we cannot expect it to completely be 0, but over longer ranges
we could expect this number to approximate 0, due to the law of big numbers
"""
    #5 Steps
    sumSteps = 0
    for x in range(1000):
        sumSteps = sumSteps + walkerPositionPlain(0,5)
    print("Average at 5 steps:"+ str(sumSteps/1000))
    #10 Steps
    sumSteps = 0
    for x in range(1000):
        sumSteps = sumSteps + walkerPositionPlain(0,10)
    print("Average at 10 steps:" + str(sumSteps/1000))
    #20 Steps
    sumSteps = 0
    for x in range(1000):
        sumSteps = sumSteps + walkerPositionPlain(0,20)
    print("Average at 20 steps:"+str(sumSteps/1000))
