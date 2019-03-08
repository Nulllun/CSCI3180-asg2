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

from pos import Pos


class NPC:

    def __init__(self, posx, posy, index, map):
        self._map = map
        self._pos = Pos(posx, posy)
        self._index = index
        self._name = None
        self._power = None

    def talk(self, content):
        print(self._name + ": " + content)

    def action_on_warrior(self, warrior):
        return False

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        self._power = power    