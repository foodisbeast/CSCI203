''' Courtney Guthrie and Brian Richardson 
9/27/18
CSCI 203: 3 pm Tuesday  
Lab 4
'''
def numToBase(num,b):
    add = num%2
    if num<=1:
        return str(num)
    else:
        return str(numToBase(num//b,b)) + str(add)
 
def baseBToNum(s,b):
    if len(s) <= 0:
        return 0
    else:
        return (b**(len(s)-1) * int(s[0])) + baseBToNum(s[1:],b)

def add(s,t):
    #adds two binary nums and returns a base 10 number
    return numToBase(baseBToNum(s,2) + baseBToNum(t,2),2)

#notes_______
#   lengths of the strings
#   characters
#   4 combinations
#     - 3 of those return 1
#   Add '1' to the end(/[front] '10101[1]') of the index
# -   add to only one index 

#return string with sum of s1 + s2

#   01  -1  -1
#  +11  -1  -1
#->111  =1

def addBase(s1,s2,b=2):
    base = b
    n1, n2 = 0, 0
    #exit/base condition
    if len(s1) == 0 and len(s2) == 0:
        return ''

    #recursive condition
    if len(s1) == 0:
        s1 = '0'
    if len(s2) == 0:
        s2 = '0'
    n1, n2 = int(s1[-1]), int(s2[-1])
    nSum = n1 + n2
    #print('n1:', n1,"n2:",n2)
    if nSum < base:
        return addBase(s1[:-1],s2[:-1]) + str(nSum)
    else:
        s1 = s1[:-1]
        if len(s1) == 0:
            s1 = '0'
        s1 = s1[:-1] + addBase(s1[-1],'1') # 1 and 1
        return addBase(s1,s2[:-1])  + str(nSum-base)
    
def addBinary(s1,s2):
    print(addBase(s1,s2,2))
 

