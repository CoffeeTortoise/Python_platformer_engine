

class Switcher:
    """A class for storing switch positions(True, False). Has property: on.
    Method __repr__() has been overriden."""
    def __init__(self, on: bool = True):
        if type(on) is bool:
            self.__on = on
        else:
            raise TypeError('on must be a boolean!')

    @property
    def on(self):
        """Switcher's positions"""
        return self.__on

    @on.setter
    def on(self, new: bool):
        if type(new) is bool:
            self.__on = new
        else:
            raise TypeError('on must be a boolean!')

    def __repr__(self):
        return f'{self.__on=}'

    def __del__(self):
        print('Switcher has been deleted')
