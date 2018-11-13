'''Brian Richardson
Lab 7
'''
class graph():
    '''
    Extension for tts()
    Graphs in the console with inputted data list, *point, and **height
    Height defaults to 10
    Point defaults to '*'
     90|
     80|
     70|
     60|
     50|
     40|            *
     30|         *
     20|*      *
     10|   *
    ---|0--1--2--3--4--
    '''
    def __init__(self, data, height, point):
        self.point = point
        self.width = len(data) #graphed width
        self.height = height
        self.ySkip = max(data) // self.height #y Skip
        self.xSkip = len(str(max(data))) #x Skip
        self.width += len(str(len(data)))
        self.createGraph(data)

    def createGraph(self, data):
        #Graph ininitialization
        self.output = [[" " for i in range(self.height + 1)] for i in range(self.width * self.xSkip + 1)]
        #Draw axes
        for x in range(len(self.output)):
            self.output[x][self.height] = '-'
        for y in range(len(self.output[0])):
            self.output[self.xSkip][y] = '|'

        #Create axis Labels
        yLabels = []
        for i in reversed(range(self.height+1)):
            label = self.ySkip * i
            label = str(label)
            while (len(label) < self.xSkip):
                label = " " + label
            yLabels.append(label)
        xLabels = [str(x) for x in range(len(data))]

        #Add axis labels
            #y axis
        for y,label in enumerate(yLabels):
            for x in range(self.xSkip):
                self.output[x][y] = label[x]
            #x axis
        for x,label in enumerate(xLabels):
            for pos in range(len(label)):
                self.output[x*self.xSkip + self.xSkip + pos + 1][self.height] = label[pos]
        self.addData(data)

    def addData(self, data):
        #Adds the data to the graph in the closest position possible given the yAxis
        for x,target in enumerate(data):
            x = x*self.xSkip + self.xSkip + 1#x including offset
            possY = [y*self.ySkip for y in reversed(range(self.height + 1))] #listed in descending order
            absY = [abs(target - y) for y in possY]
            y = absY.index(min(absY))
            self.output[x][y] = '#'

    def print(self):
        print(self)

    def __str__(self):
        output = ''
        for y in range(len(self.output[0])):
            for x in range(len(self.output)):
                output = output + self.output[x][y]
            output = output + "\n"
        return output
