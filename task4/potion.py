import random
from pos import Pos

class Potion:

    _HEAL_CAP = 20

    def __init__(self, posx, posy, index, map):
        self._map = map
        self._pos = Pos(posx,posy)
        self._index = index
        self._name = "P" + str(index)
        self._power = random.randint(0,self._HEAL_CAP - 6) + 5

    @property
    def power(self):
        return self._power

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos

    @property
    def name(self):
        return self._name

    def action_on_warrior(self, warrior):
        warrior.talk("Very good, I got additional healing potion %s." % self.name)
        warrior.increase_health(self.power)
        if warrior.health > 40:
            warrior.health = 40
        self._map.delete_teleportable_obj(self)
        # return True means the warrior will occupy this position
        return True

    def teleport(self):
        # print("Teleporting "+self.name)
        self._map.lands = (self.pos, None)
        self.pos = self._map.get_un_occupied_position()
        self._map.lands = (self.pos, self)
        # print("Teleport finish "+self.name)
