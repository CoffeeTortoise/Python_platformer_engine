from dataclasses import dataclass


@dataclass(frozen=True)
class RedShades:
    """A class that contains basic shades of red as tuples. There is a data class.
    If you want to change something in the fields, you have to kill yourself first."""
    red: tuple[int, int, int] = (255, 0, 0)
    crayola: tuple[int, int, int] = (238, 32, 77)
    scarlett: tuple[int, int, int] = (255, 36, 0)
    burgundy: tuple[int, int, int] = (144, 0, 32)
    cinnabar: tuple[int, int, int] = (255, 77, 0)
    tomato: tuple[int, int, int] = (161, 35, 18)
    yellow: tuple[int, int, int] = (255, 255, 0)
