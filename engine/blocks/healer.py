from engine.blocks.interactive import Interactive
from engine.roots.properties.health import Health


class Healer(Interactive):
    """A block that restores health to maximum"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str):
        super().__init__(sizes, pos, path)

    def interact(self, character):
        """Restores health if the sprite is touched"""
        self.check_touch(character)
        if self.touched:
            if isinstance(character, Health):
                character.revive()

    def __del__(self):
        print('Healer has been deleted')
