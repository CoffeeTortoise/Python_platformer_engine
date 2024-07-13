from engine.roots.virtual.position import Position
from engine.roots.virtual.sizes import Sizes
from engine.constants.bounds import Bounds
from engine.roots.alt.frame import Frame
from engine.roots.alt.rect import Rect


class HealthBar(Position, Sizes, Bounds):
    """Just health bar. Based on Position, Bounds and Sizes classes.
    Adds methods: update(), shift(dx, dy), draw(surface), upgrade(k).
    Method __repr__() has been overriden. Adds properties: pos, bar, frame,
    hp, on_screen. Property sizes has been overriden"""
    def __init__(self, sizes: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 frame_width: int = 1,
                 hp_color: tuple[int, int, int] = (255, 0, 0),
                 bar_color: tuple[int, int, int] = (255, 255, 255),
                 frame_color: tuple[int, int, int] = (0, 0, 0)):
        Position.__init__(self, pos)
        Sizes.__init__(self, sizes)
        Bounds.__init__(self)
        self.__hp = Rect(sizes, pos, hp_color)
        self.__bar = Rect(sizes, pos, bar_color)
        self.__frame = Frame(sizes, pos, frame_color, frame_width)
        self.__width = self.__hp.sizes[0]
        self.__on_screen = False

    def update(self):
        """There should be a logic for health bar"""
        pass

    def shift(self, dx: int | float = 0, dy: int | float = 0):
        """Shifts the health bar along the X and Y axis"""
        self.__hp.shift(dx, dy)
        self.__bar.shift(dx, dy)
        self.__frame.shift(dx, dy)

    def upgrade(self, k: int | float):
        """Changes the width of health bar depending on the k"""
        if (type(k) is int) or (type(k) is float):
            w, h = self.__hp.sizes
            self.__hp.sizes = w * k, h
        else:
            raise TypeError('k must be either integer or float!')

    def draw(self, surface):
        """Draws the health bar if it is on the screen"""
        x, y = self.__hp.vpos
        if (x >= self.hor_bounds[0]) and (x <= self.hor_bounds[1]):
            if (y >= self.ver_bounds[0]) and (y <= self.ver_bounds[1]):
                self.__on_screen = True
                self.__bar.draw(surface)
                self.__frame.draw(surface)
                self.__hp.draw(surface)
                _, h = self.__hp.sizes
                self.__hp.sizes = self.__width, h
            else:
                self.__on_screen = False
        else:
            self.__on_screen = False

    @property
    def pos(self):
        """Positions of bar, frame and health rectangles"""
        return self.__bar.vpos, self.__frame.vpos, self.__hp.vpos

    @pos.setter
    def pos(self, new: tuple[int | float, int | float]):
        self.__bar.vpos = new
        self.__frame.vpos = new
        self.__hp.vpos = new
        self.vpos = new

    @property
    def sizes(self):
        """Sizes of bar, frame and hp rectangles"""
        return self.__bar.sizes, self.__frame.sizes, self.__hp.sizes

    @sizes.setter
    def sizes(self, new: tuple[int | float, int | float]):
        self.__bar.sizes = new
        self.__frame.sizes = new
        self.__hp.sizes = new

    @property
    def bar(self):
        """Returns bar rectangle"""
        return self.__bar

    @property
    def frame(self):
        """Returns frame rectangle"""
        return self.__frame

    @property
    def hp(self):
        """Returns hp rectangle"""
        return self.__hp

    @property
    def on_screen(self):
        """Is the health bar on screen?"""
        return self.__on_screen

    @on_screen.setter
    def on_screen(self, new: bool):
        if type(new) is bool:
            self.__on_screen = new
        else:
            raise TypeError('Argument must be a boolean!')

    def __repr__(self):
        return '\n'.join([Position.__repr__(self),
                          Sizes.__repr__(self),
                          self.__hp.__repr__(),
                          self.__bar.__repr__(),
                          self.__frame.__repr__()])

    def __del__(self):
        print('HealthBar has been deleted')
