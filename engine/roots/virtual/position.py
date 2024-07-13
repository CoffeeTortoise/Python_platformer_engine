

class Position:
    """A class for storing the position of an object in 2D world.
    The class object can be used for mathematical and logical operations with
    tuples, returns a tuple. Has a length. Has property pos."""
    def __init__(self, pos: tuple[int | float, int | float] = (0, 0)):
        if type(pos) is tuple:
            if len(pos) == 2:
                check1 = (type(pos[0]) is int) or (type(pos[0]) is float)
                check2 = (type(pos[1]) is int) or (type(pos[1]) is float)
                if check1 and check2:
                    self.__vpos: tuple[int | float, int | float] = pos
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of pos must be equal to 2!')
        else:
            raise TypeError('Pos must be a tuple!')

    @property
    def vpos(self):
        """Position of a number as tuple"""
        return self.__vpos

    @vpos.setter
    def vpos(self, new: tuple[int | float, int | float]):
        if type(new) is tuple:
            if len(new) == 2:
                check1 = (type(new[0]) is int) or (type(new[0]) is float)
                check2 = (type(new[1]) is int) or (type(new[1]) is float)
                if check1 and check2:
                    self.__vpos = new
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of new must be equal to 2!')
        else:
            raise TypeError('New must be a tuple!')

    def __repr__(self):
        return f'vpos: {self.__vpos}'

    def __eq__(self, other):
        return self.__vpos == other

    def __ne__(self, other):
        return self.__vpos != other

    def __gt__(self, other):
        return self.__vpos > other

    def __ge__(self, other):
        return self.__vpos >= other

    def __lt__(self, other):
        return self.__vpos < other

    def __le__(self, other):
        return self.__vpos <= other

    def __add__(self, other):
        return tuple(map(lambda i, j: i + j, self.__vpos, other))

    def __radd__(self, other):
        return tuple(map(lambda i, j: i + j, other, self.__vpos))

    def __sub__(self, other):
        return tuple(map(lambda i, j: i - j, self.__vpos, other))

    def __rsub__(self, other):
        return tuple(map(lambda i, j: i - j, other, self.__vpos))

    def __mul__(self, other):
        return tuple(map(lambda i, j: i * j, self.__vpos, other))

    def __rmul__(self, other):
        return tuple(map(lambda i, j: i * j, other, self.__vpos))

    def __truediv__(self, other):
        return tuple(map(lambda i, j: i / j, self.__vpos, other))

    def __rtruediv__(self, other):
        return tuple(map(lambda i, j: i / j, other, self.__vpos))

    def __floordiv__(self, other):
        return tuple(map(lambda i, j: i // j, self.__vpos, other))

    def __rfloordiv__(self, other):
        return tuple(map(lambda i, j: i // j, other, self.__vpos))

    def __mod__(self, other):
        return tuple(map(lambda i, j: i % j, self.__vpos, other))

    def __rmod__(self, other):
        return tuple(map(lambda i, j: i % j, other, self.__vpos))

    def __pow__(self, power):
        return tuple(map(lambda i, j: i ** j, self.__vpos, power))

    def __rpow__(self, power):
        return tuple(map(lambda i, j: i ** j, power, self.__vpos))

    def __pos__(self):
        return tuple(map(lambda i: i, self.__vpos))

    def __neg__(self):
        return tuple(map(lambda i: -i, self.__vpos))

    def __abs__(self):
        return tuple(map(lambda i: abs(i), self.__vpos))

    def __len__(self):
        return len(self.__vpos)

    def __del__(self):
        print('Position has been deleted')
