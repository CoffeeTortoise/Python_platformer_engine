from engine.roots.virtual.direction import Direction
from engine.roots.properties.speed import Speed


class Orientation(Direction, Speed):
    """A class for determining the direction of a character. Based on Speed and
    Direction classes. Adds method: define_right(). Method __repr__() has been
    overriden"""
    def __init__(self, speed: int | float = 0):
        Speed.__init__(self, speed)
        Direction.__init__(self)

    def define_right(self):
        """Determines the direction of the character's movement depending on the
        speed"""
        if self.speed > 0:
            self.right = True
        if self.speed < 0:
            self.right = False

    def __repr__(self):
        return Speed.__repr__(self) + '\n' + Direction.__repr__(self)

    def __del__(self):
        print('Orientation has been deleted')
