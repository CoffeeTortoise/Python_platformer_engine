from engine.roots.virtual.position import Position
from engine.roots.alt.sprite import Sprite
from engine.roots.alt.group import Group


class Camera(Position):
    """Class for simulating a camera. Useful only for playable characters.
    Based on a class Position. Adds method: world_shift(). Method __repr__()
    has been overriden. Adds property: delta."""
    def __init__(self, pos: tuple[int | float, int | float] = (0, 0),
                 delta: tuple[int | float, int | float] = (0, 0)):
        super().__init__(pos)
        if type(delta) is tuple:
            if len(delta) == 2:
                check1 = (type(delta[0]) is int) or (type(delta[0]) is float)
                check2 = (type(delta[1]) is int) or (type(delta[1]) is float)
                if check1 and check2:
                    self.__delta = delta
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of delta must be equal to 2!')
        else:
            raise TypeError('delta must be a tuple!')

    def world_shift(self, character=None, monsters=None,
                    blocks=None, interacts=None,
                    solid_interacts=None, background=None):
        """Shifts the world relative to a given point by a given offset, so that the
        character and environment are visible on the screen. Character must be
        an instance of Sprite, blocks and background are instances of Group"""
        dx, dy = 0, 0
        if isinstance(character, Sprite):
            dx = self.vpos[0] - character.pos[0] + self.__delta[0]
            dy = self.vpos[1] - character.pos[1] + self.__delta[1]
            character.shift(dx, dy)
        if isinstance(monsters, Group):
            monsters.shifts(dx, dy)
        if isinstance(blocks, Group):
            blocks.shifts(dx, dy)
        if isinstance(interacts, Group):
            interacts.shifts(dx, dy)
        if isinstance(solid_interacts, Group):
            solid_interacts.shifts(dx, dy)
        if isinstance(background, Group):
            background.shifts(dx, dy)

    @property
    def delta(self):
        """A tuple with specified axis offsets"""
        return self.__delta

    @delta.setter
    def delta(self, new: tuple[int | float, int | float]):
        if type(new) is tuple:
            if len(new) == 2:
                check1 = (type(new[0]) is int) or (type(new[0]) is float)
                check2 = (type(new[1]) is int) or (type(new[1]) is float)
                if check1 and check2:
                    self.__delta = new
                else:
                    raise TypeError('Elements must be either integers or floats!')
            else:
                raise ValueError('Length of delta must be equal to 2!')
        else:
            raise TypeError('delta must be a tuple!')

    def __repr__(self):
        return '\n'.join([f'delta: {self.__delta}', Position.__repr__(self)])

    def __del__(self):
        print('Camera has been deleted')
