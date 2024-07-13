from engine.roots.properties.color import Color
from engine.roots.virtual.path import Path
from engine.roots.virtual.size import Size
import pygame as pg


class Font(Path, Size, Color):
    """A class representing font. Based on Path, Size and Color classes.
    Adds methods: get_text(txt), get_frame(txt, bg_color). Adds property: font.
    Method __repr__() has been overriden."""
    def __init__(self, path: str, size: int,
                 color: tuple[int, int, int] = (0, 0, 0)):
        Path.__init__(self, path)
        Size.__init__(self, size)
        Color.__init__(self, color)

    def get_text(self, txt: str):
        """Returns a simple text object"""
        if type(txt) is str:
            font = pg.font.Font(self.path, self.size)
            return font.render(txt, 1, self.color)
        else:
            raise TypeError('txt must be a string!')

    def get_frame(self, txt: str, bg_color: tuple[int, int, int]):
        """Returns a text object with background"""
        if type(txt) is str:
            if type(bg_color) is tuple:
                if len(bg_color) == 3:
                    for el in bg_color:
                        if not (type(el) is int):
                            raise TypeError('Elements of bg_color must be an integers!')
                    else:
                        font = pg.font.Font(self.path, self.size)
                        return font.render(txt, 1, self.color, bg_color)
                else:
                    return ValueError('Length of bg_color must be equal to 3!')
            else:
                raise TypeError('bg_color must be a tuple!')
        else:
            raise TypeError('txt must be a string!')

    @property
    def font(self):
        """Returns a font"""
        return pg.font.Font(self.path, self.size)

    def __repr__(self):
        reprs = [Path.__repr__(self), Size.__repr__(self), Color.__repr__(self)]
        return ''.join((rep + '\n') for rep in reprs)

    def __del__(self):
        print('Font has been deleted')
