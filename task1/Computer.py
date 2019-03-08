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
import random
from Player import Player
from GameBoard import GameBoard

class Computer(Player):

    def nextMove(self,board):
        pos = []
        gameboard = GameBoard()
        gameboard.board = board
        for i in range(8):
            for j in range(8):
                if board[i][j] == ' ':
                    # Start checking iff the pos don't has a disc
                    # then check the 8 direction
                    for x in range(-1,2):
                        for y in range(-1,2):
                            if gameboard.checkDirection([i,j], self.playerSymbol, [x,y], False):
                                pos.append([i,j])
        randomIndex = random.randint(0,(len(pos)-1))
        pos = pos[randomIndex]
        del gameboard
        print('Player '+self.playerSymbol+'\'s turn.')
        print('Computer Player choose to place the disc on: %d %d' % (pos[0]+1,pos[1]+1))
        return pos