

class Radius:
    """Class that contains radius of a circle. Has property: radius. Method __repr__
    has been overriden."""
    def __init__(self, radius: int | float):
        if (type(radius) is int) or (type(radius) is float):
            self.__radius = radius
        else:
            raise TypeError('Radius must be either integer or float!')

    @property
    def radius(self):
        """Radius of a circle"""
        return self.__radius

    @radius.setter
    def radius(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__radius = new
        else:
            raise TypeError('Radius must be either integer or float!')

    def __repr__(self):
        return f'radius: {self.__radius}'

    def __del__(self):
        print('Radius has been deleted')
