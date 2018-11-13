''' Courtney Guthrie and Brian Richardson 
9/27/18
CSCI 203: 3 pm Tuesday  
Lab 4
'''
def numToBase(num,b):
    '''FROM PREVIOUS HW ASSIGNMENT'''
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

def compress(s):
    '''If the input bits(string/image) are in the alternating form '010101'
    the compression will be larger than the original
        - Ex. compressing '01' returns '0000000110000001'
    Therefore, for 64 alternating input bits(string/image), 64 * 8,
    the maximum numbers of bits to represent a 64bit input would be 512 bits
    '''
    if len(s) == 0:
        return ''
    else:
        val = s[0]
        count = 1
        i = 1
        while i < len(s):
            if s[i] == val:
                count += 1
                i += 1
            else:
                break
        bCount = numToBase(count,2)
        while len(bCount) < 7:
            bCount = '0' + bCount
        return (val + bCount) + compress(s[count:])
    
def uncompress(c):
    if len(c) <= 0:
        return ''
    else:
        return (c[0] * baseBToNum(c[1:8],2)) + uncompress(c[8:])
    
