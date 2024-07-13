from engine.tools.timer import Timer


class Attack:
    """Class that contains an attack of a character as a number.
    Has properties: attack, max_attack, harmful. Has methods: damage(), reset_attack().
    Method __repr__ has been overriden. By default, attack is 0, harmful is True"""
    def __init__(self, attack: int | float = 0):
        if (type(attack) is int) or (type(attack) is float):
            self.__attack: int | float = 0
            self.__max_attack: int | float = attack
            self.__harmful: bool = True
            self.__timer_attack: Timer = Timer()
        else:
            raise TypeError('attack must be an integer or float!')

    def damage(self):
        """Creates damage that a character can inflict. To get the value, use the
        attack property after this method. If a character not harmful, damage is 0"""
        if self.__harmful:
            time = self.__timer_attack.get_time()
            self.__timer_attack.restart()
            self.__attack = self.__max_attack * time
        else:
            self.__timer_attack.restart()
            self.__attack = 0

    def reset_attack(self):
        """Resets the timer attack"""
        self.__timer_attack.restart()

    @property
    def attack(self):
        """Attack of a character as a number."""
        return self.__attack

    @attack.setter
    def attack(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__attack = new
        else:
            raise TypeError('Argument must be either integer or float!')

    @property
    def max_attack(self):
        """Max attack of a character as a number"""
        return self.__max_attack

    @max_attack.setter
    def max_attack(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__max_attack = new
        else:
            raise TypeError('Argument must be either integer or float!')

    @property
    def harmful(self):
        """Character's ability to cause damage"""
        return self.__harmful

    @harmful.setter
    def harmful(self, new: bool):
        if type(new) is bool:
            self.__harmful = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'attack: {self.__attack}\nmax attack: {self.__max_attack}\nharmful: {self.__harmful}'

    def __del__(self):
        print('Attack has been deleted')
