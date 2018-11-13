''' Courtney Guthrie and Brian Richardson 
9/27/18
CSCI 203: 3 pm Tuesday  
Lab 7 - Writing Recursive Functions
'''
NUM_ITERATIONS = 25
MAX_X = -1.0
MIN_X = -1.3
MAX_Y = 0.3
MIN_Y = 0.1
def mult(c,n):
    result = 0
    for i in range(n):
        result += c
    return result

def update(c,n):
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z

def isInMandelbrotSet(c,n=NUM_ITERATIONS):
    '''
    >>> n = 25
    >>> c = 0 + 0j
    >>> isInMandelbrotSet(c,n)
    True
    >>> c = 3 + 4j
    >>> isInMandelbrotSet(c,n)
    False
    >>> c = 0.3 + -0.5j
    >>> isInMandelbrotSet(c,n)
    True
    >>> c = -0.7 + 0.3j
    >>> isInMandelbrotSet(c,n)
    False
    >>> c = -0.9 + 0.4j
    >>> isInMandelbrotSet(c,n)
    False
    >>> c = 0.42 + 0.2j
    >>> isInMandelbrotSet(c,25)
    True
    >>> isInMandelbrotSet(c,50)
    False
    '''
    z = 0
    for i in range(n):
        z = z**2 + c
        if (abs(z)>2):
            return False
    return True

#import doctest
#doctest.testmod()

from cs5png import * # You may already have this line... 
def isPixelWanted(col, row): 
    """ Determines if we want a pixel. 
    """ 
    return col % 10 == 0 and row % 10 == 0 #Changing the 'and' to 'or' would create a grate instead of dotting
    
def testImage(): 
    """ Demonstrates how to create and save a png file. 
    """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 

    for col in range(width): 
        for row in range(height): 
            if isPixelWanted(col, row): 
                image.plotPoint(col, row) 
   
     # We looped through every image pixel; we now write the file 

    image.saveFile()

def scale(coord, coordmax, floatMin, floatMax):
    ratio = coord/coordmax
    delta = floatMax - floatMin
    movement = delta*ratio
    return floatMin + movement
    
def mandelbrotSet(width, height):
    #-2.0 <= x or real coordinate <= +1.0
    #-1.0 <= y or imaginary coordinate <= +1.0
    image = PNGImage(width,height)
    for col in range(width):
        x = scale(col, width, MIN_X, MAX_X)
        for row in range(height):
            y = scale(row,height,MIN_Y,MAX_Y)
            c = x+y*1j
            if (isInMandelbrotSet(c)):
                image.plotPoint(col,row,(0,255,0))
            else:
                image.plotPoint(col,row,(255,0,0))
    image.saveFile()
                
    

    
