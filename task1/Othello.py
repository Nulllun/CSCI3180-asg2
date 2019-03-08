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
# Name : Lun Yin Fung
# Student ID : 1155092566
# Email Addr : 1155092566@link.cuhk.edu.hk

import sys
import random


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
                            if self.check_direction([i,j], symbol, [x,y], False):
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
                self.check_direction(pos, symbol, [x,y], True)
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

    def check_direction(self, pos, symbol, direction, flip):
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
        if xIncre == 0 and yIncre == 0:
            return False
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
        # print([finishPos[0]+1,finishPos[1]+1])
        while [xPos,yPos] != finishPos:
            self.board[xPos][yPos] = symbol
            xPos += xIncre
            yPos += yIncre
        return True


class Player:

    def __init__(self, symbol):
        self.playerSymbol = symbol

    def nextMove(self, board):
        pass


class Human(Player):

    def check_direction(self, pos, symbol, direction, board):
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
        if xIncre == 0 and yIncre == 0:
            return False
        xPos = pos[0]
        yPos = pos[1]
        xPos += xIncre
        yPos += yIncre
        meetOpp = False
        meetSpace = False
        meetSelf = False
        finishPos = []
        while xPos <= 7 and xPos >=0 and yPos <=7 and yPos >=0:
            if board[xPos][yPos] == ' ':
                # The 'road' between the same symbol should not contain SPACE
                meetSpace = True
                break
            elif board[xPos][yPos] == oppSymbol:
                meetOpp = True
            elif board[xPos][yPos] == symbol:
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
        return True

    def nextMove(self,board):
        pos = []
        while True:
            print('Player '+self.playerSymbol+'\'s turn.')
            try:
                row, col = input("Type the row and col to put the disc: ").split(' ')
                # the gameboard 2D list is different from user view
                row = int(row) - 1
                col = int(col) - 1
                if row > 7 or row < 0 or col > 7 or col < 0 or board[row][col] != ' ':
                    print('Invalid Input.')
                    continue
            except ValueError:
                # make sure the input is integer
                print('Invalid Input.')
                continue
            validCo = False
            for x in range(-1,2):
                for y in range(-1,2):
                    if self.check_direction([row,col], self.playerSymbol, [x,y], board) == True:
                        validCo = True
            if validCo == True:
                pos.append(row)
                pos.append(col)
                break
            else:
                print('Invalid Input.')
        return pos


class Computer(Player):

    def check_direction(self, pos, symbol, direction, board):
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
        if xIncre == 0 and yIncre == 0:
            return False
        xPos = pos[0]
        yPos = pos[1]
        xPos += xIncre
        yPos += yIncre
        meetOpp = False
        meetSpace = False
        meetSelf = False
        finishPos = []
        while xPos <= 7 and xPos >=0 and yPos <=7 and yPos >=0:
            if board[xPos][yPos] == ' ':
                # The 'road' between the same symbol should not contain SPACE
                meetSpace = True
                break
            elif board[xPos][yPos] == oppSymbol:
                meetOpp = True
            elif board[xPos][yPos] == symbol:
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
        return True
        
    def nextMove(self,board):
        pos = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == ' ':
                    # Start checking iff the pos don't has a disc
                    # then check the 8 direction
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if self.check_direction([i,j], self.playerSymbol, [x,y], board):
                                # save the possible position to the list
                                pos.append([i,j])
        randomIndex = random.randint(0,(len(pos)-1))
        # generate a random integer index of the list
        pos = pos[randomIndex]
        print('Player '+self.playerSymbol+'\'s turn.')
        print('Computer Player choose to place the disc on: %d %d' % (pos[0]+1,pos[1]+1))
        return pos


class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        if playerNum == 1:
            # The 'O' player
            print('Please choose player 1 (O):')
        if playerNum == 2:
            # The 'X' player
            print('Please choose player 2 (X):')
        print('1. Human')
        print('2. Computer Player')
        while True:
            playerType = input('Your choice is: ')
            if playerType == '1':
                # Human player
                newPlayer = Human(symbol)
                break
            if playerType == '2':
                newPlayer = Computer(symbol)
                break
            print('Invalid input! Input must be integer "1" or "2" ')
        return newPlayer


    def startGame(self):
	#basic logic
        self.player1 = self.createPlayer('O', 1)
        self.player2 = self.createPlayer('X', 2)
        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

        while not self.gameBoard.check_ending():
            current_player = [self.player1,self.player2][self.turn]
			 
            if self.gameBoard.check_legal_move(current_player.playerSymbol):
                pos = current_player.nextMove(self.gameBoard.board)
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            self.turn = 1 - self.turn

            self.gameBoard.printGameBoard()

        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')


if __name__ == "__main__":
    othello = Othello()
    othello.startGame()
