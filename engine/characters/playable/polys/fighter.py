from engine.characters.playable.polys.hero import Hero
from engine.roots.properties.attack import Attack
from engine.tools.healthbar import HealthBar


class Fighter(Hero, Attack):
    """Playable character with motion animation, health bar and attack. Based on
    Hero and Attack classes. Methods update(), draw(surface), shift(dx, dy),
    control_death() and __repr__() have been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], paths: list[str],
                 hp: int | float = 100, playable: bool = True,
                 gravity: int | float = 0, jump: int | float = 0,
                 speed: int | float = 0, slow: bool = False,
                 attack: int | float = 0,
                 frame_width: int = 1,
                 hp_color: tuple[int, int, int] = (255, 0, 0),
                 bar_color: tuple[int, int, int] = (255, 255, 255),
                 frame_color: tuple[int, int, int] = (0, 0, 0)):
        Hero.__init__(self, sizes, pos, paths, hp, playable,
                      gravity, jump, speed, slow)
        Attack.__init__(self, attack)
        hp_sizes = sizes[0] * 3, sizes[1] / 5
        hp_pos = pos[0], pos[1] - sizes[1]
        self.__health_bar = HealthBar(hp_sizes, hp_pos, frame_width, hp_color,
                                      bar_color, frame_color)

    def update(self):
        self.damage()
        Hero.update(self)
        self.__health_bar.upgrade(self.relative_hp)

    def draw(self, surface):
        Hero.draw(self, surface)
        if self.on_screen and self.hp > 0:
            self.__health_bar.draw(surface)

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        Hero.shift(self, dx, dy)
        self.__health_bar.shift(dx, dy)
        hp_x = self.pos[0] - self.sizes[0]
        hp_y = self.pos[1] - self.sizes[1]
        self.__health_bar.pos = hp_x, hp_y

    def control_death(self):
        if self.hp <= 0:
            self.speed = 0
            self.jump = 0
            self.gravity = 0
            self.attack = 0

    def __repr__(self):
        return '\n'.join([Hero.__repr__(self),
                          Attack.__repr__(self),
                          self.__health_bar.__repr__()])

    def __del__(self):
        print('Fighter has been deleted')
