from engine.tools.motions.patrol import Patrol
from engine.blocks.spike import Spike


class HorizontalSpike(Spike):
    """A spike patrolling in horizontal direction. Based on Spike class. Methods
    update(), shift(dx, dy) and __repr__() have been overriden. Adds property
    patrol. By default, start is equal to a starting position on the x-axis."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 path: str, jump: int | float = 0,
                 attack: int | float = 0,
                 speed: int | float = 0,
                 start: int | float = 0,
                 end: int | float = 0):
        super().__init__(sizes, pos, path, jump, attack)
        if start == 0:
            start = self.pos[0]
        self.__patrol = Patrol(speed, start, end)

    def update(self):
        """Controls the movement of the character's patrol. Doesn't depend on the shifts
        due to the camera"""
        x = self.__patrol.patrol(self.pos[0])
        self.pos = x, self.pos[1]

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        super().shift(dx, dy)
        x1, x2 = self.__patrol.start, self.__patrol.end
        self.__patrol.start = x1 + dx
        self.__patrol.end = x2 + dx

    @property
    def patrol(self):
        """Returns the patrol movement associated with the character"""
        return self.__patrol

    def __repr__(self):
        return '\n'.join([super().__repr__(),
                          self.__patrol.__repr__()])

    def __del__(self):
        print('Horizontal spike has been deleted')
