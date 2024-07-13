import time as tm


class Timer:
    """A simple timer. Have methods: get_time(), restart()"""
    def __init__(self):
        self.__buffer: int | float = 0
        self.__time_before: int | float = 0
        self.__redo: bool = False

    def get_time(self):
        """Returns the time in seconds with a small error"""
        if not self.__redo:
            self.__time_before = tm.time()
            self.__redo = True
        else:
            time_now: int | float = tm.time()
            time_elapsed: int | float = time_now - self.__time_before
            self.__buffer += time_elapsed
            self.__redo = False
        return self.__buffer

    def restart(self):
        """Restarts the timer if more then 0 seconds have been accumulated"""
        if self.__buffer != 0:
            self.__buffer = 0
            self.__time_before = 0
            self.__redo = False

    def __del__(self):
        print('Timer has been deleted')
