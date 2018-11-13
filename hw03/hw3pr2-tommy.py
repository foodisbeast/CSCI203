''' Courtney Guthrie and Brian Richardson
hw3pr2.py- Lab Problem: "Lights On!"
Lab Instructor: Darakhshan Mir
9/18/18
CSCI 203: 3 pm Tuesday  
Lab 3 - Designing functions and working with lists
'''
from collections import Counter
def encipher(s,n):
    sNew = ""
    for char in s:
        if char >= 'a' and char <= 'z':
            #from 97-122
            if ord(char) + n > 122:
                sNew = sNew + (chr(ord(char) + n - 26))
            elif ord(char) + n < 97:
                sNew = sNew + (chr(ord(char) + n + 26))
            else:
                sNew = sNew + (chr(ord(char) + n))
        elif char >= 'A' and char <= 'Z':
            #FROM 65-90
            if ord(char) + n > 90:
                sNew = sNew + (chr(ord(char) + n - 26))
            elif ord(char) + n < 65:
                sNew = sNew + (chr(ord(char) + n + 26))
            else:
                sNew = sNew + (chr(ord(char) + n))
        else:
            sNew = sNew + char
    return sNew
def decipher(s):
    Max = 0.0
    options = {}
    for i in range(27):
        options[totalError(encipher(s,i))] = encipher(s,i)
    for x in options:
        if x > Max:
            Max = x
    return(options[Max])
        
def totalError(word):
    '''Returns total error
    '''
    letterCount = dict(Counter(word))
    Sum = 0.0
    for x in word:
        Sum = Sum + ((letterFrequency(x) - (letterCount[x]/len(word)))**2)
    return Sum

def letterFrequency(c):
    ''' Determines the frequency (percent) at which a letter occurs in English
    text.  If the letter is not alphabetic, return 0.  See Letter Frequenc
    in Wikipedia.
    '''
    if 'A' <= c <= 'Z':
        c = c.lower()
    if c < 'a' or c > 'z':
        return 0
    frequencies = {'a':8.167,
                   'b':1.492,
                   'c':2.782,
                   'd':4.253,
                   'e':12.702,
                   'f':2.228,
                   'g':2.015,
                   'h':6.094,
                   'i':6.966,
                   'j':0.153,
                   'k':0.772,
                   'l':4.025,
                   'm':2.406,
                   'n':6.749,
                   'o':7.507,
                   'p':1.929,
                   'q':0.095,
                   'r':5.987,
                   's':6.327,
                   't':9.056,
                   'u':2.758,
                   'v':0.978,
                   'w':2.36,
                   'x':0.15,
                   'y':1.974,
                   'z':0.074
                   }
    return frequencies[c]
