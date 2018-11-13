"""
Brian Richardson
hw2pr5 extra credit
9/11/18
This is my personal work, nobody elses
"""
import math
from functools import *

#Going natural (+4 points)
def inverse(n):
    if n != 0:
        return 1/n
    else:
        return 'Cannot divide by 0'
def e(n):
    if n == 0:
        return 1
    else:
        return inverse(math.factorial(n)) + e(n-1)
def error(n):
    return math.fabs(math.e-e(n))

#Re-writing factorial (+3 points)
def add(num1,num2):
    return num1+num2
def factorial(n):
    return reduce(add,range(n+1))

#This is “mean”… (+3 points)
def mean(numList):
    return reduce(add,numList)/len(numList)

#A Primal Problem (+5 points)
def divides(n): 
    def isDivisor(k): 
        return n % k == 0 
    return isDivisor
def isPrime(n):
    result = map(divides(n),range(2,n))
    return True not in result
    
