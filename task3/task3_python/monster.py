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
from npc import NPC


class Monster(NPC):

    _DAMAGE_CAP = 20

    def __init__(self, posx, posy, index, map):
        super(Monster,self).__init__(posx,posy,index,map)
        self._name = "M" + str(index)
        self._power = random.randint(0, self._DAMAGE_CAP - 6) + 5

    def action_on_warrior(self, warrior):
        self.talk("I am the monster " + self.name + ".  Here is my territory.  " + "My damage power is " + str(self.power) + ".")
        self.talk("Your health is " + str(warrior.health) + ".")
        self.talk("Do you really want to challenge me?")
        self.talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a = input()
        if (a == '1'):
            if(warrior.health > self.power):
                warrior.decrease_health(self.power)
                warrior.increase_crystal(random.randint(0, 4) + 5)
                warrior.talk("Nice, I have killed the monster " + self.name + ".")
                self._map.decrease_num_of_alive_monsters()
                return True
            warrior.decrease_health(self.power)
        return False
