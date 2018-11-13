'''Brian Richardson & Courtney Gutherie
Lab 7
'''
class TTS():
    """TTS System"""
    print("Welcome to TTS")
    def __init__(self):
        self.menu()
    def menu(self):
        for key,value in self.commands.items():
            print("("+str(key)+")   "+ self.descriptions[value])
        choice = int(input("\nEnter your choice: "))
        options = [key for key in self.commands]
        if (choice not in options):
            self.other()
        else:
            command = self.commands[choice]
            command()
    def newList(self):
        """Input a new list"""
        print()
        self.menu()
    def printCurrent(self):
        """Print the current list"""
        print()
        self.menu()
    def averagePrice(self):
        """Find the average price"""
        print()
        self.menu()
    def standardDeviation(self):
        """Find the standard deviation"""
        print()
        self.menu()
    def minDay(self):
        """Find the min and its day"""
        print()
        self.menu()
    def maxDay(self):
        """Find the max and its day"""
        print()
        self.menu()
    def getPlan(self):
        """Your TTS investment plan"""
        print()
        self.menu()
    def quitSys(self):
        """Quit"""
        quit()
    def other(self):
        print("Thats not an option\n")
        self.menu()
    commands = {
        0:newList,
        1:printCurrent,
        2:averagePrice,
        3:standardDeviation,
        4:minDay,
        5:maxDay,
        6:getPlan,
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
        quitSys:"Quit"
    }
