from engine.roots.alt.sprite import Sprite


class Interactive(Sprite):
    """A class for creating blocks that interact with player. Based on a class Sprite.
    Adds methods interact(character) and check_touch(character)."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float], path: str):
        super().__init__(sizes, pos, path)
        self.__touched = False

    def interact(self, character):
        """A method for the block to interact with the player. Should be
        overriden"""
        pass

    def check_touch(self, character):
        """Checks if character touched the sprite"""
        if isinstance(character, Sprite):
            self.__touched = False
            if self.rect.colliderect(character.rect):
                self.__touched = True
        else:
            raise TypeError('character must be an instance of Sprite')

    @property
    def touched(self):
        """Has the character touched the sprite?"""
        return self.__touched

    @touched.setter
    def touched(self, new: bool):
        if type(new) is bool:
            self.__touched = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __del__(self):
        print('Interactive block has been deleted')
