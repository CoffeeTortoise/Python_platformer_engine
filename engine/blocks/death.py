from engine.tools.motions.circular import Circular
from engine.blocks.spike import Spike


class DeathWheel(Spike):
    """An entity that moves like a Ferris wheel, but have an attack. Based on a
    Spike class. Methods update(), shift(dx, dy) and __repr__() have been overriden.
    Adds property: circular."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 radius: int | float,
                 path: str,
                 pos: tuple[int | float, int | float] = (0, 0),
                 speed: int | float = 0,
                 jump: int | float = 0,
                 attack: int | float = 0):
        super().__init__(sizes, pos, path, jump, attack)
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
        return '\n'.join([super().__repr__(),
                          self.__circular.__repr__()])

    def __del__(self):
        print('Death wheel has been deleted')
