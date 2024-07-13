from engine.characters.base.monos.falling import Falling


class Dropping(Falling):
    """The player's falling character. Based on Falling class. Method update
    has been overriden."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str,
                 hp: int | float = 100, playable: bool = True,
                 gravity: int | float = 0):
        super().__init__(sizes, pos, path, hp, playable, gravity)

    def update(self):
        self.apply_gravity()
        self.control_death()

    def __del__(self):
        print('Dropping has been deleted')
