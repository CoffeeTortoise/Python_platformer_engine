from engine.tools.motions.patrol import Patrol
from engine.roots.alt.sprite import Sprite


class Lift(Sprite):
    """A platform that moves like a lift. Based on a sprite class. Methods update()
        and shift(dx, dy) have been overriden. Adds property: patrol. By default,
        start is equal to starting position on the x-axis."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 speed: int | float = 0, start: int | float = 0,
                 end: int | float = 0):
        super().__init__(sizes, pos, path)
        if start == 0:
            start = self.pos[1]
        self.__patrol = Patrol(speed, start, end)

    def update(self):
        """Controls the movement of the character's patrol. Doesn't depend on the shifts
                 due to the camera"""
        y = self.__patrol.patrol(self.pos[1])
        self.pos = self.pos[0], y

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        super().shift(dx, dy)
        y1, y2 = self.__patrol.start, self.__patrol.end
        self.__patrol.start = y1 + dy
        self.__patrol.end = y2 + dy

    @property
    def patrol(self):
        """Returns the patrol movement associated with the character"""
        return self.__patrol

    def __repr__(self):
        return '\n'.join([super().__repr__(), self.__patrol.__repr__()])

    def __del__(self):
        print('Lift has been deleted')
