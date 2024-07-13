from engine.roots.virtual.direction import Direction
from engine.tools.motions.rotation import Rotation
from engine.roots.alt.sprite import Sprite


class Rotated(Sprite, Direction):
    """A block rotating around it's center. Based on a Sprite and Direction classes.
    Adds property rotation. Methods update() and __repr__() have been overriden.
    By default, right is True(clockwise)."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 points: int = 12, slow: bool = False):
        Sprite.__init__(self, sizes, pos, path)
        Direction.__init__(self)
        sprite = Sprite(sizes, pos, path)
        self.__rotation = Rotation(sprite, points, slow)

    def update(self):
        """Controls the rotation of the block"""
        if self.right:
            center = self.rect.center
            self.image, self.rect = self.__rotation.rotate_clockwise()
            self.rect.center = center
        else:
            center = self.rect.center
            self.image, self.rect = self.__rotation.rotate_counterclockwise()
            self.rect.center = center

    @property
    def rotation(self):
        """Returns the object of rotation movement"""
        return self.__rotation

    def __repr__(self):
        return '\n'.join([Sprite.__repr__(self),
                          Direction.__repr__(self),
                          self.__rotation.__repr__()])

    def __del__(self):
        print('Rotated has been deleted')
