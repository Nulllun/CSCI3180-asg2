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
        pass

    def check_ending(self):
        #check whether the game is over or not
        #return True or False
        pass
	
	def check_legal_move(self,symbol):
	    #check if their is a legal move given symbol
        #return True or False
        pass


    def check_winner(self):
        #return a list[s1,s2], represent the total number for O and X
        pass

    def execute_flip(self, pos, symbol):
        pass

    def printGameBoard(self):
        pass