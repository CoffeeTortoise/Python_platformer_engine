from engine.roots.virtual.thick import Thick
from engine.roots.alt.rect import Rect
import pygame as pg


class Frame(Rect, Thick):
    """A class representing frame. Based on a Rect and Thick classes.
    Methods draw(surface) and __repr__() have been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 color: tuple[int, int, int] = (0, 0, 0), line: int = 0):
        Rect.__init__(self, sizes, pos, color)
        Thick.__init__(self, line)

    def draw(self, surface):
        """Draws the border on the screen"""
        x, y = self.vpos
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                pg.draw.rect(surface, self.color, (self.vpos, self.sizes), self.line)

    def __repr__(self):
        return Rect.__repr__(self) + Thick.__repr__(self)

    def __del__(self):
        print('Frame has been deleted')
