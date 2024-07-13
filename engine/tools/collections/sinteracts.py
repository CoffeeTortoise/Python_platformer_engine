from engine.tools.collections.solids import Solids
from engine.blocks.interactive import Interactive
from engine.roots.alt.sprite import Sprite


class SolidInteracts(Solids):
    """Controls interaction with solid blocks. Based on Solids class. Adds method
    interacts(character). Methods append(item), insert(index, item), remove(item)
    have been overriden"""
    def __init__(self):
        super().__init__()

    def append(self, item: Interactive):
        if isinstance(item, Interactive):
            super().append(item)
        else:
            raise TypeError('item must be an instance of Interactive!')

    def insert(self, index: int, item: Interactive):
        if isinstance(item, Interactive):
            super().insert(index, item)
        else:
            raise TypeError('item must be an instance of Interactive!')

    def remove(self, item: Interactive):
        if isinstance(item, Interactive):
            super().remove(item)
        else:
            raise TypeError('item must be an instance of Interactive!')

    def interacts(self, character):
        """Calls the interact method for blocks"""
        if len(self.group) != 0:
            if isinstance(character, Sprite):
                for block in self.group:
                    block.interact(character)
            else:
                raise TypeError('character must be an instance of Sprite!')

    def __del__(self):
        print('Interacts has been deleted')
