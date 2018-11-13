''' Courtney Guthrie and Brian Richardson
hw3pr2.py- Lab Problem: "Lights On!"
Lab Instructor: Darakhshan Mir
9/18/18
CSCI 203: 3 pm Tuesday  
Lab 3 - Designing functions and working with lists
'''
from collections import Counter
def encipherChar(char,n):
    sNew = ''
    if char >= 'a' and char <= 'z':
        #from 97-122
        if ord(char) + n > 122:
            sNew = (chr(ord(char) + n - 26))
        elif ord(char) + n < 97:
            sNew = (chr(ord(char) + n + 26))
        else:
            sNew = (chr(ord(char) + n))
    elif char >= 'A' and char <= 'Z':
        #FROM 65-90
        if ord(char) + n > 90:
            sNew = (chr(ord(char) + n - 26))
        elif ord(char) + n < 65:
            sNew = (chr(ord(char) + n + 26))
        else:
            sNew = (chr(ord(char) + n))
    else:
        sNew = char
    return sNew
def encipher(s,n):
    if s == '':
        return ''
    else:
        return encipherChar(s[0], n) + encipher(s[1:],n)
    
def decipher(s,debug=False):
    d = {}
    for i in range(27):
        d[error(encipher(s,i))] = encipher(s,i)
    maxError = 0.0
    for curError in d:
        if debug:
            print(d[curError],curError)
        if curError > maxError:
            maxError = curError
    return(d[maxError])
        
def error(s):
    '''Returns sum of squared error
    for formula see:
    https://math.tutorvista.com/statistics/error-sum-of-squares.html
    '''
    errorSum = 0.0
    #Actual Letter count
    letterCount = dict(Counter(s))
    for char in s:
        errorSum = errorSum + ((letterFrequency(char) - (letterCount[char]/len(s)))**2)
    return errorSum

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
