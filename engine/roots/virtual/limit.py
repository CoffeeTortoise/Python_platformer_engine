

class Limit:
    """Basically a numerical limit. Has property limit. Method __repr__() has
    been overriden"""
    def __init__(self, limit: int | float = 0):
        if (type(limit) is int) or (type(limit) is float):
            self.__limit = limit
        else:
            raise TypeError('Argument must be either integer or float!')

    @property
    def limit(self):
        """Numerical limit"""
        return self.__limit

    @limit.setter
    def limit(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__limit = new
        else:
            raise TypeError('Argument must either integer or float!')

    def __repr__(self):
        return f'{self.__limit=}'

    def __del__(self):
        print('Limit has been deleted')
