from engine.tools.collections.animator import Animator
from engine.roots.virtual.direction import Direction
from engine.roots.virtual.switcher import Switcher
from engine.roots.alt.sprite import Sprite
import pygame as pg


class Animated(Sprite, Direction, Switcher):
    """A block with a given animation. Based on Sprite, Direction and Switcher classes.
    Adds method animation. Methods update and __repr__() have been overriden. Adds
    properties: normal, flipped and animator. By default, animation has normal speed."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 paths: list[str], on: bool = True, slow: bool = False):
        Sprite.__init__(self, sizes, pos, paths[0])
        Direction.__init__(self)
        Switcher.__init__(self, on)
        self.__normal = self.image
        self.__flipped = pg.transform.flip(self.image, True, False)
        self.__animator = Animator(paths, sizes, slow)

    def update(self):
        """Plays an animation of the block if the switcher is on"""
        if self.on:
            self.animation()
        else:
            self.turn_image()

    def animation(self):
        """Plays right or left animation"""
        if self.right:
            self.image = self.__animator.animate_right()
        else:
            self.image = self.__animator.animate_left()

    def turn_image(self):
        """Reflects the first frame of the character to the left or right
                depending on the direction"""
        if self.right:
            self.image = self.__normal
        else:
            self.image = self.__flipped

    @property
    def normal(self):
        """The first frame of the right animation"""
        return self.__normal

    @normal.setter
    def normal(self, new):
        self.__normal = new

    @property
    def flipped(self):
        """The first frame of the left animation"""
        return self.__flipped

    @flipped.setter
    def flipped(self, new):
        self.__flipped = new

    @property
    def animator(self):
        """Returns an animator attached to this object"""
        return self.__animator

    def __repr__(self):
        return '\n'.join([Sprite.__repr__(self),
                          Direction.__repr__(self),
                          Switcher.__repr__(self)])

    def __del__(self):
        print('Animated block has been deleted')
