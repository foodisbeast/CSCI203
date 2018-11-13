#
# hw9pr2.py
# Name: Brian Richardson & Courtney Gutherie
#
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

def connect4():
    b = Board(7,6)
    b.hostGame()
import doctest
doctest.testmod()
