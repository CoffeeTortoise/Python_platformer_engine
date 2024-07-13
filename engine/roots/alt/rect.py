from engine.roots.virtual.position import Position
from engine.roots.properties.color import Color
from engine.roots.virtual.sizes import Sizes
from engine.constants.bounds import Bounds
import pygame as pg


class Rect(Position, Color, Sizes, Bounds):
    """A class representing rectangle. Based on Position, Color, Sizes and Bounds classes.
    Adds method: update(), draw(surface), shift(dx, dy). Adds property: rect.
    Method __repr__ has been overriden. By default, color is (0, 0, 0)"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 color: tuple[int, int, int] = (0, 0, 0)):
        Position.__init__(self, pos)
        Color.__init__(self, color)
        Sizes.__init__(self, sizes)
        Bounds.__init__(self)

    def update(self):
        """Logic attached to the rectangle. Must be overriden."""
        pass

    def draw(self, surface):
        """Draws the rectangle on the screen"""
        x, y = self.vpos
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                pg.draw.rect(surface, self.color, (self.vpos, self.sizes))

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        """Shifts the rectangle along with x and y axes"""
        check1 = (type(dx) is int) or (type(dx) is float)
        check2 = (type(dy) is int) or (type(dy) is float)
        if check1 and check2:
            x, y = self.vpos[0] + dx, self.vpos[1] + dy
            self.vpos = x, y
        else:
            raise TypeError('Arguments must be either integers or floats!')

    @property
    def rect(self):
        """Returns a pygame rectangle"""
        return pg.rect.Rect(self.vpos, self.sizes)

    def __repr__(self):
        reprs = [Position.__repr__(self), Color.__repr__(self),
                 Sizes.__repr__(self), Bounds.__repr__(self)]
        return ''.join((rep + '\n') for rep in reprs)

    def __del__(self):
        print('Geometric rectangle has been deleted')
