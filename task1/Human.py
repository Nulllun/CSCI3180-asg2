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
from Player import Player
from GameBoard import GameBoard

class Human(Player):
        
    def nextMove(self,board):
        pos = []
        gameboard = GameBoard()
        gameboard.board = board
        while True:
            print('Player '+self.playerSymbol+'\'s turn.')
            try:
                row, col = input("Type the row and col to put the disc: ").split(' ')
                row = int(row) - 1
                col = int(col) - 1
            except ValueError:
                print('Invalid Input.')
                continue
            validCo = False
            for x in range(-1,2):
                for y in range(-1,2):
                    if gameboard.checkDirection([row,col], self.playerSymbol, [x,y], False) == True:
                        validCo = True
            if validCo == True:
                pos.append(row)
                pos.append(col)
                break
            else:
                print('Invalid Input.')
        del gameboard
        return pos