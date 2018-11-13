''' Courtney Guthrie and Brian Richardson 
9/27/18
CSCI 203: 3 pm Tuesday  
Lab 4 - Writing Recursive Functions
'''
def numToBinary(a):
    add = a%2
    if a<=1:
        return str(a)
    else:
        return str(numToBinary(a//2) + str(add))
 
def binaryToNum(a):
    if len(a) <= 0:
        return 0
    else:
        return (2**(len(a)-1) * int(a[0])) + binaryToNum(a[1:])
def increment(a):
    a = binaryToNum(a)
    a = a + 1
    if a > 255:
        a = 0
    a = numToBinary(a)
    while len(a) < 8:
        a = '0' + a
    return a

def count(a,n):
    print(a)
    if n == 0:
        return
    else:
        a = increment(a)
        count(a,n-1)

def numToTernary(a):
    add = a%3
    if a<=1:
        return str(a)
    else:
        return str(numToTernary(a//3) + str(add))

def ternaryToNum(a):
    if len(a) <= 0:
        return 0
    else:
        return (3**(len(a)-1) * int(a[0])) + ternaryToNum(a[1:])
