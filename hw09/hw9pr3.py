#
# hw9pr3.py
# Name: Brian Richardson & Courtney Gutherie
#
import random
def createDictionary(fileName):
    '''
    >>> wordDict = createDictionary('t.txt')
    >>> wordDict
    {'$': ['A', 'A', 'B', 'C'], 'A': ['B', 'B', 'C.'], 'B': ['A.', 'C.', 'A'], 'C': ['C', 'C.']}
    '''
    f =  open(fileName,'r')
    data = f.read()
    data = data.replace('\n', '')
    words = data.split(' ')
    word_dict = {}
    prev_word = '$'
    for word in words:
        if prev_word in word_dict:
            word_dict[prev_word].append(word)
        else:
            word_dict[prev_word] = [word]
        if endSentence(word):
            prev_word = '$'
        else:
            prev_word = word
    return word_dict
def generateText(word_dict,num_words):
    sentence_endings = ['.','?','!']
    prev_word = '$'
    out = ''
    for i in range(num_words):
        word = random.choice(word_dict[prev_word])
        out += word + ' '
        if endSentence(word):
            prev_word = '$'
        else:
            prev_word = word
    return out
def endSentence(word):
    endings = ['.','?','!']
    hasEnding = [end in word for end in endings]
    return True in hasEnding
import doctest
doctest.testmod()
