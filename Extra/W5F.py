l = 'puapaynfrmvemnireazr'
s = -13
def shift(num):
    #Range: 97('a') to 123(' ')
    if num + s < 97:
        return num + s + 27
    elif num + s > 123:
        return num + s - 27
    else:
        return num + s

def translate(x):
    if type(x) == type(1):
        #type int
        if x == 123:
            return ' '
        else:
            return chr(x)
    else:
        if x == ' ':
            return 123
        else:
            return ord(x)

newList = list(l)
print(newList)
newList = list(map(translate,l))
print(newList)
newList = list(map(shift,newList))
print(newList)
newList = list(map(translate,newList))
print(newList)
