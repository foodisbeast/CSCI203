''' Courtney Guthrie and Brian Richardson 
9/11/18
CSCI 203: 3 pm Tuesday  
Lab 2 - Writing Recursive Functions
'''
from turtle import *
def main():
    home()
    clear()
    penup()
    goto(-250,250)
    pendown()
    spiral(500,90,0.9)
    done()
    

def spiral(leng,angle,mult):
    if leng < 2:
        return
    else:
        forward(leng)
        right(angle)
        spiral(leng*mult,angle,mult)

def svTree(trunkLength,levels):
    if levels < 0:
        return
    else:
        forward(trunkLength)
        right(30)
        svTree(trunkLength*0.5,levels-1)
        left(60)
        svTree(trunkLength*0.5,levels-1)
        right(30)
        backward(trunkLength)
            

        
    
