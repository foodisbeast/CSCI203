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
    table = [[] for _ in range(len(lines))] #table[col][row]
    print(table)
    for line in lines:
        line = line.split(',') #Line is array of values
        for col, val in enumerate(line):
            table[col].append(val)

    #Process into numpy
    x_labels = table[0][1:]
    x = range(x_labels)
    ganja_use = [e for e in table[4][1:]]
    drank_use = [e for e in table[2][1:]]

    plt.xticks(x,x_labels,rotation='horizontal')
    plt.xlim([0,len(x_labels)-1])
    plt.ylim([0,100])

    plt.title("Comparitive usages of Marijuana and Alcohol in age-bracket")
    plt.xlabel("Age-bracket")
    plt.ylabel("Percent use")

    plt.legend(loc = 'upper right', shadow = True)

    plt.plot(x,ganja_use,'--',label=("Marijuana Usage"))
    plt.plot(x,drank_use,'--',label=("Alcohol Usage"))

    plt.show()

import doctest
doctest.testmod()
