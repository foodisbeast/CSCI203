#
# hw9pr2E.py EXTRA CREDIT
# Name: Brian Richardson
#
import turtle
import math
class Board:
    def __init__(self, width, height):
        self.data = [[' ' for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.winScore = 4
    def __repr__(self):
        out = ''
        for y,row in enumerate(self.data):
            for x,e in enumerate(self.data[y]):
                out += ('|%s' % e)
            out+='|\n'
        for _ in range(len(out.split('\n')[0])):
            out+='-'
        out += '\n'
        for i in range(self.width):
            out += (" %s" % (i % 10))
        return out

    def addMove(self,col,player):
        '''
        >>> board = Board(7, 6)
        >>> board.addMove(0, 'X')
        >>> board.addMove(0, 'O')
        >>> board.addMove(0, 'X')
        >>> board.addMove(3, 'O')
        >>> board.addMove(4, 'O') # Cheat and let O go again!
        >>> board.addMove(5, 'O')
        >>> board.addMove(6, 'O')
        >>> board
        | | | | | | | |
        | | | | | | | |
        | | | | | | | |
        |X| | | | | | |
        |O| | | | | | |
        |X| | |O|O|O|O|
        ---------------
         0 1 2 3 4 5 6
         '''
        assert(player == 'X' or player == 'O')
        for y in reversed(range(self.height)):
            if (self.data[y][col] == ' '):
                self.data[y][col] = player
                break

    def clear(self):
        self.data = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def setBoard(self,moveString):
        nextChar = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col < self.width:
                self.addMove(col,nextChar)
            if nextChar == 'X':
                nextChar = 'O'
            else:
                nextChar = 'X'

    def isMoveLegal(self,col):
        '''
        >>> board = Board(2, 2)
        >>> print(board)
        | | |
        | | |
        -----
         0 1
        >>> board.addMove(0, 'X')
        >>> board.addMove(0, 'O')
        >>> print(board)
        |O| |
        |X| |
        -----
         0 1
        >>> board.isMoveLegal(-1)
        False
        >>> board.isMoveLegal(0)
        False
        >>> board.isMoveLegal(1)
        True
        >>> board.isMoveLegal(2)
        False
        '''
        if col >= self.width or col < 0:
            return False
        if (self.data[0][col] == ' '):
            return True
        else:
            return False

    def isFull(self):
        '''
        >>> board = Board(2, 2)
        >>> board.isFull()
        False
        >>> board.setBoard('0011')
        >>> print(board)
        |O|O|
        |X|X|
        -----
         0 1
        >>> board.isFull()
        True
        '''
        for y,row in enumerate(self.data):
            for x,e in enumerate(row):
                if e == ' ':
                    return False
        return True
    def deleteMove(self,col):
        '''
        >>> board = Board(2, 2)
        >>> board.setBoard('0011')
        >>> board.deleteMove(1)
        >>> board.deleteMove(1)
        >>> board.deleteMove(1)
        >>> board.deleteMove(0)
        >>> print(board)
        | | |
        |X| |
        -----
         0 1
        '''
        for y in range(self.height):
            if (self.data[y][col] != ' '):
                self.data[y][col] = ' '
                break
    def isWinFor(self,player):
        '''
        >>> board = Board(7, 6)
        >>> board.setBoard('00102030')
        >>> print(board)
        | | | | | | | |
        |O| | | | | | |
        |O| | | | | | |
        |O| | | | | | |
        |O| | | | | | |
        |X|X|X|X| | | |
        ---------------
         0 1 2 3 4 5 6
        >>> board.isWinFor('X')
        True
        >>> board.isWinFor('O')
        True
        >>> board.clear()
        >>> board.setBoard('23344545515')
        >>> board
        | | | | | | | |
        | | | | | | | |
        | | | | | |X| |
        | | | | |X|X| |
        | | | |X|X|O| |
        | |O|X|O|O|O| |
        ---------------
         0 1 2 3 4 5 6
        >>> board.isWinFor('X') # diagonal
        True
        >>> board.isWinFor('O')
        False
        '''
        for y,row in enumerate(self.data):
            for x,e in enumerate(row):
                score = 0
                #Horizontal Check
                if x <= self.width - self.winScore:
                    for i in range(self.winScore):
                        if (self.data[y][x + i] == player):
                            score += 1
                    if score >= 4:
                        return True
                    score = 0
                #Vertial check
                if y <= self.height - self.winScore:
                    for i in range(self.winScore):
                        if self.data[y + i][x] == player:
                            score += 1
                    if score >= 4:
                        return True
                    score = 0
                #Diag (up to down)
                if y <= self.height - self.winScore and x <= self.width - self.winScore:
                    for i in range(self.winScore):
                        if self.data[y+i][x+i] == player:
                            score += 1
                    if score >= 4:
                        return True
                    score = 0
                #Diag (down to up)
                if y >= self.winScore - 1 and x <= self.width - self.winScore:
                    for i in range(self.winScore):
                        if self.data[y-i][x+i] == player:
                            score += 1
                    if score >= 4:
                        return True
                    score = 0
        return False

    def hostGame(self):
        winner = 'Tie'
        turn = 'X'
        print("Welcome to Connect Four\n")
        while (self.isFull() == False):
            print(self)
            col = int(input("%s's choice: " % turn))
            if (self.isMoveLegal(col)):
                self.addMove(col,turn)
                if self.isWinFor(turn):
                    winner = turn
                    break
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            else:
                print("Not valid move")
        print(self)
        if winner == 'Tie':
            print("Tie Game")
        else:
            print("%s Won!" % winner)

    def createGUI(self):
        gui = GUI(self)

class GUI:
    def __init__(self,board):
        self.board = board
        self.window_size=(1000,1000)
        self.canvas_size=(800,800)
        self.offset=(self.window_size[0]//10,self.window_size[1]//10)
        self.box_size = self.canvas_size[0]//max(self.board.width,self.board.height)
        screen = turtle.Screen()
        screen.setup(self.window_size[0],self.window_size[1],0,0)
        screen.setworldcoordinates(0,self.window_size[1],self.window_size[1],0)
        screen.onscreenclick(self.screenClick)
        self.board.turn = 'X'
        self.clearGUI()
        turtle.ht()

    def clearGUI(self):
        turtle.clear()
        for y in range(self.board.height):
            pos_y = y * self.box_size + self.offset[1]
            for x in range(self.board.width):
                pos_x = x * self.box_size + self.offset[0]
                self.drawsq(pos_x,pos_y,self.box_size)
        turtle.setposition(self.window_size[0]//2, self.offset[1]//2)
        turtle.write("Player %s's Turn" % self.board.turn, True, align="center",font=("Arial",24,"normal"))

    def drawsq(self,x,y,size):
        turtle.speed(0)
        turtle.delay(0)
        turtle.tracer(0)
        turtle.seth(0)
        turtle.penup()
        turtle.setposition(x,y)
        turtle.pendown()
        for s in range(4):
            turtle.fd(size)
            turtle.right(-90)
        turtle.penup()

    def drawO(self,size):
        pos = turtle.position()
        turtle.pencolor("blue")
        turtle.setposition(pos[0], pos[1] - size)
        turtle.pendown()
        turtle.circle(size)
        turtle.penup()
        turtle.pencolor("black")

    def drawX(self,size):
        turtle.pencolor("red")
        current_pos = turtle.position()
        turtle.setposition(current_pos[0] - size//2, current_pos[1] + size//2)
        turtle.seth(-45)
        turtle.pendown()
        turtle.fd(size*1.41)
        turtle.penup()
        turtle.setposition(current_pos[0] + size//2, current_pos[1] + size//2)
        turtle.seth(180+45)
        turtle.pendown()
        turtle.fd(size*1.41)
        turtle.penup()
        turtle.setposition(current_pos[0],current_pos[1])
        turtle.pencolor("black")
        turtle.seth(0)

    def drawMoves(self):
        turtle.penup()
        for y,row in enumerate(self.board.data):
            for x,e in enumerate(row):
                pos = self.getBoxPos(x,y)
                turtle.setposition(pos[0],pos[1])
                if e == 'O':
                    self.drawO((self.box_size//2)*.85)
                if e == 'X':
                    self.drawX(self.box_size * .85)

    def getBoxPos(self,x,y):
        pos = (self.offset[0] + self.box_size//2 + x*self.box_size,self.offset[0] + self.box_size//2 + y*self.box_size)
        return pos
    def getPosCol(self,x,y):
        for box_col in range(self.board.width):
            box_pos = self.getBoxPos(0,box_col)[1]
            boundaries = (box_pos - self.box_size//2,box_pos + self.box_size//2)
            if x >= boundaries[0] and x <= boundaries[1]:
                return box_col
        return self.board.width
    def drawWin(self):
        winner = "Tie"
        if self.board.isWinFor('O'):
            winner = "O"
        elif self.board.isWinFor('X'):
            winner = "X"
        turtle.setposition(self.window_size[0]//2, self.offset[0]//4 * 3)
        turtle.write("Winner: %s" % winner, True, align="center",font=("Arial",24,"normal"))

    def screenClick(self,mouse_x,mouse_y):
        if self.board.isFull() == False and self.board.isWinFor('O') == False and self.board.isWinFor('X') == False:
            choice_col = self.getPosCol(mouse_x,mouse_y)
            if self.board.isMoveLegal(choice_col):
                self.board.addMove(choice_col,self.board.turn)
                if self.board.turn == 'X':
                    self.board.turn = 'O'
                else:
                    self.board.turn = 'X'
                self.clearGUI()
                self.drawMoves()
                if self.board.isWinFor('O') or self.board.isWinFor('X'):
                    self.drawWin()
        else:
            self.drawWin()
def connect4():
    b = Board(7,6)
    yn = input("*EXTRA CREDIT* Graphical Connect Four? (y/n): ")
    if yn == 'y':
        g = GUI(b)
    else:
        b.hostGame()
import doctest
doctest.testmod()
