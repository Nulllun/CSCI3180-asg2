# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : ***
# Student ID : **
# Email Addr : ***

class GameBoard:
    def __init__(self):
        self.board = None

    def init_gameBoard(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'
        self.board[3][3] = 'X'
        self.board[4][4] = 'X'
        return

    def check_ending(self):
        #check whether the game is over or not
        #return True or False
        checkO = self.check_legal_move('O')
        checkX = self.check_legal_move('X')
        if checkO or checkX:
            return False
        return True
        
    def check_legal_move(self,symbol):
	#check if their is a legal move given symbol
        #return True or False
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == ' ':
                    # Start checking iff the pos don't has a disc
                    # then check the 8 direction
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if self.checkDirection([i,j], symbol, [x,y], False):
                                return True
        return False
                                
    def check_winner(self):
        #return a list[s1,s2], represent the total number for O and X
        numOfO = 0
        numofX = 0
        for i in range(8):
            for j in range(8):
                if(self.board[i][j] == 'O'):
                    numOfO += 1
                if(self.board[i][j] == 'X'):
                    numofX += 1      
        return numOfO, numofX

    def execute_flip(self, pos, symbol):
        for x in range(-1,2):
            for y in range(-1,2):
                self.checkDirection(pos, symbol, [x,y], True)
        return

    def printGameBoard(self):
        print('   ', end='|')
        for i in range(1,9):
            print(' %d ' % i, end='|')
        print('')
        print('-' * 36)
        for i in range(8):
            print(' %d ' % (i+1), end='|')
            for j in range(8):
                print(" %s " % self.board[i][j], end='|')
            print('')
            print('-' * 36)
        return

    def checkDirection(self, pos, symbol, direction, flip):
        # check the given direction
        # return True if the disc can be flipped
        # flip the disc also if flip is TRUE
        # Set value for opposite symbol first
        if symbol == 'O':
            oppSymbol = 'X'
        if symbol == 'X':
            oppSymbol = 'O'
        # Check the direction
        xIncre = direction[0]
        yIncre = direction[1]
        xPos = pos[0]
        yPos = pos[1]
        xPos += xIncre
        yPos += yIncre
        meetOpp = False
        meetSpace = False
        meetSelf = False
        finishPos = []
        while xPos <= 7 and xPos >=0 and yPos <=7 and yPos >=0:
            if self.board[xPos][yPos] == ' ':
                # The 'road' between the same symbol should not contain SPACE
                meetSpace = True
                break
            elif self.board[xPos][yPos] == oppSymbol:
                meetOpp = True
            elif self.board[xPos][yPos] == symbol:
                meetSelf = True
                finishPos.append(xPos)
                finishPos.append(yPos)
                break
            else:
                break
            xPos += xIncre
            yPos += yIncre
        if meetSpace == True or meetOpp == False or meetSelf == False:
            return False
        if flip == False:
            return True
        # The following is flip statement, flip == True
        xPos = pos[0]
        yPos = pos[1]
        while [xPos,yPos] != finishPos:
            self.board[xPos][yPos] = symbol
            xPos += xIncre
            yPos += yIncre