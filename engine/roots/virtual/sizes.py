

class Sizes:
    """Class that contains sizes of an object as a tuple. Has property: sizes.
    Method __repr__ has been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float] = (0, 0)):
        if type(sizes) is tuple:
            if len(sizes) == 2:
                check1 = (type(sizes[0]) is int) or (type(sizes[0]) is float)
                check2 = (type(sizes[1]) is int) or (type(sizes[1]) is float)
                if check1 and check2:
                    self.__sizes: tuple[int | float, int | float] = sizes
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Lengths of sizes must be equal to 2!')
        else:
            raise TypeError('Sizes must be a tuple!')

    @property
    def sizes(self):
        """Sizes of an object as tuple"""
        return self.__sizes

    @sizes.setter
    def sizes(self, new: tuple[int | float, int | float]):
        if type(new) is tuple:
            if len(new) == 2:
                check1 = (type(new[0]) is int) or (type(new[0]) is float)
                check2 = (type(new[1]) is int) or (type(new[1]) is float)
                if check1 and check2:
                    self.__sizes = new
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of new must be equal to 2!')
        else:
            raise TypeError('Sizes must be a tuple!')

    def __repr__(self):
        return f'sizes: {self.__sizes}'

    def __del__(self):
        print('Sizes has been deleted')
