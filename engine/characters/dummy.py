from engine.roots.properties.playable import Playable
from engine.roots.properties.health import Health
from engine.roots.alt.sprite import Sprite


class Dummy(Sprite, Health, Playable):
    """A class representing a dummy. Based on Sprite, Health and Playable classes.
    Methods draw(surface) and __repr__() have been overriden. By default, hp is 100,
    playable is False."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 hp: int | float = 100, playable: bool = False):
        Sprite.__init__(self, sizes, pos, path)
        Health.__init__(self, hp)
        Playable.__init__(self)
        if type(playable) is bool:
            self.playable = playable
        else:
            raise TypeError('playable must be a boolean!')

    def draw(self, surface):
        """The character will be drawn only if the hp is greater than 0"""
        if self.hp > 0:
            Sprite.draw(self, surface)

    def __repr__(self):
        reprs = [Sprite.__repr__(self), Health.__repr__(self),
                 Playable.__repr__(self)]
        return ''.join((rep + '\n') for rep in reprs)

    def __del__(self):
        print('Character has been deleted')
