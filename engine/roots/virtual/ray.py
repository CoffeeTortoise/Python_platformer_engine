

class Ray:
    """A beam in one-dimensional dimension. Has properties: start, end. Method
    __repr__() has been overriden"""
    def __init__(self, start: int | float = 0, end: int | float = 0):
        check1 = (type(start) is int) or (type(start) is float)
        check2 = (type(end) is int) or (type(end) is float)
        if check1 and check2:
            self.__start = start
            self.__end = end
        else:
            raise TypeError('Arguments must be either integers or floats!')

    @property
    def start(self):
        """The initial coordinate"""
        return self.__start

    @start.setter
    def start(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__start = new
        else:
            raise TypeError('Start must be either integer or float!')

    @property
    def end(self):
        """The final coordinate"""
        return self.__end

    @end.setter
    def end(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__end = new
        else:
            raise TypeError('End must be either integer or float!')

    def __repr__(self):
        return f'{self.__start=}\n{self.__end=}'

    def __del__(self):
        print('Ray has been deleted')
