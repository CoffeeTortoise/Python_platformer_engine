

class Playable:
    """A class for storing the character's playability. Has property: playable.
    Method __repr__() has been overriden. By default, playable is False."""
    def __init__(self):
        self.__playable: bool = False

    @property
    def playable(self):
        return self.__playable

    @playable.setter
    def playable(self, new: bool):
        if type(new) is bool:
            self.__playable = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'playable: {self.__playable}'

    def __del__(self):
        print('Playable has been deleted')
