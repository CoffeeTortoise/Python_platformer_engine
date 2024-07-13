from dataclasses import dataclass


@dataclass(frozen=True)
class GreyShades:
    """A class that contains basic shades of grey as tuples. If you
          want to change something in the fields, you have to kill yourself first."""
    grey: tuple[int, int, int] = (128, 128, 128)
    agate: tuple[int, int, int] = (181, 184, 177)
    anthracite: tuple[int, int, int] = (41, 49, 51)
    basalt: tuple[int, int, int] = (78, 87, 84)
    aluminum: tuple[int, int, int] = (165, 165, 165)
    iron: tuple[int, int, int] = (67, 75, 77)
    quartz: tuple[int, int, int] = (153, 149, 140)
