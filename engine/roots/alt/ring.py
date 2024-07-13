from engine.roots.virtual.thick import Thick
from engine.roots.alt.circle import Circle
import pygame as pg


class Ring(Circle, Thick):
    """A class representing ring. Based on Circle and Thick classes. Methods
    draw(surface) and __repr__() have been overriden."""
    def __init__(self, radius: int | float, pos: tuple[int | float, int | float],
                 color: tuple[int, int, int] = (0, 0, 0), line: int = 0):
        Circle.__init__(self, radius, pos, color)
        Thick.__init__(self, line)

    def draw(self, surface):
        """Draws a ring on a string"""
        x, y = self.vpos
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                pg.draw.circle(surface, self.color, self.vpos, self.radius, self.line)

    def __repr__(self):
        return Circle.__repr__(self) + Thick.__repr__(self)

    def __del__(self):
        print('Ring has been deleted')
