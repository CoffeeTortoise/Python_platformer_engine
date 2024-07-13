from engine.tools.timer import Timer


class Jump:
    """Class that contains jump speed of a character. Has properties: jump, max_jump,
    jumped. Has method: dy(), reset_jump(). Method __repr__ has been overriden.
    By default, jump is 0, jumped is False."""
    def __init__(self, jump: int | float = 0):
        if (type(jump) is int) or (type(jump) is float):
            self.__jump: int | float = 0
            self.__max_jump: int | float = jump
            self.__jumped: bool = False
            self.__timer_jump: Timer = Timer()
        else:
            raise TypeError('jump must be either integer or float!')

    def dy(self):
        """Creates the Y-axis offset due to jump force. To get the value, use the
        jump property after this method. If the character hasn't jumped yet, the
        jump force is 0."""
        if self.__jumped:
            time = self.__timer_jump.get_time()
            self.__timer_jump.restart()
            self.__jump = self.__max_jump * time
        else:
            self.__timer_jump.restart()
            self.__jump = 0

    def reset_jump(self):
        """Resets the timer jump"""
        self.__timer_jump.restart()

    @property
    def jump(self):
        """Something like jump force of the character as a number"""
        return self.__jump

    @jump.setter
    def jump(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__jump = new
        else:
            raise TypeError('jump must be either integer or float!')

    @property
    def max_jump(self):
        """Something like max jump force of the character as a number"""
        return self.__max_jump

    @max_jump.setter
    def max_jump(self, new: int | float):
        if (type(new) is int) or (type(new) is float):
            self.__max_jump = new
        else:
            raise TypeError('jump must be either integer or float!')

    @property
    def jumped(self):
        """Did the character jump or not?"""
        return self.__jumped

    @jumped.setter
    def jumped(self, new: bool):
        if type(new) is bool:
            self.__jumped = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return f'jump: {self.__jump}\nmax jump: {self.__max_jump}\njumped: {self.__jumped}'

    def __del__(self):
        print('Jump has been deleted')
