from turtle import *

#TheScreen = Screen()
#TheScreen.onclick(mouseHandler)

currentL = None

COL = -1
ROW = -1

currentXs = []
currentYs = []

def getCol(mouse_x, mouse_y):
    global currentXs;
    global currentYs;
    global COL
    global ROW

    COL = 0
    ROW = 0
    
    for i in range(len(currentXs)-1):
        if currentXs[i] <= mouse_x < currentXs[i+1]:
            COL = i

    for i in range(len(currentYs)-1):
        if currentYs[i] <= mouse_y < currentYs[i+1]:
            ROW = i

    return COL

            
# start-up turtle stuff
reset()
tracer(False)
delay(0)
clrD = { 0:"white", 1:"red", 2:"blue", 3:"green", 4:"gold" }

def setColor(key, color):
    global clrD
    clrD[key] = color
    return

def colorLookup(clr):
    global clrD
    if clr in clrD:
        return clrD[clr]
    else:
        return clr

def drawsq(ulx, uly, side, clr):
    delay(0)
    tracer(False)
    up()
    # try setting the color
    pencolor("black")
    # look up the color
    clr = colorLookup(clr)
    # go!
    try:
        fillcolor(clr)
    except:
        print("Color", clr, "was not recognized.")
        print("Using blue instead.")
        fillcolor("blue")

    goto(ulx, uly)
    down()
    seth(0) # east in normal mode
    
    begin_fill()
    for s in range(4):
        forward(side)
        right(90)
    end_fill()

    up()

    
def show1d(aList):
    """ new - with turtle!! """
    # remember this!
    global currentL
    currentL = aList
    
    W = window_width()
    H = window_height()
    if len(aList) == 0:
        print("You can't show(aList) when aList is empty.")
        return

    n = len(aList) + 2 # 2 more for a margin on each side

    sq_side = min(W/float(n), H/float(3), 100.0)
    
    uly = 0 + sq_side/2.0
    ulx = -sq_side*len(aList)/2.0

    global currentYs
    currentYs = [-uly, uly]
    global currentXs
    currentXs = [ulx]


    clear()
    for clr in aList:
        #print("clr is", clr)
        drawsq(ulx, uly, sq_side, clr)
        ulx += sq_side
        currentXs.append(ulx)

    return

def show(aList):
    show1d(aList)
    return


# start with something
show1d([1, 1, 0, 1])


    
