''' Courtney Guthrie and Brian Richardson 
9/11/18
CSCI 203: 3 pm Tuesday  
Lab 2 - Writing Recursive Functions
'''
def mult(n,m):
    if m == 0:
        return 0
    elif m>0:
        return n+mult(n, m-1)
    elif m<0:
        return -mult(n,-m)

def dotProduct(list1,list2):
    if len(list1) != len(list2):
        return 0.0
    if len(list1)==0 and len(list2) == 0:
        return 0.0
    if len(list1) > 0:
        return (list1[0] * list2[0]) + dotProduct(list1[1:],list2[1:])

def myIndex(e, seq):
    if e == seq[0]:
        return 0
    else:
        return 1 + myIndex(e,seq[1:])

def letterScore(letter):
    letterDict = {
            'a':1,
            'b':3,
            'c':3,
            'd':2,
            'e':1,
            'f':4,
            'g':2,
            'h':4,
            'i':1,
            'j':8,
            'k':5,
            'l':1,
            'm':3,
            'n':1,
            'o':1,
            'p':3,
            'q':10,
            'r':1,
            's':1,
            't':1,
            'u':1,
            'v':4,
            'w':4,
            'x':8,
            'y':4,
            'z':10
        }
    return letterDict.get(letter)

def scrabbleScore(word):
    if len(word) == 0:
        return 0
    else:
        return letterScore(word[0]) + scrabbleScore(word[1:])
