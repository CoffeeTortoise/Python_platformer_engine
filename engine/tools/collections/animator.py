from engine.constants.animates import Animates
from engine.tools.timer import Timer
import pygame as pg


class Animator:
    """A class for creating animations (including right and left)"""
    def __init__(self, paths: list[str], sizes: tuple[int | float, int | float],
                 slow: bool = False):
        if not (type(paths) is list):
            raise TypeError('paths must be a list!')
        else:
            for el in paths:
                if not (type(el) is str):
                    raise TypeError('Elements in paths must be strings!')
        if not (type(sizes) is tuple):
            raise TypeError('sizes must be a tuple!')
        else:
            if not (len(sizes) == 2):
                raise ValueError('Length of sizes must be equal to 2!')
            else:
                for el in sizes:
                    if not ((type(el) is int) or (type(el) is float)):
                        raise TypeError('Elements must be an integers or floats!')
        if not (type(slow) is bool):
            raise TypeError('slow must be a boolean!')
        anime = Animates()
        raw = [pg.image.load(path).convert_alpha() for path in paths]
        self.__fr_t = anime.fr_t1 if slow else anime.fr_t2
        self.__right = [pg.transform.scale(img, sizes) for img in raw]
        self.__left = [pg.transform.flip(img, True, False) for img in self.__right]
        self.__length: int = len(self.__right) - 1
        self.__timer_right = Timer()
        self.__timer_left = Timer()

    def animate_right(self):
        """Returns the current frame for the right animation"""
        time = self.__timer_right.get_time()
        if time >= self.__fr_t * self.__length:
            time = 0
            self.__timer_right.restart()
        for i, image in enumerate(self.__right):
            if (i * self.__fr_t) >= time:
                return image

    def animate_left(self):
        """Returns the current frame for the left animation"""
        time = self.__timer_left.get_time()
        if time >= self.__fr_t * self.__length:
            time = 0
            self.__timer_left.restart()
        for i, image in enumerate(self.__left):
            if (i * self.__fr_t) >= time:
                return image

    def __repr__(self):
        return f'{self.__fr_t=}\n{self.__length=}'

    def __del__(self):
        print('Animator has been deleted')
