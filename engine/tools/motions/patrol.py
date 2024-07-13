from engine.roots.properties.speed import Speed
from engine.roots.virtual.ray import Ray


class Patrol(Speed, Ray):
    """A class for creating a patrol movement. Based on a Speed and Ray classes.
    Adds method: patrol(xy). Method __repr__() has been overriden."""
    def __init__(self, speed: int | float = 0, start: int | float = 0,
                 end: int | float = 0):
        Speed.__init__(self, speed)
        Ray.__init__(self, start, end)
        self.__finish = False

    def patrol(self, xy: int | float):
        """Shifts the point to create a patrol movement along the axis."""
        if not ((type(xy) is int) or (type(xy) is float)):
            raise TypeError('xy must be either integer or float!')
        self.dx()
        self.__orient_speed()
        if (xy <= self.start) and not self.__finish:
            xy += self.speed
        elif ((xy >= self.start) and (xy < self.end)) and not self.__finish:
            xy += self.speed
        elif (xy >= self.end) and not self.__finish:
            xy += self.speed
            self.__finish = True
        elif (xy >= self.end) and self.__finish:
            xy += self.speed
        elif ((xy < self.end) and (xy > self.start)) and self.__finish:
            xy += self.speed
        elif (xy <= self.start) and self.__finish:
            xy += self.speed
            self.__finish = False
        else:
            xy += 0
        return xy

    def __orient_speed(self):
        # Created just to make possible create define_right() method
        if self.__finish:
            if self.speed > 0:
                self.speed *= -1
        else:
            if self.speed < 0:
                self.speed *= -1

    def __repr__(self):
        return '\n'.join([Speed.__repr__(self), Ray.__repr__(self)])

    def __del__(self):
        print('Patrol has been deleted')
