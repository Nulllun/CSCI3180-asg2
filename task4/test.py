from land import Land


class H:

    def __init__(self):
        self.__x = 1
        self.__y = 1

    def hi(self):
        print('Hi')

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

class M(H):

    def __init__(self):
        self.__x = 2
        self.__y = 2
        self.__pos = Pos(5,5)
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos
    
class Pos:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

