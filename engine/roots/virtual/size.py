

class Size:
    """A class used to storing 1 size. Has property: size. Method __repr__() has
    been overriden"""
    def __init__(self, size: int):
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError('Size must be an integer!')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new: int):
        if type(new) is int:
            self.__size = new
        else:
            raise TypeError('Size must be an integer!')

    def __repr__(self):
        return f'size: {self.__size}'

    def __del__(self):
        print('Size has been deleted')
