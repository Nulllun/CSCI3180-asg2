import random
from npc import NPC


class Elf(NPC):
    
    _MAGIC_CAP = 20

    def __init__(self, posx, posy, index, map):
        super(Elf,self).__init__(posx,posy,index,map)
        self._name = "E" + str(index)
        self._power = random.randint(0, self._MAGIC_CAP - 6) + 5

    def action_on_warrior(self, warrior):
        self.talk("My name is "+ self.name + ".  Welcome to my home.  " + "My magic power is " + str(self.power) + ".")
        self.talk("Your magic crystal is " + str(warrior.magic_crystal) + ".")
        self.talk("Do you need my help?")
        self.talk("You now have following options: ")
        print("1. Yes")
        print("2. No")
        a = input()

        if (a == '1'):
            value = random.randint(0, self.power - 3) + 2
            if(warrior.magic_crystal > value):
                warrior.decrease_crystal(value)
                warrior.increase_health(value)
                warrior.talk("Thanks for your help! " + self.name + ".")
            else:
                warrior.talk("Very embarrassing, I don't have enough crystals.")
        return False
