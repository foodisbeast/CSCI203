from functools import *
nums = [0,1,2,3,4,5]
def greater(num1,num2):
    if num1 > num2:
        return num1
    return num2

reduce(greater,nums)
