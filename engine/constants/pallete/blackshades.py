from dataclasses import dataclass


@dataclass(frozen=True)
class BlackShades:
    """A class that contains basic shades of black as tuples. If you
             want to change something in the fields, you have to kill yourself first."""
    black: tuple[int, int, int] = (0, 0, 0)
    graphyte: tuple[int, int, int] = (28, 28, 28)
    olive: tuple[int, int, int] = (18, 25, 16)
    purple: tuple[int, int, int] = (35, 13, 33)
    brown: tuple[int, int, int] = (53, 23, 12)
    gblue: tuple[int, int, int] = (2, 32, 39)
