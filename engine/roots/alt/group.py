from engine.roots.alt.sprite import Sprite
from copy import deepcopy
from typing import Self


class Group:
    """A class for storing and manipulating sprites. The shell above python list.
     Has property: group. Has methods: updates(). draws(surface), shifts(dx, dy),
     all_pos(), all_sizes(), append(item), insert(index, item), remove(item), clear().
     Can be indexed, has a length. Methods __repr__ and __eq__ have been overriden."""
    def __init__(self):
        self.__group: list[Sprite] = []

    def updates(self):
        """Activates the update method for all sprites in the group."""
        if len(self.__group) != 0:
            for sprite in self.__group:
                sprite.update()

    def draws(self, surface):
        """Activates the draw method for all sprites in the group"""
        if len(self.__group) != 0:
            for sprite in self.__group:
                sprite.draw(surface)

    def shifts(self, dx: int | float = 0, dy: int | float = 0):
        """Activates the shift method for all sprites in the group"""
        check1 = (type(dx) is int) or (type(dx) is float)
        check2 = (type(dy) is int) or (type(dy) is float)
        if check1 and check2:
            if len(self.__group) != 0:
                for sprite in self.__group:
                    sprite.shift(dx, dy)
        else:
            raise TypeError('Arguments must be either integers or floats!')

    def all_pos(self):
        """Returns positions of all sprites in the group as 2d tuple"""
        if len(self.__group) != 0:
            return tuple(sprite.pos for sprite in self.__group)
        else:
            return tuple()

    def all_sizes(self):
        """Returns sizes of all sprites in the group as 2d tuple"""
        if len(self.__group) != 0:
            return tuple(sprite.sizes for sprite in self.__group)
        else:
            return tuple()

    def all_image(self):
        """Returns image for each sprite in the group as a tuple"""
        if len(self.__group) != 0:
            return tuple(sprite.image for sprite in self.__group)
        else:
            return tuple()

    def all_rect(self):
        """Returns rect for each sprite in the group as a tuple"""
        if len(self.__group) != 0:
            return tuple(sprite.rect for sprite in self.__group)
        else:
            return tuple()

    def append(self, item: Sprite):
        if isinstance(item, Sprite):
            self.__group.append(item)
        else:
            raise TypeError('item must be an instance of Sprite!')

    def insert(self, index: int, item: Sprite):
        if isinstance(item, Sprite):
            self.__group.insert(index, item)
        else:
            raise TypeError('item must be an instance of Sprite')

    def remove(self, item: Sprite):
        if isinstance(item, Sprite):
            self.__group.remove(item)
        else:
            raise TypeError('item must be an instance of Sprite')

    def clear(self):
        self.__group = []

    @property
    def group(self):
        """A list with the elements of this group"""
        return self.__group

    @group.setter
    def group(self, new: Self):
        if type(new) is type(self):
            self.__group = deepcopy(new)
        else:
            raise TypeError('Argument must be a same type!')

    def __repr__(self):
        if len(self.__group) != 0:
            list_ = [sprite.__repr__() for sprite in self.__group]
            res = ''.join((info + '\n') for info in list_)
            return res
        else:
            return 'Empty list for sprites'

    def __len__(self):
        return len(self.__group)

    def __getitem__(self, index: int):
        if (index >= 0) and (index < len(self)):
            return self.__group[index]
        else:
            return None

    def __setitem__(self, index: int, value: Sprite):
        if (index >= 0) and (index < len(self)):
            if isinstance(value, Sprite):
                self.__group[index] = value
            else:
                raise TypeError('item be an instance of Sprite!')

    def __eq__(self, other: Self):
        if len(self) == len(other):
            res = True
            for i in range(len(self)):
                compare = self[i] == other[i]
                res = res and compare
            return res
        else:
            return False

    def __del__(self):
        print('Group has been deleted')
