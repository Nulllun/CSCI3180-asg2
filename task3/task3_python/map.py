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
from land import Land
from pos import Pos
# from npc import NPC
from elf import Elf
from monster import Monster
from warrior import Warrior

class Map:

    _DIMENSION = 10

    def __init__(self):
        self._lands = [[Land]*self._DIMENSION for i in range(self._DIMENSION)]
        self._teleportable_obj = []
        self._e = random.randint(0,1) + 2
        self._m = random.randint(0,1) + 2
        self._w = 1
        self._total_num = self._m + self._e + self._w
        self._num_of_alive_monsters = self._m
        self._num_of_alive_warriors = self._w

    @property
    def num_of_alive_monsters(self):
        return self._num_of_alive_monsters

    @num_of_alive_monsters.setter
    def num_of_alive_monsters(self, value):
        self._num_of_alive_monsters = value

    def decrease_num_of_alive_monsters(self):
        self.num_of_alive_monsters -= 1

    @property
    def num_of_alive_warriors(self):
        return self._num_of_alive_warriors

    @num_of_alive_warriors.setter
    def num_of_alive_warriors(self, value):
        self._num_of_alive_warriors = value

    def decrease_num_of_alive_warriors(self):
        self.num_of_alive_warriors -= 1

    @property
    def lands(self):
        return self._lands

    @lands.setter
    def lands(self, param):
        pos, obj = param
        self._lands[pos.x][pos.y].occupied_obj = obj

    def initialize_all(self):
        print("Welcome to Kafustrok. Light blesses you. ")
        for i in range(self._DIMENSION):
            for j in range(self._DIMENSION):
                self._lands[i][j] = Land()
        for i in range(self._total_num):
            pos = self.get_un_occupied_position()
            if i < self._m:
                self.lands[pos.x][pos.y].occupied_obj = Monster(pos.x, pos.y, i, self)
            elif i < self._m + self._e:
                self.lands[pos.x][pos.y].occupied_obj = Elf(pos.x,pos.y, i - self._m, self)
            else:
                self.lands[pos.x][pos.y].occupied_obj = Warrior(pos.x, pos.y, i - self._m - self._e, self)
                self._teleportable_obj.append(self.lands[pos.x][pos.y].occupied_obj)

    def teleport_all(self):
        for obj in self._teleportable_obj:
            if isinstance(obj, Warrior):
                    obj.teleport()

    def coming(self, posx, posy, warrior):
        return self.lands[int(posx)][int(posy)].coming(warrior)

    def delete_teleportable_obj(self, obj):
        index = self._teleportable_obj.index(obj)
        self._teleportable_obj[index] = None

    def get_un_occupied_position(self):
        randx = random.randint(0,self._DIMENSION-1)
        randy = random.randint(0,self._DIMENSION-1)
        while(self.lands[randx][randy].occupied_obj != None):
            randx = random.randint(0,self._DIMENSION-1)
            randy = random.randint(0,self._DIMENSION-1)
        return Pos(randx,randy)

    def print_board(self):
        print_object = [['']*self._DIMENSION for i in range(self._DIMENSION)]

        for i in range(self._DIMENSION):
            for j in range(self._DIMENSION):
                occupant_name = self.lands[i][j].occupant_name
                if(occupant_name == None):
                    occupant_name = "  "
                print_object[i][j] = occupant_name

        print(" ", end="")
        for i in range(self._DIMENSION):
            print("| %d  " % i, end="")
        print("|")
        print("-" * int(5.5 * self._DIMENSION), end="")
        print("")

        for row in range(self._DIMENSION):
            print(row,end="")
            for col in range(self._DIMENSION):
                print("| %s " % print_object[row][col], end="")
            print("|")
            print("-" * int(5.5 * self._DIMENSION), end="")
            print("")
            