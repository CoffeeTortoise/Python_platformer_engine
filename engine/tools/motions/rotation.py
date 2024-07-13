from engine.roots.virtual.imagery import Imagery
from engine.constants.animates import Animates
from engine.roots.alt.sprite import Sprite
from engine.tools.timer import Timer
import pygame as pg


class Rotation:
    """A class for creating rotation around it's center. Has methods:
    rotate_clockwise(), rotate_counterclockwise(). Has property: frame_time.
    Method __repr__() has been overriden"""
    def __init__(self, sprite: Sprite, points: int = 12, slow: bool = False):
        if not isinstance(sprite, Sprite):
            raise TypeError('sprite must be an instance of Sprite!')
        if not (type(points) is int):
            raise TypeError('points must be an integer!')
        if not (type(slow) is bool):
            raise TypeError('slow must be a boolean!')
        step = 360 / points
        self.__normal, self.__flipped = [], []
        for i in range(points + 1):
            frame = Imagery()
            frame.image = pg.transform.rotate(sprite.image, step * i)
            frame.rect = frame.image.get_rect()
            frame.rect.center = sprite.rect.center
            self.__normal.append(frame)
        for frame in self.__normal:
            flipped = Imagery()
            flipped.image = pg.transform.flip(frame.image, True, False)
            flipped.rect = flipped.image.get_rect()
            flipped.rect.center = sprite.rect.center
            self.__flipped.append(flipped)
        anime = Animates()
        self.__length = len(self.__normal) - 1
        self.__fr_t = anime.fr_t1 if slow else anime.fr_t2
        self.__timer_clockwise = Timer()
        self.__timer_counterclockwise = Timer()

    def rotate_counterclockwise(self):
        """Returns an image and a rectangle to rotate counterclockwise for
        the current time"""
        time = self.__timer_counterclockwise.get_time()
        if time >= self.__length * self.__fr_t:
            time = 0
            self.__timer_counterclockwise.restart()
        for i, imagery in enumerate(self.__normal):
            if i * self.__fr_t >= time:
                return imagery.image, imagery.rect

    def rotate_clockwise(self):
        """Returns an image and a rectangle to rotate clockwise for
        the current time"""
        time = self.__timer_clockwise.get_time()
        if time >= self.__length * self.__fr_t:
            time = 0
            self.__timer_clockwise.restart()
        for i, imagery in enumerate(self.__flipped):
            if i * self.__fr_t >= time:
                return imagery.image, imagery.rect

    @property
    def frame_time(self):
        """Just frame time"""
        return self.__fr_t

    @frame_time.setter
    def frame_time(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__fr_t = new
        else:
            raise TypeError('frame time must be an integer or float!')

    def __repr__(self):
        return f'{self.__length=}\n{self.__fr_t=}'

    def __del__(self):
        print('Rotation has been deleted')
