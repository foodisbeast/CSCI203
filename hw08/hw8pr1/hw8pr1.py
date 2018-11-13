#
# hw8pr1.py - Game of Life lab
#
# Name: Brian Richardson & Courtney Gutherie
#

import random
from gameOfLife import *

def createOneRow(width):
    """ Returns one row of zeros of width "width"...
        You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
	'''
	>>> board = createBoard(5, 3)
	>>> board
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	'''
	board = [[0 for i in range(width)] for i in range(height)]
	return board

def printBoard(board):
	'''
	>>> board = createBoard(5,3)
	>>> printBoard(board)
	00000
	00000
	00000
	'''
	for y in range(len(board)):
		out = ''
		for x in range(len(board[y])):
			out += str(board[y][x])
		print(out)

def diagonalize(width,height):

	'''
	>>> board = diagonalize(7, 6)
	>>> board
	[[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]]

	>>> printBoard(board)
	1000000
	0100000
	0010000
	0001000
	0000100
	0000010
	'''

	board = createBoard(width, height) 
	for y in range(height): 
		for x in range(width): 
			if x == y: 
				board[y][x] = 1 
			else: 
				board[y][x] = 0 
	return board

def innerCells(width,height):
	'''
	>>> board = innerCells(5, 5)
	>>> printBoard(board)
	00000
	01110
	01110
	01110
	00000
	'''
	board = createBoard(width,height)
	for y in range(height):
		for x in range(width):
			if not(y == 0 or x == 0 or x == width-1 or y == height -1):
				board[y][x] = 1
	return board

def randomCells(width,height):
	board = createBoard(width,height)
	for y in range(height):
		for x in range(width):
			if not(y == 0 or x == 0 or x == width-1 or y == height -1):
				board[y][x] = random.randint(0,1)
	return board

def copy(board):
	'''
	>>> board = createBoard(2, 2)
	>>> board2 = board
	>>> printBoard(board2)
	00
	00
	>>> board[0][0] = 1
	>>> printBoard(board)
	10
	00
	>>> printBoard(board2)
	10
	00
	>>> board = createBoard(2,2)
	>>> board2 = copy(board)
	>>> id(board) != id(board2)
	True
	>>> board[0][0] = 1
	>>> board2
	00
	00
	>>> board[1][0] = 1
	>>> board2
	00
	00
	>>> board[0][1] = 1
	>>> board2
	00
	00
	>>> board[1][1] = 1
	>>> board2
	00
	00
	'''
	copy = createBoard(len(board[0]),len(board))
	for y in range(len(board[0])):
		for x in range(len(board)):
			copy[y][x] = board[y][x]
	return copy

def innerReverse(board):
	'''
	>>> b = innerCells(4,4)
	>>> b = innerReverse(b)
	>>> printBoard(b)
	0000
	0000
	0000
	0000
	'''
	board2 = copy(board)
	width = len(board[0])
	height = len(board)
	for y in range(height):
		for x in range(width):
			if not(y == 0 or x == 0 or x == width-1 or y == height -1):
				if board[y][x] == 1:
					board2[y][x] = 0
				else:
					board2[y][x] = 1
	return board2
def countNeighbors(board):
	'''
	>>> b = innerCells(5,5)
	>>> printBoard(b)
	00000
	01110
	01110
	01110
	00000
	>>> c = countNeighbors(b)
	>>> printBoard(c)
	00000
	03530
	05850
	03530
	00000
	'''
	width = len(board[0])
	height = len(board)
	count = createBoard(width,height)
	for by in range(height):
		for bx in range(width):
			if not(by == 0 or bx == 0 or bx == width-1 or by == height -1):
				for cy in range(by-1, by+2):
					for cx in range(bx-1,bx+2):
						if ((cy,cx) != (by,bx)):
							count[by][bx] += board[cy][cx]
				
	return count

def nextLifeGeneration(board):
	'''
	>>> board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
	>>> printBoard(board)
	00000
	00100
	00100
	00100
	00000
	>>> board2 = nextLifeGeneration(board)
	>>> printBoard(board2)
	00000
	00000
	01110
	00000
	00000

	>>> board3 = nextLifeGeneration(board2)
	>>> printBoard(board3)
	00000
	00100
	00100
	00100
	00000
	'''
	width = len(board[0])
	height = len(board)
	count = countNeighbors(board)
	newBoard = copy(board)
	for y in range(height):
		for x in range(width):
			if not(y == 0 or x == 0 or x == width-1 or y == height -1):
				if count[y][x] < 2:
					newBoard[y][x] = 0
				if count[y][x] > 3:
					newBoard[y][x] = 0
				if count[y][x] == 3:
					newBoard[y][x] = 1
	return newBoard
