from engine.roots.properties.playable import Playable
from engine.roots.properties.health import Health
from engine.roots.virtual.direction import Direction
from engine.blocks.reversible import HorizontalSpike
import pygame as pg


class Mobster(HorizontalSpike, Direction, Health, Playable):
    """A single-frame monster that patrols the site. Based on HorizontalSpike,
    Direction, Health and Playable classes. Adds methods define_right(), turn_image()
    and control_death(). Methods update(), draw(surface), interact(character) and
    __repr__() have been overriden. Adds properties: flipped, normal."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 path: str, jump: int | float = 0,
                 attack: int | float = 0,
                 speed: int | float = 0,
                 start: int | float = 0,
                 end: int | float = 0,
                 hp: int | float = 100,
                 playable: bool = False):
        HorizontalSpike.__init__(self, sizes, pos, path, jump, attack,
                                 speed, start, end)
        Direction.__init__(self)
        Health.__init__(self, hp)
        Playable.__init__(self)
        self.playable = playable
        self.__normal = self.image
        self.__flipped = pg.transform.flip(self.image, True, False)

    def update(self):
        """Controls the movement and changes the frame"""
        if self.hp > 0:
            HorizontalSpike.update(self)
            self.change_image()

    def draw(self, surface):
        """Draws a character if it's alive and on the screen"""
        if self.hp > 0:
            HorizontalSpike.draw(self, surface)

    def interact(self, character):
        """If a character jumps on a monster, then damage is done to the monster"""
        if self.hp > 0:
            HorizontalSpike.damage(self)
            HorizontalSpike.check_touch(self, character)
            if self.touched:
                character.hp -= self.attack
                if not character.on_ground:
                    self.hp -= character.attack
                HorizontalSpike.lift_character(self, character)

    def define_right(self):
        """Determines the direction of the character's movement depending on the
        speed"""
        if self.patrol.speed > 0:
            self.right = True
        if self.patrol.speed < 0:
            self.right = False

    def turn_image(self):
        """Reflects the first frame of the character to the left or right
        depending on the direction"""
        if self.right:
            self.image = self.__normal
        else:
            self.image = self.__flipped

    def change_image(self):
        """Changes the character's image depending on the direction"""
        self.define_right()
        self.turn_image()

    def control_death(self):
        """Invalidates character's characteristics if it's dead"""
        if self.hp <= 0:
            self.attack = 0
            self.jump = 0
            self.patrol.speed = 0

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

    def __repr__(self):
        return '\n'.join([HorizontalSpike.__repr__(self),
                          Direction.__repr__(self),
                          Health.__repr__(self),
                          Playable.__repr__(self)])

    def __del__(self):
        print('Mobster has been deleted')
