

class Color:
    """A class for storing the color of an object. Has property: color.
    Method __repr__() has been overriden"""
    def __init__(self, color: tuple[int, int, int] = (0, 0, 0)):
        if type(color) is tuple:
            if len(color) == 3:
                for num in color:
                    if not (type(num) is int):
                        raise TypeError('Elements must be an integers!')
                else:
                    self.__color = color
            else:
                raise ValueError('Length of color must be equal to 3!')
        else:
            raise TypeError('color must be a tuple!')

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new: tuple[int, int, int]):
        if type(new) is tuple:
            if len(new) == 3:
                for el in new:
                    if not (type(el) is int):
                        raise TypeError('Elements must be an integers!')
                else:
                    self.__color = new
            else:
                raise ValueError('Length of color must be equal to 3!')
        else:
            raise TypeError('color must be a tuple!')

    def __repr__(self):
        return f'color: {self.__color}'

    def __del__(self):
        print('Color has been deleted')
