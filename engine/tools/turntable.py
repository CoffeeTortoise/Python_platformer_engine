from engine.roots.virtual.switcher import Switcher
import pygame as pg


class Turntable(Switcher):
    """A class for playing pygame music. Based on Switcher class. Adds method play().
    Adds properties music and active"""
    def __init__(self, path: str, on: bool = True):
        super().__init__(on)
        if not (type(path) is str):
            raise TypeError('path must be a string!')
        self.__music = pg.mixer.music
        self.__music.load(path)
        self.__active = False

    def play(self):
        """Plays music if in infinite loop if it is on"""
        if self.on:
            self.__activate_mus()
        else:
            self.__music.stop()
            self.__active = False

    def __activate_mus(self):
        if not self.__active:
            self.__music.play(-1)
            self.__active = True

    @property
    def music(self):
        """Returns pygame music object"""
        return self.__music

    @property
    def active(self):
        """Is the music active?"""
        return self.__active

    @active.setter
    def active(self, new: bool):
        if type(new) is bool:
            self.__active = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __del__(self):
        print('Turntable has been deleted')
