from engine.blocks.interactive import Interactive
from engine.roots.properties.jump import Jump
from engine.roots.alt.sprite import Sprite


class Trampoline(Interactive, Jump):
    """A block behaving like a trampoline. Based on Interactive and Jump classes.
    Adds method lift_character(character). Methods interact(character) and __repr__()
    have been overriden. Adds property: limit_jump."""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 path: str, jump: int | float = 0):
        Interactive.__init__(self, sizes, pos, path)
        Jump.__init__(self, jump)
        self.jumped = True
        self.__limit: int | float = 0

    def interact(self, character):
        """Throws the character into the air when touched"""
        Interactive.check_touch(self, character)
        if self.touched:
            self.lift_character(character)

    def lift_character(self, character):
        """Lifts the character"""
        if isinstance(character, Sprite):
            self.__limit = character.rect.height * 6
            self.__lim_jump()
            x, y = character.pos[0], character.pos[1] + self.jump
            character.pos = x, y
        else:
            raise TypeError('character must be an instance of Sprite!')

    def __lim_jump(self):
        # Limits the height of the jump
        self.dy()
        if abs(self.jump) >= self.__limit:
            self.jump = -self.__limit

    @property
    def limit_jump(self):
        """Max height of the jump"""
        return self.__limit

    @limit_jump.setter
    def limit_jump(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__limit = new
        else:
            raise TypeError('limit must be either integer or float!')

    def __repr__(self):
        return '\n'.join([Interactive.__repr__(self), Jump.__repr__(self)])

    def __del__(self):
        print('Trampoline has been deleted')
