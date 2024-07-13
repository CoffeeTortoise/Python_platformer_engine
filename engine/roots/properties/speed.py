from engine.tools.timer import Timer


class Speed:
    """Class that contains speed of a character. Has properties: speed, max_speed ,
    can_go. Has methods: dx(), reset_speed(). Method __repr__ has been overriden.
     By default, speed is 0, can_go is True"""
    def __init__(self, speed: int | float = 0):
        if (type(speed) is int) or (type(speed) is float):
            self.__speed: int | float = 0
            self.__max_speed: int | float = speed
            self.__can_go: bool = True
            self.__timer_speed: Timer = Timer()
        else:
            raise TypeError('speed must be either integer or float!')

    def dx(self):
        """Creates the X-axis offset due to speed. To get the value, use
        speed property after this method. If the character cannot go, dx is 0"""
        if self.__can_go:
            time = self.__timer_speed.get_time()
            self.__timer_speed.restart()
            self.__speed = self.__max_speed * time
        else:
            self.__timer_speed.restart()
            self.__speed = 0

    def reset_speed(self):
        """Resets the timer speed"""
        self.__timer_speed.restart()

    @property
    def speed(self):
        """Speed of the character as a number"""
        return self.__speed

    @speed.setter
    def speed(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__speed = new
        else:
            raise TypeError('speed must be either integer or float!')

    @property
    def max_speed(self):
        """Max speed of the character as a number"""
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__max_speed = new
        else:
            raise TypeError('speed must be either integer or float!')

    @property
    def can_go(self):
        return self.__can_go

    @can_go.setter
    def can_go(self, new: bool):
        if type(new) is bool:
            self.__can_go = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'speed: {self.__speed}\nmax speed: {self.__max_speed}\ncan go: {self.__can_go}'

    def __del__(self):
        print('Speed has been deleted')
