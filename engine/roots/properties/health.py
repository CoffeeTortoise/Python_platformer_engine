from engine.roots.master import Master


class Health:
    """Class that can contains hp of a character as a number. Has property: hp,
     max_hp, indestructible. Method __repr__ has been overriden. Has method: revive().
     By default, hp equals to max hp, indestructible is False."""
    def __init__(self, hp: int | float = 100):
        if (type(hp) is int) or (type(hp) is float):
            self.__hp: int | float = hp
            self.__max_hp: int | float = hp
            self.__indestructible: bool = False
            master = Master()
            self.__lim_hp: int | float = master.hp
        else:
            raise TypeError('hp must be either integer or float!')

    def revive(self):
        """Fulfills the hp to the max hp"""
        self.__hp = self.__max_hp

    @property
    def hp(self):
        """Health of a character as a number"""
        if self.__indestructible:
            self.__hp = self.__lim_hp
        return self.__hp

    @hp.setter
    def hp(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__hp = new
        else:
            raise TypeError('hp must be either integer or float!')
        if self.__indestructible:
            self.__hp = self.__lim_hp

    @property
    def max_hp(self):
        """Max health of a character as a number"""
        if self.__indestructible:
            self.__max_hp = self.__lim_hp
        return self.__max_hp

    @max_hp.setter
    def max_hp(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__max_hp = new
        else:
            raise TypeError('hp must be either integer or float!')
        if self.__indestructible:
            self.__max_hp = self.__lim_hp

    @property
    def relative_hp(self):
        """Returns the ratio of the current health to the maximum"""
        return self.__hp / self.__max_hp

    @property
    def indestructible(self):
        """Is the character indestructible?"""
        return self.__indestructible

    @indestructible.setter
    def indestructible(self, new: bool):
        if type(new) is bool:
            self.__indestructible = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        if self.__indestructible:
            self.__hp = self.__lim_hp
            self.__max_hp = self.__lim_hp
        return f'HP: {self.__hp}\nMax HP: {self.__max_hp}\nIndestructible: {self.__indestructible}'

    def __del__(self):
        print('Health has been deleted')
