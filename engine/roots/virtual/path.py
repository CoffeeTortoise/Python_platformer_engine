

class Path:
    """A class used to storing path. Has property: path. Method __repr__()
    has been overriden"""
    def __init__(self, path: str):
        if type(path) is str:
            self.__path = path
        else:
            raise TypeError('Argument must be a string!')

    @property
    def path(self):
        """Path as a string"""
        return self.__path

    @path.setter
    def path(self, new: str):
        if type(new) is str:
            self.__path = new
        else:
            raise TypeError('Argument must be a string!')

    def __repr__(self):
        return f'path: {self.__path}'

    def __del__(self):
        print('Path has been deleted')
