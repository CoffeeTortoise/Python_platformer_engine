from engine.characters.playable.monos.dropping import Dropping
from engine.roots.properties.jump import Jump
import pygame as pg


class Jumper(Dropping, Jump):
    """A playable character who can only jump. Based on Dropping and Jump classes.
    Adds method keys. Methods update(), control_death() and __repr__() have
    been overridden."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 hp: int | float = 100, playable: bool = True,
                 gravity: int | float = 0, jump: int | float = 0):
        Dropping.__init__(self, sizes, pos, path, hp, playable, gravity)
        Jump.__init__(self, jump)

    def update(self):
        self.keys()
        self.dy()
        self.apply_gravity()
        self.control_death()
        dy = self.gravity + self.jump
        self.shift(dy=dy)

    def control_death(self):
        if self.hp <= 0:
            self.gravity = 0
            self.jump = 0

    def keys(self):
        """A method for processing keystrokes"""
        key = pg.key.get_pressed()
        self.jumped = False
        if key[pg.K_UP] and self.on_ground:
            self.jumped = True
            self.on_ground = False
        self.on_ground = False

    def __repr__(self):
        return Dropping.__repr__(self) + Jump.__repr__(self)

    def __del__(self):
        print('Jumper has been deleted')
