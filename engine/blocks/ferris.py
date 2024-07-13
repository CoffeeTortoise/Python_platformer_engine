from engine.tools.motions.circular import Circular
from engine.roots.alt.sprite import Sprite


class Ferris(Sprite):
    """An entity that moves like a Ferris wheel. Based on a Sprite class.
    Methods update(), shift(dx, dy) and __repr__() have been overriden.
    Adds property: circular."""
    def __init__(self, sizes: tuple[int | float, int | float], path: str,
                 radius: int | float,
                 pos: tuple[int | float, int | float] = (0, 0),
                 speed: int | float = 0):
        super().__init__(sizes, pos, path)
        self.__circular = Circular(radius, pos, speed)

    def update(self):
        """Creates a character's movement around the circle"""
        self.pos = self.__circular.move_circular()

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        check1 = (type(dx) is int) or (type(dx) is float)
        check2 = (type(dy) is int) or (type(dy) is float)
        if check1 and check2:
            x, y = self.__circular.vpos
            self.__circular.vpos = x + dx, y + dy
        else:
            raise TypeError('Arguments must be either integers or floats!')

    @property
    def circular(self):
        """Returns a model of movement along circle of a given radius and center at
        a given speed"""
        return self.__circular

    def __repr__(self):
        return '\n'.join([self.__circular.__repr__(), super().__repr__()])

    def __del__(self):
        print('Ferris wheel has been deleted')
