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
    