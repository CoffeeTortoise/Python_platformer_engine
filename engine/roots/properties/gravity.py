from engine.tools.timer import Timer


class Gravity:
    """A class that contains gravity acting on the character. Has properties:
    gravity, max_gravity, on_ground. Has methods: apply_gravity(), reset_gravity().
    Method __repr__ has been overriden. By default, gravity is 0, on_ground is False"""
    def __init__(self, gravity: int | float = 0):
        if (type(gravity) is int) or (type(gravity) is float):
            self.__gravity: int | float = 0
            self.__max_gravity: int | float = gravity
            self.__on_ground: bool = False
            self.__timer_gravity: Timer = Timer()
        else:
            raise TypeError('gravity must be either integer or float!')

    def apply_gravity(self):
        """If the character is not on the ground, it creates a Y-axis offset
        due to gravity. To get the value, use gravity property after this method.
        If the character is on ground, gravity is 0"""
        if not self.__on_ground:
            time = self.__timer_gravity.get_time()
            self.__timer_gravity.restart()
            self.__gravity = self.__max_gravity * time
        else:
            self.__timer_gravity.restart()
            self.__gravity = 0

    def reset_gravity(self):
        """Resets the timer gravity"""
        self.__timer_gravity.restart()

    @property
    def gravity(self):
        """Something like the weight of the character as a number"""
        return self.__gravity

    @gravity.setter
    def gravity(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__gravity = new
        else:
            raise TypeError('gravity must be either integer or float!')

    @property
    def max_gravity(self):
        """Something like the max weight of the character as a number"""
        return self.__max_gravity

    @max_gravity.setter
    def max_gravity(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__max_gravity = new
        else:
            raise TypeError('gravity must be either integer or float!')

    @property
    def on_ground(self):
        """Is the character on ground?"""
        return self.__on_ground

    @on_ground.setter
    def on_ground(self, new: bool):
        if type(new) is bool:
            self.__on_ground = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'gravity: {self.__gravity}\nmax gravity: {self.__max_gravity}\non ground: {self.__on_ground}'

    def __del__(self):
        print('Gravity has been deleted')
