

class Thick:
    """Class that contains thickness of a geometrical object like a border.
    Has property: line. Method __repr__() has been overriden"""
    def __init__(self, line: int):
        if type(line) is int:
            self.__line = line
        else:
            raise TypeError('line must be an integer!')

    @property
    def line(self):
        """Thickness as an integer"""
        return self.__line

    @line.setter
    def line(self, new: int):
        if type(new) is int:
            self.__line = new
        else:
            raise TypeError('line must be an integer!')

    def __repr__(self):
        return f'thickness: {self.__line}'

    def __del__(self):
        print('Thickness has been deleted')
