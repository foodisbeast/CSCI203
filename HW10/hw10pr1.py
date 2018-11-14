import numpy as np
import matplotlib.pyplot as plt

def readFile(fileName):
    inFile = open(fileName,'r')
    text = inFile.read()
    inFile.close()
    return text

def readFileFor(fileName):
    inFile = open(fileName, 'r')
    total = 0

    for line in inFile:
        lineList = line.split()
        total = total + int(lineList[2])

    inFile.close()
    return total

def readFileWhile(fileName):
    '''
    >>> readFileFor('numbers.txt')
    20
    >>> readFileWhile('numbers.txt')
    20
    '''
    inFile = open(fileName, 'r')
    total = 0

    while True:
        line = inFile.readline()
        if not line:
            break
        lineList = line.split()
        total += int(lineList[2])

    inFile.close()
    return total

def plotDrugUse():
    #Load csv
    f = open('drug_use_age.csv','r')
    lines = f.read().split('\n')
    lines = lines[:-1] #Removes blank line at end
    #table = [[] for _ in range(len(lines))] #table[col][row]
    table = [[header] for header in lines[0].split(',')]
    print(table,'\n',len(table))
    for line in lines[1:]:
        values = line.split(',')
        print('len of values: ', len(values))
        for col,e in enumerate(values):
            print(col,e)
            if e == '-':
                e = 0
            if col >= 1:
                table[col].append(float(e))
            else:
                table[col].append(e)
    #Process into numpy
    x_labels = table[0][1:]
    print('x_labels\n',x_labels)
    x = range(len(x_labels))
    ganja_use = [e for e in table[4][1:]]
    drank_use = [e for e in table[2][1:]]

    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.plot(x,drank_use,'r-',label='Alcohol Usage')
    plt.plot(x,ganja_use,'--',label='Marijuana Usage')
    plt.xticks(x,x_labels,rotation='vertical')
    plt.xlim([0,len(x_labels)-1])
    plt.ylim(0,100)
    plt.xlabel("Age Groups")
    plt.ylabel("Percentage of age group who used drug in past 12 months")

    plt.title("From national survey on drug use 2015")
    plt.legend(loc = 'upper right', shadow = True)

    plt.show()

import doctest
doctest.testmod()
