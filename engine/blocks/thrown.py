from engine.roots.properties.speed import Speed
from engine.blocks.rotated import Rotated


class Thrown(Rotated, Speed):
    """Thrown projectile, rotates when moving. Based on Rotated and Speed classes.
    Methods shift(dx, dy) and __repr__() have been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 points: int = 12, speed: int | float = 0,
                 slow: bool = False):
        Rotated.__init__(self, sizes, pos, path, points, slow)
        Speed.__init__(self, speed)

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        Rotated.shift(self, dx, dy)
        self.dx()
        self.rect.move_ip(self.speed, 0)

    def __repr__(self):
        return '\n'.join([Rotated.__repr__(self),
                          Speed.__repr__(self)])

    def __del__(self):
        print('Thrown has been deleted')
