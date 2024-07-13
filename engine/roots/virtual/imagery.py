from engine.constants.bounds import Bounds
import pygame as pg


class Imagery(Bounds):
    """The sprite class to assign image and rect values to. Based on a class Bounds.
    Adds properties: image, rect, pos, sizes, on_screen. Adds method draw(surface).
    Method __repr__() has been overriden"""
    def __init__(self):
        super().__init__()
        self.__image = None
        self.__rect = None
        self.__on_screen = True

    def draw(self, surface):
        """Draws a character if it's within the screen"""
        x, y = self.__rect.left, self.__rect.top
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                surface.blit(self.__image, self.__rect)
                self.__on_screen = True
            else:
                self.__on_screen = False
        else:
            self.__on_screen = False

    @property
    def pos(self):
        """Position of the character (left, top) as a tuple"""
        return self.__rect.left, self.__rect.top

    @pos.setter
    def pos(self, new: tuple[int | float, int | float]):
        if type(new) is tuple:
            if len(new) == 2:
                check1 = (type(new[0]) is int) or (type(new[0]) is float)
                check2 = (type(new[1]) is int) or (type(new[1]) is float)
                if check1 and check2:
                    self.__rect.left, self.__rect.top = new
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of new must be equal to 2!')
        else:
            raise TypeError('Argument must be a tuple!')

    @property
    def sizes(self):
        """Sizes of the character (width, height) as a tuple"""
        return self.__rect.width, self.__rect.height

    @sizes.setter
    def sizes(self, new: tuple[int | float, int | float]):
        if type(new) is tuple:
            if len(new) == 2:
                check1 = (type(new[0]) is int) or (type(new[0]) is float)
                check2 = (type(new[1]) is int) or (type(new[1]) is float)
                if check1 and check2:
                    x, y = self.__rect.left, self.__rect.top
                    self.__image = pg.transform.scale(self.__image, new)
                    self.__rect = self.__image.get_rect()
                    self.__rect.left, self.__rect.top = x, y
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of new must be equal to 2!')
        else:
            raise TypeError('Argument must be a tuple!')

    @property
    def image(self):
        """The pygame image attached to the character"""
        return self.__image

    @image.setter
    def image(self, new):
        self.__image = new

    @property
    def rect(self):
        """The pygame rectangle attached to the character"""
        return self.__rect

    @rect.setter
    def rect(self, new):
        self.__rect = new

    @property
    def on_screen(self):
        """Is the sprite on screen?"""
        return self.__on_screen

    @on_screen.setter
    def on_screen(self, new: bool):
        if type(new) is bool:
            self.__on_screen = new
        else:
            raise TypeError('Argument must be boolean!')

    def __repr__(self):
        return super().__repr__()

    def __del__(self):
        print('Imagery has been deleted')
