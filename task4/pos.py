class Pos:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    '''
    @property
    def pos(self):
        return self

    @pos.setter
    def pos(self, pos):
        self._x = pos.x
        self._y = pos.y
    '''