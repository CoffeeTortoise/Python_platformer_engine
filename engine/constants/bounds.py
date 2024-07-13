from engine.constants.window import Window


class Bounds:
    """A class for storing horizontal and vertical screen borders. Has properties:
    hor_bounds, ver_bounds. Method __repr__ has been overriden."""
    def __init__(self):
        bounds = Window()
        self.__x1, self.__x2 = -bounds.size * 5, bounds.wnd_size[0] + bounds.size * 5
        self.__y1, self.__y2 = -bounds.size * 5, bounds.wnd_size[1] + bounds.size * 5

    @property
    def hor_bounds(self):
        """Returns horizontal bounds as a tuple"""
        return self.__x1, self.__x2

    @property
    def ver_bounds(self):
        """Returns vertical bounds as a tuple"""
        return self.__y1, self.__y2

    def __repr__(self):
        x = f'Horizontal bounds: {self.__x1}, {self.__x2}\n'
        y = f'Vertical bounds: {self.__y1}, {self.__y2}\n'
        return x + y

    def __del__(self):
        print('Bounds has been deleted')
