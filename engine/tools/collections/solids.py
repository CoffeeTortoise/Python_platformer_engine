from engine.roots.alt.sprite import Sprite
from engine.roots.alt.group import Group
from engine.roots.properties.gravity import Gravity
from engine.roots.properties.speed import Speed
from engine.roots.properties.jump import Jump


class Solids(Group):
    """A class for manipulating sprites and controlling block collisions with the
    player. Based on a Group class. Adds methods: ver_collisions(character),
    hor_collisions(character)."""
    def __init__(self):
        super().__init__()

    def ver_collisions(self, character):
        """Controls vertical collisions. So far, only gravity. In order for the
        character's collision with the ceiling to work, it's necessary that the
        thickness of the ceiling be approximately equal to the height of the
        character, or the distance between him and the ceiling is 3 blocks."""
        if len(self.group) != 0:
            Solids.check_character(character)
            char_pos = character.pos
            char_rect = character.rect
            for block in self.group:
                if not character.on_ground:
                    if char_rect.colliderect(block.rect):
                        if character.jumped:
                            y = block.pos[1] + block.rect.height
                            character.speed = 0
                            character.pos = char_pos[0], y
                        else:
                            y = block.pos[1] - char_rect.height * 1.1
                            character.speed = 0
                            character.on_ground = True
                            character.pos = char_pos[0], y

    def hor_collisions(self, character):
        """Controls horizontal collisions"""
        if len(self.group) != 0:
            Solids.check_character(character)
            char_rect = character.rect
            char_pos = character.pos
            w, h = char_rect.width, char_rect.height
            for block in self.group:
                delta_x = abs(char_pos[0] - block.pos[0])
                delta_y = abs(char_pos[1] - block.pos[1])
                if (delta_x <= w) and (delta_y <= h):
                    if block.rect.colliderect(character.rect):
                        if character.speed != 0:
                            character.speed = -character.speed * 4
                        else:
                            if character.right:
                                x = block.pos[0] - w * 4
                                character.pos = x, char_pos[1]
                            else:
                                x = block.pos[0] + w * 4
                                character.pos = x, char_pos[1]

    @staticmethod
    def check_character(character):
        check1 = isinstance(character, Sprite)
        check2 = isinstance(character, Gravity)
        check3 = isinstance(character, Speed)
        check4 = isinstance(character, Jump)
        if not (check1 and check2 and check3 and check4):
            raise TypeError('character be an instance of Sprite, Gravity, Speed, Jump!')

    def __del__(self):
        print('Solids have been deleted')
