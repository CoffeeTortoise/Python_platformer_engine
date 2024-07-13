from engine.roots.virtual.imagery import Imagery
from typing import Self
import pygame as pg


class Sprite(Imagery):
    """Character's sprite. Based on a class Imagery. Adds methods: update(),
    shift(dx, dy). Methods __repr__ and  __eq__ have been overriden."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str):
        super().__init__()
        if not (type(sizes) is tuple):
            raise TypeError('sizes must be a tuple!')
        else:
            if not (len(sizes) == 2):
                raise ValueError('Length of sizes must be equal to 2!')
            else:
                for el in sizes:
                    if not ((type(el) is int) or (type(el) is float)):
                        raise TypeError('Elements must be either integers or floats!')
        if not (type(pos) is tuple):
            raise TypeError('pos must be a tuple!')
        else:
            if not (len(pos) == 2):
                raise ValueError('Length of pos must be equal to 2!')
            else:
                for el in pos:
                    if not ((type(el) is int) or (type(el) is float)):
                        raise TypeError('Elements must be either integers or floats!')
        if not (type(path) is str):
            raise TypeError('path must be a string')
        image = pg.image.load(path).convert_alpha()
        self.image = pg.transform.scale(image, sizes)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos[0], pos[1]

    def update(self):
        """The method describes the logic for the character. Must be overriden."""
        pass

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        """Shifts the character along the x and y axes"""
        check1 = (type(dx) is int) or (type(dx) is float)
        check2 = (type(dy) is int) or (type(dy) is float)
        if check1 and check2:
            self.rect.move_ip(dx, dy)
        else:
            raise TypeError('Arguments must be either integers or floats!')

    def __repr__(self):
        pos = self.rect.left, self.rect.top
        sizes = self.rect.width, self.rect.height
        return f'pos: {pos}\nsizes: {sizes}\n' + super().__repr__()

    def __eq__(self, other: Self):
        return (self.rect == other.rect) and (self.image == other.image)

    def __del__(self):
        print('Sprite has been deleted')
