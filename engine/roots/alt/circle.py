from engine.roots.virtual.position import Position
from engine.roots.properties.color import Color
from engine.roots.virtual.radius import Radius
from engine.constants.bounds import Bounds
import pygame as pg


class Circle(Color, Position, Radius, Bounds):
    """A class representing circle. Based on Color, Position, Radius and Bounds classes.
     Adds method: update(), draw(surface), shift(dx, dy). Adds property: rect.
     By default, color is (0, 0, 0)"""
    def __init__(self, radius: int | float, pos: tuple[int | float, int | float],
                 color: tuple[int, int, int] = (0, 0, 0)):
        Color.__init__(self, color)
        Position.__init__(self, pos)
        Radius.__init__(self, radius)
        Bounds.__init__(self)

    def update(self):
        """A method that contains logic of an entity. Must be overriden."""
        pass

    def draw(self, surface):
        """Draws the circle on a screen"""
        x, y = self.vpos
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                pg.draw.circle(surface, self.color, self.vpos, self.radius)

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        check1 = (type(dx) is int) or (type(dx) is float)
        check2 = (type(dy) is int) or (type(dy) is float)
        if check1 and check2:
            x, y = self.vpos[0] + dx, self.vpos[1] + dy
            self.vpos = x, y
        else:
            raise TypeError('Arguments must be either integers or floats!')

    @property
    def rect(self):
        """Returns a rectangle equivalent to a circle"""
        pos = self.vpos[0] - self.radius, self.vpos[1] - self.radius
        sizes = self.radius * 2, self.radius * 2
        return pg.rect.Rect(pos, sizes)

    def __repr__(self):
        reprs = [Color.__repr__(self), Position.__repr__(self),
                 Radius.__repr__(self), Bounds.__repr__(self)]
        return ''.join((rep + '\n') for rep in reprs)

    def __del__(self):
        print('Circle has been deleted')
