from engine.characters.base.monos.mobster import Mobster
from engine.tools.collections.animator import Animator


class Monster(Mobster):
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 paths: list[str], jump: int | float = 0,
                 attack: int | float = 0,
                 speed: int | float = 0,
                 start: int | float = 0,
                 end: int | float = 0,
                 hp: int | float = 100,
                 playable: bool = False,
                 slow: bool = False):
        super().__init__(sizes, pos, paths[0], jump, attack, speed,
                         start, end, hp, playable)
        self.__animator = Animator(paths, sizes, slow)

    def change_image(self):
        self.define_right()
        if self.patrol.speed != 0:
            self.animation()
        else:
            self.turn_image()

    def animation(self):
        if self.patrol.speed > 0:
            self.image = self.__animator.animate_right()
        if self.patrol.speed < 0:
            self.image = self.__animator.animate_left()

    @property
    def animator(self):
        return self.__animator

    def __repr__(self):
        return '\n'.join([super().__repr__(),
                          self.__animator.__repr__()])

    def __del__(self):
        print('Monster has been deleted')
