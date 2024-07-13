

class Direction:
    """A class used to storing the direction of movement. Has property: right.
    Method __repr__() has been overriden. By default, right is True."""
    def __init__(self):
        self.__right: bool = True

    @property
    def right(self):
        """Is the direction right?"""
        return self.__right

    @right.setter
    def right(self, new: bool):
        if type(new) is bool:
            self.__right = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'right: {self.__right}'

    def __del__(self):
        print('Direction has been deleted')
