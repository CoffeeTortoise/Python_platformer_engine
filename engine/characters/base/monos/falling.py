from engine.roots.properties.gravity import Gravity
from engine.characters.dummy import Dummy


class Falling(Dummy, Gravity):
    """A falling unplayable character. Based on Dummy and Gravity classes. Adds
    method control_death(). Methods update() and __repr__() have been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 hp: int | float = 100, playable: bool = False,
                 gravity: int | float = 0):
        Dummy.__init__(self, sizes, pos, path, hp, playable)
        Gravity.__init__(self, gravity)

    def update(self):
        self.apply_gravity()
        self.control_death()
        self.shift(dy=self.gravity)

    def control_death(self):
        """Invalidates physical characteristics if the character has died"""
        if self.hp <= 0:
            self.gravity = 0

    def __repr__(self):
        return Dummy.__repr__(self) + Gravity.__repr__(self)

    def __del__(self):
        print('Falling has been deleted')
