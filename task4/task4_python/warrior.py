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

import random
from pos import Pos


class Warrior:
    
    _HEALTH_CAP = 40

    def __init__(self, posx, posy, index, map):
        self._map = map
        self._pos = Pos(posx, posy)
        self._index = index
        self._name = "W" + str(index)
        self._health = self._HEALTH_CAP
        self._magic_crystal = 10

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health 

    @property
    def magic_crystal(self):
        return self._magic_crystal

    @magic_crystal.setter
    def magic_crystal(self, value):
        self._magic_crystal = value

    def increase_crystal(self, value):
        self.magic_crystal =  self.magic_crystal + value

    def decrease_crystal(self, value):
        self.magic_crystal = self.magic_crystal - value

    def increase_health(self, value):
        self.health = self.health + value

    def decrease_health(self, value):
        self.health = self.health - value

    def teleport(self):
        print("Hi, " + self.name + ". " + "Your position is (%s,%s) and health is %d." % (self.pos.x, self.pos.y, self.health))
        print("Specify your target position (Input 'x y').")
        posx = None
        posy = None
        while posx == None and posy == None:
            try:
                posx, posy = input().split(' ')
                posx = int(posx)
                posy = int(posy)
                if posx < 0 or posy < 0 or posx > 9 or posy > 9:
                    print("Invalid input")
                    print("Specify your target position (Input 'x y').")
                    posx = None
                    posy = None
                elif posx == self.pos.x and posy == self.pos.y:
                    print("Invalid input")
                    print("Specify your target position (Input 'x y'). It should not be the same as the original one.")
                    posx = None
                    posy = None
            except ValueError:
                print("Invalid input")
                print("Specify your target position (Input 'x y').")
                posx = None
                posy = None
        result = self._map.coming(posx,posy,self)
        if result:
            self._map.lands = (self.pos, None)
            self.pos = Pos(posx,posy)
            self._map.lands = (self.pos, self)
        if self.health <= 0:
            print("Very sorry, " + self.name + " has been killed.")
            self._map.lands = (self.pos, None)
            self._map.delete_teleportable_obj(self)
            self._map.decrease_num_of_alive_warriors()

    def talk(self, content):
        print(self.name + ": " + content)

    def action_on_warrior(self, other_warrior):
        self.talk("Hi, bro. You can call me %s. I am very happy to meet you. I have %d magic crystals." % (self.name,self.magic_crystal))
        self.talk("Need I share with you some magic crystals?")
        self.talk("You now have following options:")
        print("1.Yes")
        print("2.No")
        a = input()
        if (a == '1'):
            free_crystals = random.randint(0,self.magic_crystal)
            other_warrior.increase_crystal(free_crystals)
            self.decrease_crystal(free_crystals)
            other_warrior.talk("Thanks for your shared %d magic crystals!  %s." % (free_crystals,self.name))
            # return True means replace the position
        else:
            self.talk("See you!")
        # must return false as you do not want the warrior occupy the other warriors' position
        return False
