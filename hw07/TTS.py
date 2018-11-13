import math
class tts():
    """TTS System"""
    
    def __init__(self):
        self.prices = []
        print("Welcome to TTS")
        self.menu()
    def menu(self):
        print()
        for key,value in self.commands.items():
            print("("+str(key)+")   "+ self.descriptions[value])
        choice = int(input("\nEnter your choice: "))
        options = [key for key in self.commands]
        if (choice not in options):
            self.other()
        else:
            command = self.commands[choice]
            command(self)
    def newList(self):
        """Input a new list"""
        try:
            self.prices = eval(input("Enter a new list of prices: "))
        except:
            print("Unable to evaluate entered list")
            self.prices = []
        self.menu()
    def printCurrent(self):
        """Print the current list"""
        print("DAY | PRICE")
        for i in range(len(self.prices)):
            day = str(i)
            price = self.prices[i]
            price = '${:,.2f}'.format(price)
            while(len(day) < 3):
                day = " " + day
            print(day + " | " + price)
        self.menu()
    def averagePrice(self):
        """Find the average price"""
        average = 0
        for p in self.prices:
            average += p
        average = average / len(self.prices)
        average = '${:,.2f}'.format(average)
        print("The average price is", average)
        self.menu()
    def standardDeviation(self):
        """Find the standard deviation"""
        average = 0
        for p in self.prices:
            average += p
        average = average / len(self.prices)
        result = 0
        for p in self.prices:
            result = result + (p - average)**2 #SIGMA
        result = result / len(self.prices) #DIVIDE BY LEN
        result = math.sqrt(result) #SQUARE ROOT
        print("The standard deviation is",result)
        self.menu()
    def minDay(self):
        """Find the min and its day"""
        result = (0,self.prices[0])
        for i in range(len(self.prices)):
            if result[1] > self.prices[i]:
                result = (i,self.prices[i])
        print("The min is on day "+ str(result[0]) + " at price " + '${:,.2f}'.format(result[1]))
        self.menu()
    def maxDay(self):
        """Find the max and its day"""
        result = (0,self.prices[0]) #(Day,Price)
        for i in range(len(self.prices)):
            if result[1] < self.prices[i]:
                result = (i,self.prices[i])
        print("The max is on day "+str(result[0]) + " at price " + '${:,.2f}'.format(result[1]))
        self.menu()
    def getPlan(self):
        """Your TTS investment plan"""
        intervals = [] #[(startDay, endDay, Profit)] <-- List of tuples
        for startDay in range(len(self.prices)-1):
            for endDay in range(1,len(self.prices)-1):
                intervals.append((startDay, endDay, self.prices[endDay] - self.prices[startDay]))
        interval = (max(intervals,key=lambda item:item[2])[0],max(intervals,key=lambda item:item[2])[1])
        priceInt = (self.prices[interval[0]],self.prices[interval[1]])
        print("Buy on day " + str(interval[0]) + " at price " + '${:,.2f}'.format(priceInt[0]))
        print("Sell on day " + str(interval[1]) + " at price " + '${:,.2f}'.format(priceInt[1]))
        self.menu()
    def quitSys(self):
        """Quit"""
        print("\nClosing TTS")
        quit()
    def other(self):
        print("Thats not an option\n")
        self.menu()
    def graph(self):
        """Graphs in the console"""
        dimensions = (len(self.prices),10)
        maxPrice = max(self.prices)
        ySkip = maxPrice // dimensions[1]
        output = [["0" for x in range(dimensions[0])] for y in range(dimensions[1])]
        for x in range(len(output)):
            out = ""
            for y in range(len(output[x])):
                out += output[x][y]
            print(out)
                    
    commands = {
        0:newList,
        1:printCurrent,
        2:averagePrice,
        3:standardDeviation,
        4:minDay,
        5:maxDay,
        6:getPlan,
        7:graph,
        9:quitSys
    }
    descriptions = {
        newList:"Input a new list",
        printCurrent:"Print the current list",
        averagePrice:"Find the average price",
        standardDeviation:"Find the stndard deviation",
        minDay:"Find the min and its day",
        maxDay:"Find the max and its day",
        getPlan:"Your TTS investment plan",
        graph:"Graph stock prices",
        quitSys:"Quit"
    }
