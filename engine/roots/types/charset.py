

class Charset:
    """A secure class for storing strings. Supports concatenation, have == operator.
    Has property: var"""
    def __init__(self, var: str):
        self.__msg = 'This is not a string!'
        self.__warn = 'Value must be a String object!'
        if type(var) is str:
            self.__var: str = var
        else:
            raise TypeError(self.__msg)

    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, new):
        if type(new) is str:
            del self.__var
            self.__var = new
        else:
            raise TypeError(self.__msg)

    def __repr__(self):
        return self.__var

    def __add__(self, other):
        if type(other) is type(self):
            res: str = self.__var + other.var
            return Charset(res)
        else:
            raise TypeError(self.__warn)

    def __radd__(self, other):
        if type(other) is type(self):
            res: str = other.var + self.__var
            return Charset(res)
        else:
            raise TypeError(self.__warn)

    def __iadd__(self, other):
        if type(other) is type(self):
            res: str = self.__var + other.var
            self.__var = res
            return self
        else:
            raise TypeError(self.__warn)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__var == other.var
        else:
            raise TypeError(self.__warn)

    def __del__(self):
        print('String has been deleted')
