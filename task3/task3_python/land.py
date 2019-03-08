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

class Land:
    
    def __init__(self):
        self._occupied_obj = None

    @property
    def occupied_obj(self):
        return self._occupied_obj

    @occupied_obj.setter
    def occupied_obj(self, obj):
        self._occupied_obj = obj

    @property
    def occupant_name(self):
        try:
            return self.occupied_obj.name
        except:
            return None

    def coming(self, warrior):
        try:
            return self.occupied_obj.action_on_warrior(warrior)
        except:
            return True
    