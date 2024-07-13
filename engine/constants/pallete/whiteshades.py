from dataclasses import dataclass


@dataclass(frozen=True)
class WhiteShades:
    """A class that contains basic shades of white as tuples. If you
      want to change something in the fields, you have to kill yourself first."""
    white: tuple[int, int, int] = (255, 255, 255)
    snow: tuple[int, int, int] = (255, 250, 250)
    antique: tuple[int, int, int] = (250, 235, 215)
    pearl: tuple[int, int, int] = (234, 230, 202)
    cream: tuple[int, int, int] = (253, 244, 227)
    papyrus: tuple[int, int, int] = (84, 87, 60)
