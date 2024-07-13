from engine.roots.properties.orientation import Orientation
from engine.characters.playable.monos.jumper import Jumper
import pygame as pg


class Person(Jumper, Orientation):
    """A playable character with basic movements: walking and jumping. Based on Jumper
    and Orientation classes. Adds methods: shifting(), fix_physic(), change_image(),
    reset_physic(). Methods update(), control_death(), keys() and __repr__()
    have been overriden.
    Adds properties: normal, flipped, ready."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 hp: int | float = 100, playable: bool = True,
                 gravity: int | float = 0, jump: int | float = 0,
                 speed: int | float = 0):
        Jumper.__init__(self, sizes, pos, path, hp, playable, gravity, jump)
        Orientation.__init__(self, speed)
        self.__normal = self.image
        self.__flipped = pg.transform.flip(self.__normal, True, False)
        self.__ready: bool = False

    def update(self):
        self.reset_physic()
        self.keys()
        self.dx()
        self.dy()
        self.apply_gravity()
        self.fix_physic()

    def shifting(self):
        """Shifts the character depending on the movement, changes the image depending
        on the direction"""
        self.change_image()
        self.control_death()
        dx, dy = self.speed, self.jump + self.gravity
        self.shift(dx, dy)

    def control_death(self):
        if self.hp <= 0:
            self.speed = 0
            self.jump = 0
            self.gravity = 0

    def fix_physic(self):
        """Imposes restrictions on the speed and the character's jump force"""
        if abs(self.speed) >= self.rect.width:
            self.speed = self.rect.width if self.right else -self.rect.width
        if abs(self.jump) >= self.rect.height * 3:
            self.jump = -self.rect.height * 3

    def keys(self):
        self.jumped, self.can_go = False, False
        key = pg.key.get_pressed()
        if key[pg.K_UP] and self.on_ground:
            self.jumped = True
            self.on_ground = False
        if key[pg.K_RIGHT]:
            self.can_go = True
            if self.max_speed < 0:
                self.max_speed *= -1
        if key[pg.K_LEFT]:
            self.can_go = True
            if self.max_speed > 0:
                self.max_speed *= -1
        self.on_ground = False

    def change_image(self):
        """Changes the character's image depending on the direction"""
        self.define_right()
        self.turn_image()

    def turn_image(self):
        """Reflects the first frame of the character to the left or right
        depending on the direction"""
        if self.right:
            self.image = self.__normal
        else:
            self.image = self.__flipped

    def reset_physic(self):
        """Resets gravity, speed and jump of the object, so it becomes ready"""
        if not self.__ready:
            self.reset_gravity()
            self.reset_jump()
            self.reset_speed()
            self.__ready = True

    @property
    def normal(self):
        """Basically the image when moving to the right"""
        return self.__normal

    @normal.setter
    def normal(self, new):
        self.__normal = new

    @property
    def flipped(self):
        """Basically the image when moving to the left"""
        return self.__flipped

    @flipped.setter
    def flipped(self, new):
        self.__flipped = new

    @property
    def ready(self):
        """Character readiness"""
        return self.__ready

    @ready.setter
    def ready(self, new: bool):
        if type(new) is bool:
            self.__ready = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return '\n'.join([Jumper.__repr__(self), Orientation.__repr__(self)])

    def __del__(self):
        print('Person has been deleted')
