import pygame as pg
pg.init()


class Window:
    """A class containing basic information about window sizes and the standard
    block size. Has properties: rows, cols, size, wnd_size. The __repr__ method
    has been redefined."""
    def __init__(self):
        wnd_info = pg.display.Info()
        wnd_raw_size: tuple[int, int] = wnd_info.current_w, wnd_info.current_h
        self.__rows: int = 24
        self.__cols: int = 42
        self.__size: float = wnd_raw_size[1]/self.__rows
        self.__wnd_size: tuple[float, float] = (self.__size * self.__cols,
                                                self.__size * self.__rows)

    @property
    def rows(self):
        """Returns the vertical size in blocks"""
        return self.__rows

    @property
    def cols(self):
        """Returns the horizontal size in blocks"""
        return self.__cols

    @property
    def size(self):
        """Returns the block size in pixels"""
        return self.__size

    @property
    def wnd_size(self):
        """Returns a tuple with the size of the game screen: (width, height)"""
        return self.__wnd_size

    def __repr__(self):
        return f'Rows: {self.__rows}\nCols: {self.__cols}\nSize: {self.__size}\nWnd size: {self.__wnd_size}'

    def __del__(self):
        print('Constants for sizes has been deleted')
