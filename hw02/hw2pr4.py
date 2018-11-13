"""
Brian Richardson
hw2pr4 extra credit
9/11/18
This is my personal work, nobody elses
"""
from turtle import *
speed(0)
pencolor('black')
fillcolor('blue')
penup()
def snowflake(sidelength, levels):
    '''Draws the snowflake and fills with the color blue'''
    goto(sidelength/-2,sidelength/2) #moves the turtle to a spot where the whole snowflake can be seen
    pendown()
    begin_fill()
    snowflakeSide(sidelength,levels)
    right(120)
    snowflakeSide(sidelength,levels)
    right(120)
    snowflakeSide(sidelength,levels)
    end_fill()
def snowflakeSide(sidelength,levels):
    '''Recursively draws one side of the snowflake with specified sidelength, and levels'''
    if levels < 0:
        return
    if levels == 0:
        forward(sidelength)
    else:
        snowflakeSide(sidelength/3,levels-1)
        left(60)
        snowflakeSide(sidelength/3,levels-1)
        right(120)
        snowflakeSide(sidelength/3,levels-1)
        left(60)
        snowflakeSide(sidelength/3,levels-1)
    
        
