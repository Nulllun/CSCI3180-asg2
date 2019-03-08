import sys


if __name__ == "__main__":
    a = input('Input: ')
    b = []
    for i in range(len(a)):
        b.append(a[i])
    
    for i in range(len(b)):
        if b[i] == 'A':
            b[i] = 1
        if b[i] == 'B':
            b[i] = 2
        if b[i] == 'C':
            b[i] = 3
        if b[i] == 'D':
            b[i] = 4
        if b[i] == 'E':
            b[i] = 5
        if b[i] == 'F':
            b[i] = 6
        if b[i] == 'G':
            b[i] = 7
        if b[i] == 'H':
            b[i] = 8
    
    i = 0
    while i != len(b):
        print("%s %s" % (b[i+1], b[i]))
        i = i + 2
        
class Parent:
    
    def __init__(self, posx, posy):
        self._x = posx
        self._y = posy

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

class Child(Parent):

    def __init__(self, posx, posy):
        super(Child,self).__init__(posx, posy)

# constant use capital letter
