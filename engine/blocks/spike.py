from engine.roots.properties.attack import Attack
from engine.blocks.trampoline import Trampoline


class Spike(Trampoline, Attack):
    """A block that deals damage and throws up. Based on a Trampoline and Attack
    classes. Method interact has been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 path: str, jump: int | float = 0,
                 attack: int | float = 0):
        Trampoline.__init__(self, sizes, pos, path, jump)
        Attack.__init__(self, attack)

    def interact(self, character):
        """Deals damage and throws up if the sprite is touched"""
        self.damage()
        Trampoline.check_touch(self, character)
        if self.touched:
            Trampoline.lift_character(self, character)
            character.hp -= self.attack

    def __repr__(self):
        return '\n'.join([Trampoline.__repr__(self),
                          Attack.__repr__(self)])

    def __del__(self):
        print('Spike has been deleted')
