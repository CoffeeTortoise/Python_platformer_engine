from engine.roots.virtual.position import Position
from engine.roots.virtual.radius import Radius
from engine.roots.properties.speed import Speed
import math as mt


class Circular(Position, Radius, Speed):
    """Creates a circular motion. If the speed is too high or too low, it may not
    work. Based on Position, Radius and Speed classes. Adds method: move_circular().
    Method __repr__() has been overriden."""
    def __init__(self, radius: int | float,
                 pos: tuple[int | float, int | float] = (0, 0),
                 speed: int | float = 0):
        Position.__init__(self, pos)
        Radius.__init__(self, radius)
        Speed.__init__(self, speed)
        self.__t: int | float = 0

    def move_circular(self):
        """Creates coordinates for movement around a circle of a given radius and
        center"""
        x = self.radius * mt.cos(self.__t) + self.vpos[0]
        y = self.radius * mt.sin(self.__t) + self.vpos[1]
        self.__control_t()
        return x, y

    def __control_t(self):
        # Creates the parameter t for the coordinate equation
        self.dx()
        self.__t += self.speed
        if self.speed < 0 and self.__t <= -mt.pi * 2:
            self.__t = 0
        if self.speed > 0 and self.__t >= mt.pi * 2:
            self.__t = 0

    def __repr__(self):
        return '\n'.join([f'{self.__t=}', Position.__repr__(self),
                          Radius.__repr__(self), Speed.__repr__(self)])

    def __del__(self):
        print('Circular motion has been deleted')
