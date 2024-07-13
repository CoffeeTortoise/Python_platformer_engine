from engine.characters.playable.monos.person import Person
from engine.tools.collections.animator import Animator


class Hero(Person):
    """Character class with motion animation. Based on a class Person. Adds method
    animation(). Methods change_image() and __repr__() have been overriden. Adds
    property animator. By default, animation has normal speed"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], paths: list[str],
                 hp: int | float = 100, playable: bool = True,
                 gravity: int | float = 0, jump: int | float = 0,
                 speed: int | float = 0, slow: bool = False):
        super().__init__(sizes, pos, paths[0], hp, playable, gravity, jump, speed)
        self.__animator = Animator(paths, sizes, slow)

    def change_image(self):
        """Changes the character's image depending on the direction or speed"""
        self.define_right()
        if self.speed != 0:
            self.animation()
        else:
            self.turn_image()

    def animation(self):
        """Plays the character's motion animation"""
        if self.speed > 0:
            self.image = self.__animator.animate_right()
        if self.speed < 0:
            self.image = self.__animator.animate_left()

    def __repr__(self):
        return '\n'.join([Person.__repr__(self), self.__animator.__repr__()])

    @property
    def animator(self):
        """Returns an animator attached to this object"""
        return self.__animator

    def __del__(self):
        print('Hero has been deleted')
